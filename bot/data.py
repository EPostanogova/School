import pandas as pd
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt

dataset=pd.read_csv('diabetes_data_upload.csv')
print(dataset.info())

#sns.displot(dataset['Age'])
#plt.show()

dataset.columns=['Age','Gender','','','','','']
dataset['Gender']=dataset.label.map({'Male':0,'Female':1})
print(dataset.head())

