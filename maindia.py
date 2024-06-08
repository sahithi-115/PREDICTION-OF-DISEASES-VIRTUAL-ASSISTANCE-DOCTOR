import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn. metrics import accuracy_score
import pickle

df=pd.read_csv("diabetes.csv")
print(df.shape)
print(df.head())
print(df.describe())
print(df["Outcome"].value_counts())
X = df.drop(columns="Outcome", axis=1)
print(X.shape)
Y=df['Outcome']
print(X,Y)

scaler =StandardScaler()
scaler.fit(X)
standard=scaler.transform(X)
print(standard)

x=standard
y=df["Outcome"]
print(x,y)
X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.2, stratify=Y, random_state=2)
print(X.shape, X_train.shape, X_test.shape)
classifier=svm.SVC(kernel="linear")
classifier.fit(X_train, Y_train)
X_train_prediction=classifier.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction, Y_train)
print("Accuracy score of the training data:", training_data_accuracy)
X_test_prediction=classifier.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction, Y_test)
print("Accuracy score of the test data:", test_data_accuracy)
'''
i = a.get()
j = b.get()
k = c.get()
l = d.get()
m = e.get()
n = f.get()
o = g.get()
p = h.get()
'''
input_data=(6,148,72,35,0,33.6,0.627,50)
inasnp=np.asarray(input_data)
indere=inasnp.reshape(1,-1)
std_data=scaler.transform(indere)
print(std_data)
prediction=classifier.predict(std_data)
print(prediction)
if prediction[0] == 0:
    print("hello")
else:
    print("done")
