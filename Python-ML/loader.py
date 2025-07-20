import pickle
from collections import Counter
import numpy as numpy
import seaborn as sns
import pandas as pd
import numpy as np
import os

from IPython.core.pylabtools import figsize
from wordcloud import WordCloud
import matplotlib.pyplot as plt

GROUPC = pd.read_csv(
    "C:/Users/jspre/PycharmProjects/Coursework4thyear/cleanData/group-c.csv")
grouped = GROUPC.groupby(GROUPC.EAR_TAG)
DF_list = []
for group in grouped.groups:
    loopframe = grouped.get_group(group)
    DF_list.append(loopframe)

listlr = list()
listf1 = list()
listf2 = list()
listacc = list()
listacc2 = list()
listacc3 = list()
a_list1 = list()
a_list5 = list()
a_list1_all = list()
a_list5_all = list()
a_list1_herd = list()
a_list5_herd = list()
idlist = list()
path = 'smote-yes'
path2 = 'smote-no'
path3= 'smote-no-basic'
lr3 = np.zeros((2, 2))
for frame in DF_list:
    id = frame.EAR_TAG.array[0]
    if os.path.exists(str(id) + '\\' + path + '\\confusion_matrix'):
        id = frame.EAR_TAG.array[0]
        idlist.append(id)
        with open(str(id) + '\\' + path + '\\f1-score', 'rb') as f:
            lr1 = pickle.load(f)
            listlr.append(lr1)
        with open(str(id) + '\\' + path2 + '\\f1-score', 'rb') as f:
            lr = pickle.load(f)
            listf1.append(lr)
        with open(str(id) + '\\' + path3 + '\\prc-score', 'rb') as f:
            lr = pickle.load(f)
            listf2.append(lr)


        with open(str(id) + '\\' + path + '\\acc-score', 'rb') as f:
            acc1 = pickle.load(f)
            listacc.append(acc1)
        with open(str(id) + '\\' + path2 + '\\acc-score', 'rb') as f:
            acc = pickle.load(f)
            listacc2.append(acc)
        with open(str(id) + '\\' + path3 + '\\rec-score', 'rb') as f:
            acc = pickle.load(f)
            listacc3.append(acc)



        with open(str(id) + '\\' + path + '\\confusion_matrix', 'rb') as f:
            lr2 = pickle.load(f)
            lr3 = lr3 + lr2
            idlist.append(id)
            # print(id)
            # print(sum(sum(lr2)))
            # print(sum(sum(lr3)))
        with open(str(id) + '\\' + path + '\\important_features_grouped', 'rb') as f:
            lr4 = pickle.load(f)
            limit =  False
            if limit == True:
                grped_coeff = lr4
                grped_coeff = grped_coeff.T
                if 'LOCO_SCORE 1,2' in grped_coeff.columns and 'LOCO_SCORE 3,4,5' in grped_coeff.columns:
                    grped_coeff["abs"] = np.abs(grped_coeff.iloc[:, 0]) + np.abs(grped_coeff.iloc[:, 1])
                    grped_coeff.sort_values("abs", inplace=True, ascending=False)
                    plt.figure(figsize(6.4, 6))

                    newplot2 = grped_coeff.head(32).sort_values("abs", ascending=True).drop("abs", axis=1).plot.barh()
                    newplot2.set_title("Feature Importance")
                    newplot2.set_xlabel("Importance")
                    newplot2.set_ylabel("Features")
                    newplot2.figure.savefig(str(id) + '\\' + path + '\\featureimportance3.pdf', bbox_inches='tight')
                    plt.close()
            lr5 = lr4.T
            if lr1 > 0.7 and acc1 > 0.7:
                if 'LOCO_SCORE 1,2' in lr5.columns:
                    loco_1 = lr5[lr5['LOCO_SCORE 1,2'] > 0]
                    a_list1.append(loco_1.axes[0])
                if 'LOCO_SCORE 3,4,5' in lr5.columns:
                    loco_5 = lr5[lr5['LOCO_SCORE 3,4,5'] > 0]
                    a_list5.append(loco_5.axes[0])

            if 'LOCO_SCORE 1,2' in lr5.columns:
                loco_1_all = lr5[lr5['LOCO_SCORE 1,2'] > 0]
                a_list1_all.append(loco_1_all.axes[0])
            if 'LOCO_SCORE 3,4,5' in lr5.columns:
                loco_5_all = lr5[lr5['LOCO_SCORE 3,4,5'] > 0]
                a_list5_all.append(loco_5_all.axes[0])

print(numpy.median(listf2))
print(numpy.median(listacc3))
def Average(lst):
    return sum(lst) / len(lst)


listlr = numpy.array(listlr)
listf1 = numpy.array(listf1)
listf2 = numpy.array(listf2)
listacc = numpy.array(listacc)
listacc2 = numpy.array(listacc2)
listacc3 = numpy.array(listacc3)
i=0
while i < 154:
    with open("herd_yes_smote2/"+str(i)+"important_features_grouped_val", 'rb') as f:
        lr4 = pickle.load(f)
        print(lr4.columns.values)
        lr5 = lr4.T

        if 'LOCO_SCORE 1,2' in lr5.columns:
            loco_1_herd = lr5[lr5['LOCO_SCORE 1,2'] > 0]
            a_list1_herd.append(loco_1_herd.axes[0])
        if 'LOCO_SCORE 3,4,5' in lr5.columns:
            loco_5_all = lr5[lr5['LOCO_SCORE 3,4,5'] > 0]
            a_list5_herd.append(loco_5_all.axes[0])
        i=i+1



flat_listhelathy = [item for sublist in a_list1 for item in sublist]
flat_listlame = [item for sublist in a_list5 for item in sublist]
flat_listhelathy_all = [item for sublist in a_list1_all for item in sublist]
flat_listlame_all = [item for sublist in a_list5_all for item in sublist]
a_list1_herd_t = [item for sublist in a_list1_herd for item in sublist]
a_list5_herd_t = [item for sublist in a_list5_herd for item in sublist]
print(a_list1_herd_t)

newlisth = list()
newlistl = list()
newlisth_all = list()
newlistl_all = list()
newlisth_herd = list()
newlistl_herd = list()
for word in flat_listhelathy:
    ##print(word)
    word = word.replace("(0IF(", "")

    newlisth.append(word.split(" "))

for word in flat_listlame:
    word = word.replace("(0IF(", "")

    newlistl.append(word.split(" "))

for word in flat_listhelathy_all:
    # print(word)
    word = word.replace("(0IF(", "")

    newlisth_all.append(word.split(" "))

for word in flat_listlame_all:
    word = word.replace("(0IF(", "")

    newlistl_all.append(word.split(" "))

for word in a_list1_herd_t:
    # print(word)
    word = word.replace("(0IF(", "")

    newlisth_herd.append(word.split(" "))

for word in a_list5_herd_t:
    word = word.replace("(0IF(", "")

    newlistl_herd.append(word.split(" "))

# print(id)
# print(idlist.__sizeof__())
pickle.dump(idlist, open("idlist", 'wb'))

# print(Counter(flat_list))
print(newlisth_herd)
helthy = [item for sublist in newlisth for item in sublist]
lame = [item for sublist in newlistl for item in sublist]
helthy_all = [item for sublist in newlisth_all for item in sublist]
lame_all = [item for sublist in newlistl_all for item in sublist]
healthy_herd = [item for sublist in newlisth_herd for item in sublist]
lame_herd = [item for sublist in newlistl_herd for item in sublist]



dthealthy = Counter(helthy)
dtlame = Counter(lame)
dthealthy_all = Counter(helthy_all)
dtlame_all = Counter(lame_all)
healthy_herdcount= Counter(healthy_herd)
lame_herdcount = Counter(lame_herd)

removewords = ('<=', '>', '<', '0.00', ',0))',"7.00","0.25","2.90","YIELD_2","STDCELLCOUNT","AVGFATPERC","STDYIELD","AVGPROTEINPERC","STDPROTEINPERC",
               "AVGYIELD","AVGCELLCOUNT","162.80","1101.00","2.00","FAT_PERCENTAGE_3","1999.00","CELL_COUNT_1","PROTEIN_PERCENTAGE_2","YIELD_1",
               'FAT_PERCENTAGE_1','3631.00','CELL_COUNT_2','STDFATPERC','PROTEIN_PERCENTAGE_1','1664.00','270.89','CELL_COUNT_3',
               'YIELD_3','FAT_PERCENTAGE_2','PROTEIN_PERCENTAGE_3','1119.00','3.83','16.77','497.27','497.26','137.71','15/10/2013','19/01/2016',
               '10/07/2012','10/06/2014','03/01/2012','21/05/2013','22/07/2014','13/12/2016','03/11/2016','07/10/2014','21/11/2013','18/09/2012',
               '25/01/2017')##the attributes removed are from milk comp they are over represented because they barly show up in the data, i would of remved them but testing took too long and dont what to change all the attributes between tests

for x in removewords:
    if x in dthealthy:
        print("hi")
        print(x)
        del dthealthy[x]
for x in removewords:
    if x in dtlame:
        del dtlame[x]
for x in removewords:
    if x in dthealthy_all:
        del dthealthy_all[x]
for x in removewords:
    if x in dtlame_all:
        del dtlame_all[x]
for x in removewords:
    if x in healthy_herdcount:
        del healthy_herdcount[x]
for x in removewords:
    if x in lame_herdcount:
        del lame_herdcount[x]

        with open('herd_no_smote/acc-score_val', 'rb') as f:
            accnoherd = pickle.load(f)
        with open('herd_no_smote/f1-score_val', 'rb') as f:
            f1noherd = pickle.load(f)
        with open('herd_yes_smote/acc-score', 'rb') as f:
            accyesherd = pickle.load(f)
        with open('herd_yes_smote/f1-score', 'rb') as f:
            f1yesherd = pickle.load(f)





# Creating plot''
#box_dict = {'Smote-cows-acc':listacc,'Cows-acc':listacc2,
#            'basic-cows-acc':listacc3,}
###box_dict = {'Smote-NO-Cows-f1': listf1,'Smote-YES-Cows-f1': listlr, 'Basic-Cows-f1': listf2, 'Smote-cows-acc':listacc,'Cows-acc':listacc2,
#            'basic-cows-acc':listacc3}
#box_dict = {'herd-acc':accnoherd,'smote-herd-acc':accyesherd,'herd-f1':f1noherd,'smote-herd-f1':f1yesherd}

with open("herd_no_smote/rec-score_val_list", 'rb') as f:
    recall = pickle.load(f)
with open("herd_no_smote/prc-score_val_list", 'rb') as f:
    prc = pickle.load(f)
with open("herd_no_smote/acc-score_val_list", 'rb') as f:
    acclist = pickle.load(f)
with open("herd_no_smote/f1-score_val_list", 'rb') as f:
    f1 = pickle.load(f)

print("herd_no_smote")
print(numpy.median(recall))
print(numpy.median(prc))
print(numpy.median(acclist))
print(numpy.median(f1))



box_dict = {'Smote-Yes-Cows-recall': listlr, 'Smote-No-Cows-recall': listf1,'Basic-Cows-recall': listf2, 'Smote-Yes-cows-precision':listacc,'Smote-No-Cows-precision':listacc2, 'basic-cows-precision':listacc3}

fig = plt.figure(figsize=(30, 30))
fig, ax = plt.subplots(figsize=(15, 10))

ax.boxplot(box_dict.values(),notch=True)
ax.set_xticklabels(box_dict.keys())

plt.savefig(path + "boxplot",bbox_inches='tight')
plt.close()

box_dict = {'Recall': recall, 'Precision':prc,'Accuracy':acclist, 'F1-Score':f1}
fig = plt.figure(figsize=(30, 30))
fig, ax = plt.subplots(figsize=(15, 10))
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

ax.boxplot(box_dict.values(),notch=True)
ax.set_xticklabels(box_dict.keys())

plt.savefig(path + "boxplotherd",bbox_inches='tight')
plt.close()





with open("arecall-smote-cows", 'rb') as f:
    recall = pickle.load(f)
with open("aprec-smote-cows", 'rb') as f:
    prc = pickle.load(f)
with open("acc-smote-cows", 'rb') as f:
    acclist = pickle.load(f)
with open("af1-smote-cows", 'rb') as f:
    f1 = pickle.load(f)




box_dict = {'Recall': recall, 'Precision':prc,'Accuracy':acclist, 'F1-Score':f1}

print("cowssmote")
print(numpy.median(recall))
print(numpy.median(prc))
print(numpy.median(acclist))
print(numpy.median(f1))
fig = plt.figure(figsize=(30, 30))
fig, ax = plt.subplots(figsize=(15, 10))
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
ax.boxplot(box_dict.values(),notch=True)
ax.set_xticklabels(box_dict.keys())

plt.savefig(path + "nosmotecows",bbox_inches='tight')
plt.close()



with open("herd_yes_smote2/rec-score_val_list", 'rb') as f:
    recall = pickle.load(f)
with open("herd_yes_smote2/prc-score_val_list", 'rb') as f:
    prc = pickle.load(f)
    print(prc)
with open("herd_yes_smote2/acc-score_val_list", 'rb') as f:
    acclist = pickle.load(f)
with open("herd_yes_smote2/f1-score_val_list", 'rb') as f:
    f1 = pickle.load(f)
print("herd_yes_smote")
print(numpy.median(recall))
print(numpy.median(prc))
print(numpy.median(acclist))
print(numpy.median(f1))


box_dict = {'Recall': recall, 'Precision':prc,'Accuracy':acclist, 'F1-Score':f1}
fig = plt.figure(figsize=(30, 30))
fig, ax = plt.subplots(figsize=(15, 10))
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)




ax.boxplot(box_dict.values(),notch=True)
ax.set_xticklabels(box_dict.keys())

plt.savefig(path + "herdyessmote",bbox_inches='tight')
plt.close()









wc = WordCloud(
    background_color='white',
    stopwords='',
    max_words=35,
    relative_scaling= 0.5,
    colormap='Dark2',
    collocation_threshold=3

)
print(dthealthy)
wc.generate_from_frequencies(dthealthy)
wc.to_file(path + "-healthycloud.png")

wc.generate_from_frequencies(dtlame)
wc.to_file(path + "-lamecloud.png")
print(dtlame)
wc.generate_from_frequencies(dthealthy_all)
wc.to_file(path + "-healthycloud-all.png")
print(dthealthy_all)
wc.generate_from_frequencies(dtlame_all)
wc.to_file(path + "-lamecloud-all.png")

wc.generate_from_frequencies(healthy_herdcount)
wc.to_file("heath-herd-all-val.png")
print(healthy_herdcount)
wc.generate_from_frequencies(lame_herdcount)
print(lame_herdcount)
wc.to_file("lame-herd-all-val.png")



group_names = ['TrueNeg', 'FalsePos', 'FalseNeg', 'TruePos']
group_counts = ['{0:0.0f}'.format(value) for value in lr3.flatten()]
group_percentages = ['{0:.2%}'.format(value) for value in
                     lr3.flatten() / np.sum(lr3)]
labels = [f"{v1}\n{v2}\n{v3}" for v1, v2, v3 in zip(group_names, group_counts, group_percentages)]
labels = np.asarray(labels).reshape(2, 2)
plt.close()
cnf_matrix = sns.heatmap(lr3, annot=labels, fmt='', cmap='Blues')
cnf_matrix.get_figure().savefig('confusion_matrix_' + path + '.png')
