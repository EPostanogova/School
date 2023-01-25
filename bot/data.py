import pandas as pd
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

RAND=0
dataset=pd.read_csv('diabetes_data_upload.csv')
print(dataset.info())

#sns.displot(dataset['Age'])
#plt.show()
dataset['Gender'].replace('Female',0, inplace=True)
dataset['Gender'].replace('Male',1, inplace=True)
dataset['Polyuria'].replace('No',0, inplace=True)
dataset['Polyuria'].replace('Yes',1, inplace=True)
dataset['Polydipsia'].replace('No',0, inplace=True)
dataset['Polydipsia'].replace('Yes',1, inplace=True)
dataset['sudden weight loss'].replace('No',0, inplace=True)
dataset['sudden weight loss'].replace('Yes',1, inplace=True)
dataset['weakness'].replace('No',0, inplace=True)
dataset['weakness'].replace('Yes', 1, inplace=True)
dataset['Polyphagia'].replace('Yes', 1, inplace=True)
dataset['Polyphagia'].replace('No', 0, inplace=True)
dataset['Genital thrush'].replace('Yes', 1, inplace=True)
dataset['Genital thrush'].replace('No', 0, inplace=True)
dataset['visual blurring'].replace('Yes', 1, inplace=True)
dataset['visual blurring'].replace('No', 0, inplace=True)
dataset['Itching'].replace('Yes', 1, inplace=True)
dataset['Itching'].replace('No', 0, inplace=True)
dataset['Irritability'].replace('Yes', 1, inplace=True)
dataset['Irritability'].replace('No', 0, inplace=True)
dataset['delayed healing'].replace('Yes', 1, inplace=True)
dataset['delayed healing'].replace('No', 0, inplace=True)
dataset['partial paresis'].replace('Yes', 1, inplace=True)
dataset['partial paresis'].replace('No', 0, inplace=True)
dataset['muscle stiffness'].replace('Yes', 1, inplace=True)
dataset['muscle stiffness'].replace('No', 0, inplace=True)
dataset['Alopecia'].replace('Yes', 1, inplace=True)
dataset['Alopecia'].replace('No',0, inplace=True)
dataset['Obesity'].replace('No',0, inplace=True)
dataset['Obesity'].replace('Yes',1, inplace=True)

X=dataset.iloc[:,0:16].values
Y=dataset.iloc[:,16].values

X_train,X_test,y_train,y_test=train_test_split(X,Y,random_state=RAND,test_size=0.2)

# model=[]
# model.append(['LR',LogisticRegression(random_state=RAND,solver='liblinear')])
# model.append(['Tree',DecisionTreeClassifier(criterion='entropy',random_state=RAND)])
# model.append(['SVC',SVC(kernel='linear',random_state=RAND)])
# model.append(['Gaus',GaussianNB()])
# model.append(['RF',RandomForestClassifier(n_estimators=100,criterion='entropy',random_state=RAND)])
# model.append(['KN',KNeighborsClassifier(n_neighbors=15,metric='minkowski',p=2)])
#
# results=[]
# names=[]
#
# for name,mod in model:
#     kfold=StratifiedKFold(n_splits=10,random_state=0,shuffle=True)
#     cv_result=cross_val_score(mod,X_train,y_train,cv=kfold,scoring='accuracy')
#     results.append(cv_result)
#     names.append(name)
#     print(name,cv_result.mean(),cv_result.std())
def predict(data_list):
    classifier=RandomForestClassifier(n_estimators=100,criterion='entropy',random_state=RAND)
    classifier.fit(X_train,y_train)
    #y_pred=classifier.predict(X_test)
    y_pred=classifier.predict([data_list])
    return y_pred

#print(confusion_matrix(y_test,y_pred))
#print(accuracy_score(y_test,y_pred))


