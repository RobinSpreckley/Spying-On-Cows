# Import essential libraries for modeling, preprocessing, evaluation, explainability, and I/O
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
from functools import partial  # For wrapping model predict function for LIME
from lime import submodular_pick
from imblearn.over_sampling import SMOTENC
import pickle
import seaborn as sns
import os

# Wrapper for converting data to LIME-compatible format and getting prediction probabilities
def custom_predict_proba(X, model):
    X_str = convert_to_lime_format(X, categorical_names, col_names=X_train.columns, invert=True)
    return model.predict_proba(X_str)

# Load cleaned dataset
GROUPC = pd.read_csv("C:/Users/jspre/PycharmProjects/Coursework4thyear/cleanData/group-c.csv")

# Encode categorical variables into numeric formats
GROUPC['LCT_CALVING_EASE'].replace(to_replace=['A', 'N', 'FN', 'VN', 'FM', 'VM', 'VC'], value=[1, 2, 3, 4, 5, 6, 7], inplace=True)
GROUPC['month(WEIGHT_DATE)'].replace(to_replace=[12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                                     value=['Winter', 'Winter', 'Winter', 'Spring', 'Spring','Spring', 'Summer', 'Summer', 'Summer', 'Autumn', 'Autumn', 'Autumn'], inplace=True)
GROUPC['majfeedtype'].replace(to_replace=['XB', 'xb', 'DR', 'dr', 'ZZ', 'zz', 'XH', 'xh', 'XM', 'xm', 'HE', 'he', 'XE', 'xe', 'ST', 'st', 'NT', 'nt'],
                              value=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9], inplace=True)
GROUPC['majfeedtype'] = GROUPC.majfeedtype.astype(float)

# Binarize LOCO_SCORE into 0 and 1
GROUPC['LOCO_SCORE'].replace(to_replace=[1, 2, 3, 4, 5], value=[0, 0, 1, 1, 1], inplace=True)

# Utility function for LIME: convert categorical columns to/from integer encoding
def convert_to_lime_format(X, categorical_names, col_names=None, invert=False):
    """Convert categorical string values to integer encodings and vice versa for LIME compatibility"""
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

# Filter dataset to only include specific cow IDs
with open('idlist', 'rb') as f:
    lr2 = pickle.load(f)
    print(GROUPC)
GROUPC = GROUPC[GROUPC.EAR_TAG.isin(lr2)]

# Drop redundant or irrelevant columns
GROUPC['LCT_RECORDER_TYPE'].replace(to_replace=['CA', 'CU'], value=[1, 2], inplace=True)
GROUPC.drop('DAM_GENETIC_GROUP', 1, inplace=True)
GROUPC.drop('DAM_BOOk_NO', 1, inplace=True)
GROUPC.drop('LCT_DRYING_DATE', 1, inplace=True)
GROUPC.drop('LCT_LACT_START_DATE', 1, inplace=True)
GROUPC.drop('LCT_CALVING_DATE', 1, inplace=True)
GROUPC.drop('FEEDTYPE', 1, inplace=True)
GROUPC.drop('LCT_DOB', 1, inplace=True)
GROUPC.drop('BCS_IDENT', 1, inplace=True)
GROUPC.drop('MC_FEED_GROUP', 1, inplace=True)
GROUPC.drop('DAM_DAM_CODE', 1, inplace=True)
GROUPC.drop('DAM_SIRE_CODE', 1, inplace=True)
GROUPC.drop('DAM_FAMILY_NO', 1, inplace=True)
GROUPC = GROUPC[GROUPC.columns.drop(list(GROUPC.filter(regex='Group_Concat')))]
GROUPC = GROUPC[GROUPC.columns.drop(list(GROUPC.filter(regex='group_concat')))]
GROUPC.drop('day(WEIGHT_DATE)', 1, inplace=True)
GROUPC.drop('cnt', 1, inplace=True)  # Possibly count of records per cow

# Group data by individual cow
DF_list = []
grouped = GROUPC.groupby(GROUPC.EAR_TAG)
for group in grouped.groups:
    loopframe = grouped.get_group(group)
    DF_list.append(loopframe)

# Define modeling components
Y_col = 'LOCO_SCORE'
classifier = MLPClassifier(max_iter=4000, random_state=42)
scaler = StandardScaler()
cows = {}

# Identify numeric and categorical features
l1 = list(GROUPC.columns)
l2 = ["RECORDER", "LACT_NO", "COND_SCORE", "LCT_RECORDER_TYPE", "LCT_CALVING_COND_SCORE",
      "LCT_CALVING_EASE", "LCT_NO_OF_CALVES","LCT_NO_OF_CALVES_DEAD", "LCT_DRYING_WGT",
      "LCT_DRYING_COND_SCORE", "LCT_RECORDER", "majfeedtype", "YEAR(WEIGHT_DATE)", "month(WEIGHT_DATE)","FEED_GROUP","DAM_INHERD",
      "DAM_NO_OF_LACTS","DAM_HOLSTEIN_PERC","WEIGHT_DATE","EAR_TAG"]
l3 = [x for x in l1 if x not in l2]
numeric_features = l3
numeric_features.remove("LOCO_SCORE")
categorical_features = l2

# Define hyperparameter grid for MLP
param_grid = {
    "classifier__hidden_layer_sizes": [117],
    'classifier__activation': ['logistic'],
    'classifier__solver': ['adam'],
}

# Prepare global train/test sets
X_traint = pd.DataFrame()
X_testt = pd.DataFrame()
y_traint= pd.Series()
y_testt= pd.Series()
X_testtl= []
y_testtl= []
x_traintl= []
categorical_names = {}
categorical_features_smote=[]

# Split each cow’s data and collect for herd-level training
for frame in DF_list:
    X_cols = frame.loc[:, frame.columns != Y_col].columns
    X_train, X_test, y_train, y_test = train_test_split(frame[X_cols], frame[Y_col], test_size=0.2, random_state=42)
    print("hi")
    X_traint=X_traint.append(X_train)
    X_testt=X_testt.append(X_test)
    y_traint= y_traint.append(y_train)
    y_testt=y_testt.append(y_test)
    X_testtl.append(X_test)
    y_testtl.append(y_test)
    x_traintl.append(X_train)

print((X_test.iloc[[0], :]))

# Combine all cow data for model training
X_train=X_traint
X_test=X_testt
y_train=y_traint
y_test=y_testt

# Define categorical mappings for LIME
for col in l2:
    categorical_names[X_train.columns.get_loc(col)] = (list(GROUPC[col].unique()))
    categorical_features_smote.append(X_train.columns.get_loc(col))

# Only proceed if class distribution is sufficient
if y_train.value_counts()[1] > 8 and y_train.value_counts()[0] > 8 and 1 in y_test.values:

    # Build preprocessing pipelines
    numeric_transformer = Pipeline(steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())])
    categorical_transformer = OneHotEncoder(handle_unknown="ignore")
    preprocessor = ColumnTransformer(transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ])

    # Create full modeling pipeline
    clf = Pipeline(steps=[("preprocessor", preprocessor), ("classifier", classifier)])

    # Use appropriate scoring based on imbalance
    if y_train.value_counts()[0] > y_train.value_counts()[1]:
        scoring = 'f1'
    else:
        scoring = 'balanced_accuracy'

    # Grid search with CV
    grid_search = GridSearchCV(clf, param_grid, cv=5, scoring=scoring)
    grid_search.fit(X_train, y_train)
    print(scoring)
    print('Best parameters found:\n', grid_search.best_params_)
    print("model score: %.3f" % grid_search.score(X_test, y_test))
    bestparamter = grid_search.best_params_
    print(grid_search.n_features_in_)
    score = grid_search.score(X_test, y_test)

    # Evaluate model per cow
    i=0
    accuracy = []
    precision = []
    recall = []
    f1 = []

    for series in X_testtl:
        y_pred = grid_search.predict(X_testtl[i])
        accuracy.append(accuracy_score(y_testtl[i], y_pred))
        precision.append(precision_score(y_testtl[i], y_pred))
        recall.append(recall_score(y_testtl[i], y_pred))
        f1.append(f1_score(y_testtl[i], y_pred))
        i=i+1

    # Save metrics
    pickle.dump(accuracy, open("herd_no_smote/acc-score_val_list", 'wb'))
    pickle.dump(precision, open("herd_no_smote/prc-score_val_list", 'wb'))
    pickle.dump(recall, open("herd_no_smote/rec-score_val_list", 'wb'))
    pickle.dump(f1, open("herd_no_smote/f1-score_val_list", 'wb'))
    print("nocrash")

    # Evaluate and save final predictions
    y_pred = grid_search.predict(X_test)
    txtreport = classification_report(y_test, y_pred)
    matrix = confusion_matrix(y_test, y_pred)
    print(txtreport)
    print(matrix)

    # Save confusion matrix heatmap
    group_names = ['TrueNeg', 'FalsePos', 'FalseNeg', 'TruePos']
    group_counts = ['{0:0.0f}'.format(value) for value in matrix.flatten()]
    group_percentages = ['{0:.2%}'.format(value) for value in matrix.flatten() / np.sum(matrix)]
    labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in zip(group_names, group_counts, group_percentages)]
    labels = np.asarray(labels).reshape(2, 2)
    cnf_matrix = sns.heatmap(matrix, annot=labels, fmt='', cmap='Blues')
    cnf_matrix.get_figure().savefig("herd_no_smote/confusion_matrix_val.png")

    # Save model and evaluation artifacts
    pickle.dump(grid_search, open("herd_no_smote/model_balance_nosmote_val", 'wb'))
    pickle.dump(txtreport, open("herd_no_smote/class_report_val", 'wb'))
    pickle.dump(matrix, open("herd_no_smote/confusion_matrix_val", 'wb'))
    pickle.dump(bestparamter, open("herd_no_smote/bestparameter_val", 'wb'))
    pickle.dump(score, open("herd_no_smote/score_val", 'wb'))
    pickle.dump(accuracy_score(y_test, y_pred), open("herd_no_smote/acc-score_val", 'wb'))
    pickle.dump(precision_score(y_test, y_pred), open("herd_no_smote/prc-score_val", 'wb'))
    pickle.dump(recall_score(y_test, y_pred), open("herd_no_smote/rec-score_val", 'wb'))
    pickle.dump(f1_score(y_test, y_pred), open("herd_no_smote/f1-score_val", 'wb'))

    # Create and save LIME explanation for a sample
    explainer = LimeTabularExplainer(convert_to_lime_format(X_train, categorical_names).values,
                                     mode="classification",
                                     feature_names=X_train.columns.tolist(),
                                     categorical_names=categorical_names,
                                     categorical_features=categorical_names.keys(),
                                     class_names=['good', 'lame'],
                                     discretize_continuous=True,
                                     random_state=42)

    i = 0
    observation = convert_to_lime_format(X_test.iloc[[i], :], categorical_names).values[0]
    mlp_predict_proba = partial(custom_predict_proba, model=grid_search)
    mlp_explanation = explainer.explain_instance(observation, mlp_predict_proba, num_features=14)
    print(".html")
    mlp_explanation.save_to_file("herd_no_smote/mlpexplnation_val.html")
    print("end")

    # Generate and plot submodular pick LIME explanations per cow
    for series in X_testtl:
        y_pred = grid_search.predict(X_testtl[i])
        accuracy.append(accuracy_score(y_testtl[i], y_pred))
        precision.append(precision_score(y_testtl[i], y_pred))
        recall.append(recall_score(y_testtl[i], y_pred))
        f1.append(f1_score(y_testtl[i], y_pred))

        sp_obj = submodular_pick.SubmodularPick(explainer,
                                                convert_to_lime_format(x_traintl[i], categorical_names).values,
                                                mlp_predict_proba, sample_size=20, num_features=14,
                                                num_exps_desired=5)
        print(sp_obj.explanations[0])
        W_matrix = pd.DataFrame([dict(this.as_list(this.available_labels()[0])) for this in sp_obj.explanations]).fillna(0)
        matrix_mean = W_matrix.mean()

        W_matrix['prediction'] = [this.available_labels()[0] for this in sp_obj.explanations]

        # Save average importance bar plot
        plt.figure(figsize(6.4, 6))
        plt.title("Feature Importance")
        plt.xlabel("Importance")
        plt.ylabel("Features")
        newplot = np.abs(W_matrix.drop("prediction", axis=1)).mean(axis=0).sort_values(ascending=False).head(
            32).sort_values(ascending=True).plot.barh()
        newplot.figure.savefig("herd_no_smote/"+str(i)+"featureimportance2_val.pdf", bbox_inches='tight')
        plt.close()

        # Save grouped feature importance
        grped_coeff = W_matrix.groupby("prediction").mean()
        grped_coeff = grped_coeff.rename(index={0: 'LOCO_SCORE 1,2', 1: 'LOCO_SCORE 3,4,5'})
        pickle.dump(grped_coeff, open("herd_no_smote/"+str(i)+"important_features_grouped_val", 'wb'))

        # Visualize by group
        grped_coeff = grped_coeff.T
        grped_coeff["abs"] = np.abs(grped_coeff.iloc[:, 0])
        grped_coeff.sort_values("abs", inplace=True, ascending=False)
        plt.figure(figsize(15, 15))
        newplot2 = grped_coeff.head(32).sort_values("abs", ascending=True).drop("abs", axis=1).plot.barh()
        newplot2.set_title("Feature Importance")
        newplot2.set_xlabel("Importance")
        newplot2.set_ylabel("Features")
        newplot2.figure.savefig("herd_no_smote/"+str(i)+"featureimportance3_val.pdf", bbox_inches='tight')
        plt.close()

        # Save final global importances
        pickle.dump(matrix_mean, open("herd_no_smote/"+str(i)+"important_features_val", 'wb'))
        plt.figure(figsize(15, 6))
        plt.title("Feature Importance")
        plt.xlabel("Features")
        plt.ylabel("Importance")
        plt.grid(visible=True, which='major', axis='both')
        plot = matrix_mean.sort_values(ascending=False).plot.bar()
        plot.figure.savefig("herd_no_smote/"+str(i)+"featureimportance_val.pdf", bbox_inches='tight')
        plt.close()
        plt.close('all')
        print("hi")
        i = i + 1
