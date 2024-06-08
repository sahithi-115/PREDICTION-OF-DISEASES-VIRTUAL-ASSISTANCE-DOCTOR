import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn. metrics import accuracy_score
import pickle

dfh=pd.read_csv("heart.csv")
print(df)
print(df.head())
print(df.describe())
print(df["target"].value_counts())
X = dfh.drop(columns="target", axis=1)
Y=dfh['target']
print(X,Y)

scaler1 =StandardScaler()
scaler1.fit(X)
standard=scaler1.transform(X)
print(standard)

x1=standard
y1=dfh["target"]
print(x,y)
X_train1,X_test1,Y_train1,Y_test1 = train_test_split(x1, y1, test_size=0.2, stratify=Y, random_state=2)
print(X.shape, X_train1.shape, X_test1.shape)
classifier1=svm.SVC(kernel="linear")
classifier1.fit(X_train1, Y_train1)
X_train_prediction=classifier1.predict(X_train1)
training_data_accuracy=accuracy_score(X_train_prediction, Y_train1)
print("Accuracy score of the training data:", training_data_accuracy)
X_test_prediction=classifier1.predict(X_test1)
test_data_accuracy=accuracy_score(X_test_prediction, Y_test1)
print("Accuracy score of the test data:", test_data_accuracy)
input_data1=(6, 148, 72, 35, 0, 33.6, 0.627, 50)
inasnp1=np.asarray(input_data1)
indere1=inasnp1.resize(1, -1)
std_data=scaler1.transform(indere1)
print(std_data)
prediction1=classifier1.predict(std_data)
print(prediction1)
if prediction1[0] == 0:
    print("hello")
else:
    print("done")
