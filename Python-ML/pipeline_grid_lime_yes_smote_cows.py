# Import necessary libraries for modeling, preprocessing, evaluation, explainability, and file I/O
from IPython.core.pylabtools import figsize
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score, precision_score, \
    recall_score
from sklearn.neural_network import MLPClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from networkx.drawing.tests.test_pylab import plt
import pandas as pd
import numpy as np
from lime.lime_tabular import LimeTabularExplainer
from functools import partial  # Used to create partial functions for LIME
from lime import submodular_pick
from imblearn.over_sampling import SMOTENC
import pickle
import seaborn as sns
import os

# Custom prediction wrapper for LIME compatibility
def custom_predict_proba(X, model):
    X_str = convert_to_lime_format(X, categorical_names, col_names=X_train.columns, invert=True)
    return model.predict_proba(X_str)

# Load and preprocess dataset
GROUPC = pd.read_csv("C:/Users/jspre/PycharmProjects/Coursework4thyear/cleanData/group-c.csv")

# Encode categorical variables into numerical values
GROUPC['LCT_CALVING_EASE'].replace(to_replace=['A', 'N', 'FN', 'VN', 'FM', 'VM', 'VC'], value=[1, 2, 3, 4, 5, 6, 7], inplace=True)
GROUPC['month(WEIGHT_DATE)'].replace(to_replace=[12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                                     value=['Winter', 'Winter', 'Winter', 'Spring', 'Spring','Spring', 'Summer', 'Summer', 'Summer', 'Autumn', 'Autumn', 'Autumn'], inplace=True)
GROUPC['majfeedtype'].replace(to_replace=['XB', 'xb', 'DR', 'dr', 'ZZ', 'zz', 'XH', 'xh', 'XM', 'xm', 'HE', 'he', 'XE', 'xe', 'ST', 'st', 'NT', 'nt'],
                              value=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9], inplace=True)
GROUPC['majfeedtype'] = GROUPC.majfeedtype.astype(float)

# Convert multi-class LOCO_SCORE to binary
GROUPC['LOCO_SCORE'].replace(to_replace=[1, 2, 3, 4, 5], value=[0, 0, 1, 1, 1], inplace=True)

# Function to convert data to/from LIME compatible format
def convert_to_lime_format(X, categorical_names, col_names=None, invert=False):
    """Converts data with categorical values into LIME's integer format or back"""
    if not isinstance(X, pd.DataFrame):
        X_lime = pd.DataFrame(X, columns=col_names)
    else:
        X_lime = X.copy()

    for k, v in categorical_names.items():
        if not invert:
            label_map = {str_label: int_label for int_label, str_label in enumerate(v)}
        else:
            label_map = {int_label: str_label for int_label, str_label in enumerate(v)}

        X_lime.iloc[:, k] = X_lime.iloc[:, k].map(label_map)

    return X_lime

# Clean dataset: remove or encode unnecessary features
GROUPC['LCT_RECORDER_TYPE'].replace(to_replace=['CA', 'CU'], value=[1, 2], inplace=True)
GROUPC.drop('DAM_GENETIC_GROUP', 1, inplace=True)
GROUPC.drop('WEIGHT_DATE', 1, inplace=True)
GROUPC.drop('LCT_DRYING_DATE', 1, inplace=True)
GROUPC.drop('LCT_LACT_START_DATE', 1, inplace=True)
GROUPC.drop('LCT_CALVING_DATE', 1, inplace=True)
GROUPC.drop('FEEDTYPE', 1, inplace=True)
GROUPC.drop('LCT_DOB', 1, inplace=True)
GROUPC.drop('BCS_IDENT', 1, inplace=True)

# Drop columns with specific patterns
GROUPC = GROUPC[GROUPC.columns.drop(list(GROUPC.filter(regex='Group_Concat')))]
GROUPC = GROUPC[GROUPC.columns.drop(list(GROUPC.filter(regex='group_concat')))]

# Group data per individual cow
grouped = GROUPC.groupby(GROUPC.EAR_TAG)
DF_list = []
for group in grouped.groups:
    loopframe = grouped.get_group(group)
    loopframe.drop('birth_wgt', 1, inplace=True)
    loopframe.drop('DAM_HOLSTEIN_PERC', 1, inplace=True)
    loopframe.drop('DAM_NO_OF_LACTS', 1, inplace=True)
    loopframe.drop('cnt', 1, inplace=True)
    loopframe.drop('day(WEIGHT_DATE)', 1, inplace=True)
    loopframe = loopframe[loopframe.columns.drop(list(loopframe.filter(regex='DAM')))]
    DF_list.append(loopframe)

# Setup model configuration
Y_col = 'LOCO_SCORE'
classifier = MLPClassifier(max_iter=4000, random_state=42)
scaler = StandardScaler()
cows = {}

# Define feature lists
l1 = list(DF_list[0].columns)
l2 = ["RECORDER", "LACT_NO", "COND_SCORE", "LCT_RECORDER_TYPE", "LCT_CALVING_COND_SCORE",
      "LCT_Calving_WGT", "LCT_CALVING_EASE", "LCT_NO_OF_CALVES","LCT_NO_OF_CALVES_DEAD", "LCT_DRYING_WGT",
      "LCT_DRYING_COND_SCORE", "LCT_RECORDER", "majfeedtype", "YEAR(WEIGHT_DATE)", "month(WEIGHT_DATE)","FEED_GROUP"]
l3 = [x for x in l1 if x not in l2]
numeric_features = l3
numeric_features.remove("LOCO_SCORE")
numeric_features.remove("EAR_TAG")
categorical_features = l2

# Hyperparameter grid for model tuning
param_grid = {
    "classifier__hidden_layer_sizes": [(224, 112), 112, (448, 224, 112)],
    'classifier__activation': ['logistic'],
    'classifier__solver': ['adam'],
}

# Train model for each individual cow
for frame in DF_list:
    id = frame.EAR_TAG.array[0]
    print(id)
    a = os.path.exists(str(id)+"/smote-yes/important_features_grouped")
    if not a:
        frame.drop('EAR_TAG', 1, inplace=True)
        categorical_names = {}
        categorical_features_smote=[]
        X_cols = frame.loc[:, frame.columns != Y_col].columns
        X_train, X_test, y_train, y_test = train_test_split(frame[X_cols], frame[Y_col], test_size=0.2, random_state=42)

        for col in l2:
            categorical_names[X_train.columns.get_loc(col)] = (list(frame[col].unique()))
            categorical_features_smote.append(X_train.columns.get_loc(col))

        if y_train.value_counts()[1] > 8 and y_train.value_counts()[0] > 8 and 1 in y_test.values:

            # Perform SMOTENC oversampling
            sampling_strategy = {0: y_train.value_counts()[0] * 20, 1: y_train.value_counts()[1] * 20}
            sm = SMOTENC(sampling_strategy=sampling_strategy, random_state=42, k_neighbors=5,
                         categorical_features=categorical_features_smote, n_jobs=-1)
            print(np.bincount(y_train))
            X_res, y_res = sm.fit_resample(X_train, y_train)

            # Create preprocessing pipelines
            numeric_transformer = Pipeline(steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())])
            categorical_transformer = OneHotEncoder(handle_unknown="ignore")
            preprocessor = ColumnTransformer(transformers=[
                ("num", numeric_transformer, numeric_features),
                ("cat", categorical_transformer, categorical_features),
            ])

            # Full pipeline with classifier
            clf = Pipeline(steps=[("preprocessor", preprocessor), ("classifier", classifier)])
            scoring = 'f1' if y_train.value_counts()[0] > y_train.value_counts()[1] else 'balanced_accuracy'

            # Grid search cross-validation
            grid_search = GridSearchCV(clf, param_grid, cv=5, scoring=scoring)
            grid_search.fit(X_res, y_res)
            print(scoring)
            print('Best parameters found:\n', grid_search.best_params_)
            print("model score: %.3f" % grid_search.score(X_test, y_test))
            bestparamter = grid_search.best_params_
            score = grid_search.score(X_test, y_test)

            # Evaluate model and print results
            y_pred = grid_search.predict(X_test)
            txtreport = classification_report(y_test, y_pred)
            matrix = confusion_matrix(y_test, y_pred)
            print(txtreport)
            print(matrix)

            # Save confusion matrix as heatmap
            group_names = ['True Neg', 'False Pos', 'FalseNeg', 'TruePos']
            group_counts = ['{0:0.0f}'.format(value) for value in matrix.flatten()]
            group_percentages = ['{0:.2%}'.format(value) for value in matrix.flatten() / np.sum(matrix)]
            labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in zip(group_names, group_counts, group_percentages)]
            labels = np.asarray(labels).reshape(2, 2)
            cnf_matrix = sns.heatmap(matrix, annot=labels, fmt='', cmap='Blues')
            cnf_matrix.get_figure().savefig(str(id) + "/smote-yes/confusion_matrix.png")

            # Save model and evaluation metrics
            pickle.dump(grid_search, open(str(id) + "/smote-yes/model_balance_nosmote", 'wb'))
            pickle.dump(txtreport, open(str(id) + "/smote-yes/class_report", 'wb'))
            pickle.dump(matrix, open(str(id) + "/smote-yes/confusion_matrix", 'wb'))
            pickle.dump(bestparamter, open(str(id) + "/smote-yes/bestparameter", 'wb'))
            pickle.dump(score, open(str(id) + "/smote-yes/score", 'wb'))
            pickle.dump(accuracy_score(y_test, y_pred), open(str(id) + "/smote-yes/acc-score", 'wb'))
            pickle.dump(precision_score(y_test, y_pred), open(str(id) + "/smote-yes/prc-score", 'wb'))
            pickle.dump(recall_score(y_test, y_pred), open(str(id) + "/smote-yes/rec-score", 'wb'))
            pickle.dump(f1_score(y_test, y_pred), open(str(id) + "/smote-yes/f1-score", 'wb'))

            # Generate and save LIME explanation
            explainer = LimeTabularExplainer(convert_to_lime_format(X_train, categorical_names).values,
                                             mode="classification",
                                             feature_names=X_train.columns.tolist(),
                                             categorical_names=categorical_names,
                                             categorical_features=categorical_names.keys(),
                                             class_names=['good', 'lame'],
                                             discretize_continuous=True,
                                             random_state=42)

            i = 7
            observation = convert_to_lime_format(X_test.iloc[[i], :], categorical_names).values[0]
            mlp_predict_proba = partial(custom_predict_proba, model=grid_search)
            mlp_explanation = explainer.explain_instance(observation, mlp_predict_proba, num_features=14)
            print(str(id) + ".html")
            mlp_explanation.save_to_file(str(id) + "/smote-yes/mlpexplnation.html")
            print("end")

            # Submodular pick for global feature importance
            sp_obj = submodular_pick.SubmodularPick(explainer,
                                                    convert_to_lime_format(X_train, categorical_names).values,
                                                    mlp_predict_proba, sample_size=20, num_features=14,
                                                    num_exps_desired=5)
            print(sp_obj.explanations)
            W_matrix = pd.DataFrame([dict(this.as_list(this.available_labels()[0])) for this in sp_obj.explanations]).fillna(0)
            matrix_mean = W_matrix.mean()
            W_matrix['prediction'] = [this.available_labels()[0] for this in sp_obj.explanations]

            # Save feature importance plots
            plt.figure(figsize(6.4, 6))
            plt.title("Feature Importance")
            plt.xlabel("Importance")
            plt.ylabel("Features")
            newplot = np.abs(W_matrix.drop("prediction", axis=1)).mean(axis=0).sort_values(ascending=False).head(32).sort_values(ascending=True).plot.barh()
            newplot.figure.savefig(str(id) + "/smote-yes/featureimportance2.pdf", bbox_inches='tight')
            plt.close()

            grped_coeff = W_matrix.groupby("prediction").mean()
            grped_coeff = grped_coeff.rename(index={0: 'LOCO_SCORE 1,2', 1: 'LOCO_SCORE 3,4,5'})
            pickle.dump(grped_coeff, open(str(id) + "/smote-yes/important_features_grouped", 'wb'))

            grped_coeff = grped_coeff.T
            grped_coeff["abs"] = np.abs(grped_coeff.iloc[:, 0])
            grped_coeff.sort_values("abs", inplace=True, ascending=False)
            plt.figure(figsize(6.4, 6))
            newplot2 = grped_coeff.head(32).sort_values("abs", ascending=True).drop("abs", axis=1).plot.barh()
            newplot2.set_title("Feature Importance")
            newplot2.set_xlabel("Importance")
            newplot2.set_ylabel("Features")
            newplot2.figure.savefig(str(id) + "/smote-yes/featureimportance3.pdf", bbox_inches='tight')
            plt.close()

            pickle.dump(matrix_mean, open(str(id) + "/smote-yes/important_features", 'wb'))
            plt.figure(figsize(15, 6))
            plt.title("Feature Importance")
            plt.xlabel("Features")
            plt.ylabel("Importance")
            plt.grid(visible=True, which='major', axis='both')
            plot = matrix_mean.sort_values(ascending=False).plot.bar()
            plot.figure.savefig(str(id) + "/smote-yes/featureimportance.pdf", bbox_inches='tight')
            print("hi")
        else:
            print("skip")
    else:
        print("finished")
