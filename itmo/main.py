import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVR

test=pd.read_csv("test.csv",index_col=0)
train=pd.read_csv("train.csv",index_col=0)

#obj_df = train.select_dtypes(include=['object']).copy()
obj_df = train.copy()
obj_df1 = test.copy()

#print(train['target'].unique())

from sklearn.preprocessing import OrdinalEncoder

ord_enc = OrdinalEncoder()
obj_df["f2"] = ord_enc.fit_transform(obj_df[["f2"]])
obj_df["f8"] = ord_enc.fit_transform(obj_df[["f8"]])
obj_df["f10"] = ord_enc.fit_transform(obj_df[["f10"]])
obj_df["f12"] = ord_enc.fit_transform(obj_df[["f12"]])
obj_df["f20"] = ord_enc.fit_transform(obj_df[["f20"]])
obj_df["f21"] = ord_enc.fit_transform(obj_df[["f21"]])
obj_df["f22"] = ord_enc.fit_transform(obj_df[["f22"]])
obj_df["f24"] = ord_enc.fit_transform(obj_df[["f24"]])
obj_df["f26"] = ord_enc.fit_transform(obj_df[["f26"]])
obj_df["f27"] = ord_enc.fit_transform(obj_df[["f27"]])
obj_df["f34"] = ord_enc.fit_transform(obj_df[["f34"]])
obj_df["f36"] = ord_enc.fit_transform(obj_df[["f36"]])
obj_df["f41"] = ord_enc.fit_transform(obj_df[["f41"]])
obj_df["f42"] = ord_enc.fit_transform(obj_df[["f42"]])
obj_df["f43"] = ord_enc.fit_transform(obj_df[["f43"]])
obj_df["f46"] = ord_enc.fit_transform(obj_df[["f46"]])
obj_df["f47"] = ord_enc.fit_transform(obj_df[["f47"]])
obj_df["f64"] = ord_enc.fit_transform(obj_df[["f64"]])
obj_df["f69"] = ord_enc.fit_transform(obj_df[["f69"]])
obj_df["f70"] = ord_enc.fit_transform(obj_df[["f70"]])


obj_df=obj_df.fillna(obj_df.mean())


obj_df1["f2"] = ord_enc.fit_transform(obj_df1[["f2"]])
obj_df1["f8"] = ord_enc.fit_transform(obj_df1[["f8"]])
obj_df1["f10"] = ord_enc.fit_transform(obj_df1[["f10"]])
obj_df1["f12"] = ord_enc.fit_transform(obj_df1[["f12"]])
obj_df1["f20"] = ord_enc.fit_transform(obj_df1[["f20"]])
obj_df1["f21"] = ord_enc.fit_transform(obj_df1[["f21"]])
obj_df1["f22"] = ord_enc.fit_transform(obj_df1[["f22"]])
obj_df1["f24"] = ord_enc.fit_transform(obj_df1[["f24"]])
obj_df1["f26"] = ord_enc.fit_transform(obj_df1[["f26"]])
obj_df1["f27"] = ord_enc.fit_transform(obj_df1[["f27"]])
obj_df1["f34"] = ord_enc.fit_transform(obj_df1[["f34"]])
obj_df1["f36"] = ord_enc.fit_transform(obj_df1[["f36"]])
obj_df1["f41"] = ord_enc.fit_transform(obj_df1[["f41"]])
obj_df1["f42"] = ord_enc.fit_transform(obj_df1[["f42"]])
obj_df1["f43"] = ord_enc.fit_transform(obj_df1[["f43"]])
obj_df1["f46"] = ord_enc.fit_transform(obj_df1[["f46"]])
obj_df1["f47"] = ord_enc.fit_transform(obj_df1[["f47"]])
obj_df1["f64"] = ord_enc.fit_transform(obj_df1[["f64"]])
obj_df1["f69"] = ord_enc.fit_transform(obj_df1[["f69"]])
obj_df1["f70"] = ord_enc.fit_transform(obj_df1[["f70"]])



obj_df1=obj_df1.fillna(obj_df1.mean())

# data=train.drop(['f2'], axis=1)
# data=data.drop(['f69'], axis=1)
# data=data.drop(['f70'], axis=1)
# data=data.drop(['f8'], axis=1)
# data=data.drop(['f10'], axis=1)
# data=data.drop(['f12'], axis=1)
# data=data.drop(['f21'], axis=1)
# data=data.drop(['f20'], axis=1)
# data=data.drop(['f22'], axis=1)
# data=data.drop(['f24'], axis=1)
# data=data.drop(['f26'], axis=1)
# data=data.drop(['f27'], axis=1)
# data=data.drop(['f36'], axis=1)
# data=data.drop(['f34'], axis=1)
# data=data.drop(['f41'], axis=1)
# data=data.drop(['f42'], axis=1)
# data=data.drop(['f43'], axis=1)
# data=data.drop(['f47'], axis=1)
# data=data.drop(['f46'], axis=1)
# data=data.drop(['f64'], axis=1)



#le.fit(["A", "B", "C", "D","E", "F", "G", "H","I", "J", "K", "L","M", "N", "O", "P","Q", "R", "S", "T","U", "V", "W", "X","Y", "Z"])

# X = obj_df.iloc[:,1:70].values
# y = obj_df.iloc[:,70].values
X=obj_df.drop(['target'], axis=1)
y=obj_df['target']


#X['f69','f70','f8','f10','f21','f20','f22','f24','f26','f27','f36','f34','f41','f42','f43','f47','f46','f64'] = labelEncoder_gender.fit_transform(X['f69','f70','f8','f10','f21','f20','f22','f24','f26','f27','f36','f34','f41','f42','f43','f47','f46','f64'])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=101)

model = RandomForestRegressor(n_estimators=100, max_features ='sqrt')
#model = LinearRegression()
#model = SVR(kernel='linear') # метод опорных векторов с линейным ядром

# fitting the model
model.fit(X_train, y_train)

# making predictions
predictions = model.predict(X_test)

df = pd.DataFrame(predictions)

print(df)
# displaying the DataFrame
#print('DataFrame:\n', df)
# saving the DataFrame as a CSV file
gfg_csv_data = df.to_csv('otvet1.csv', header=False,index= False)
#print('\nCSV String:\n', gfg_csv_data)




# model evaluation
print('mean_squared_error : ', mean_squared_error(y_test, predictions))
print('r2 : ',  r2_score(y_test, predictions))