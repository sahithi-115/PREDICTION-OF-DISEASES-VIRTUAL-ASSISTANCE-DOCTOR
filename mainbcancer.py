import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn. metrics import accuracy_score
import sklearn.datasets
import pickle

df=pd.read_csv("bcancer1.csv")
print(df)
print(df.head())
print(df.describe())
print(df["fractal_dimension_worst"].value_counts())
X = df.drop(columns="fractal_dimension_worst", axis=1)
Y=df['fractal_dimension_worst']
print(X,Y)

scaler =StandardScaler()
scaler.fit(X)
standard=scaler.transform(X)
print(standard)

x=standard
y=df["fractal_dimension_worst"]
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

