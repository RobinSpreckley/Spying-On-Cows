import pandas as pd
from sklearn.preprocessing import RobustScaler, StandardScaler
from sklearn.neural_network import MLPClassifier
import os
import seaborn as sns
import matplotlib.pyplot as plt

# Reads in cleaned data file.
GROUPC = pd.read_csv(
    "C:/Users/jspre/PycharmProjects/Coursework4thyear/cleanData/group-c.csv")
GROUPC['LCT_CALVING_EASE'].replace(to_replace=['A', 'N', 'FN', 'VN', 'FM', 'VM', 'VC'], value=[1, 2, 3, 4, 5, 6, 7],
                                   inplace=True)
GROUPC['LCT_CALVING_EASE'] = GROUPC.LCT_CALVING_EASE.astype(float)


# Conform upper and lower case to values.
GROUPC['majfeedtype'].replace(
    to_replace=['XB', 'xb', 'DR', 'dr', 'ZZ', 'zz', 'XH', 'xh', 'XM', 'xm', 'HE', 'he', 'XE', 'xe', 'ST', 'st', 'NT',
                'nt'],
    value=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9], inplace=True)

GROUPC['majfeedtype'] = GROUPC.majfeedtype.astype(float)


# GROUPC['COND_SCORE'].replace(to_replace=[0.5,0.75,1,1.25,1.5,1.75,2,2.25,2.5,2.75,3,3.25,3.5,3.75,4,4.25],
#                              value=[1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3,3, 3, 3], inplace=True)

# IDK



# Datacleaning

GROUPC['LOCO_SCORE'].replace(to_replace=[1, 2, 3, 4, 5],
                             value=[1, 1, 2, 2, 2], inplace=True)

#Removing Redundant/Repeated Data

GROUPC['LCT_RECORDER_TYPE'].replace(to_replace=['CA', 'CU'], value=[1, 2], inplace=True)
GROUPC.drop('DAM_GENETIC_GROUP', 1, inplace=True)
GROUPC.drop('WEIGHT_DATE', 1, inplace=True)
GROUPC.drop('LCT_DRYING_DATE', 1, inplace=True)
GROUPC.drop('LCT_LACT_START_DATE', 1, inplace=True)
GROUPC.drop('LCT_CALVING_DATE', 1, inplace=True)
GROUPC.drop('FEEDTYPE', 1, inplace=True)
GROUPC.drop('LCT_DOB', 1, inplace=True)
GROUPC.drop('BCS_IDENT', 1, inplace=True)

GROUPC = GROUPC[GROUPC.columns.drop(list(GROUPC.filter(regex='Group_Concat')))]
GROUPC = GROUPC[GROUPC.columns.drop(list(GROUPC.filter(regex='group_concat')))]

grouped = GROUPC.groupby(GROUPC.EAR_TAG)


#Get Individual Cow Data

DF_list = []
for group in grouped.groups:
    loopframe = grouped.get_group(group)
    loopframe.drop('birth_wgt', 1, inplace=True)
    loopframe.drop('DAM_HOLSTEIN_PERC', 1, inplace=True)
    loopframe.drop('DAM_NO_OF_LACTS', 1, inplace=True)
    loopframe.drop('cnt', 1, inplace=True)
    loopframe = loopframe[loopframe.columns.drop(list(loopframe.filter(regex='DAM')))]
    DF_list.append(loopframe)

Y_col = 'LOCO_SCORE'
classifier = MLPClassifier(max_iter=2000)
scaler = StandardScaler()
cows = {}





corrmatrix = GROUPC.corr()
plt.figure(figsize=(60, 40))
snscorr = sns.heatmap(corrmatrix, annot=True)
plt.title("Correlation matrix of LangHill Herd data")

plt.xlabel("features")

plt.ylabel("features")

figure = snscorr.get_figure()
figure.tight_layout()
figure.savefig("correlation.pdf")

'''

for frame in DF_list:
    id = frame.EAR_TAG.array[0]
    try:
        if not os.path.exists(str(id) + "\smote-no-basic-noyear"):

            os.makedirs(str(id) + "\smote-no-basic-noyear")


    except:
        print("skip")
  '''


'''
    with open(str(id)+'\\smote-no\\f1-score', 'rb') as f:


    id = frame.EAR_TAG.array[0]
    frame.drop('EAR_TAG', 1, inplace=True)
    corrmatrix =frame.corr()
    plt.figure(figsize= (60,40))
    snscorr = sns.heatmap(corrmatrix, annot=True)
    plt.title("Correlation matrix of LangHill Herd data")

    plt.xlabel("features")

    plt.ylabel("features")
    

    figure = snscorr.get_figure()
    figure.tight_layout()
    figure.savefig(str(id)+"/correlation.png")
'''


#    figure = snscorr.get_figure()
 #   figure.savefig(str(id)+"/correlation.png")

#pairpliot
'''
    plt.figure(figsize= (50,40))
    snscorrmult = sns.pairplot(frame, hue=Y_col)
    plt.title("LOCO SCORE LangHill Herd data")
    plt.xlabel("features")
    plt.ylabel("features")
    figure2 = snscorrmult.get_figure()
    figure2.savefig(str(id)+"/pairplot.png")
'''