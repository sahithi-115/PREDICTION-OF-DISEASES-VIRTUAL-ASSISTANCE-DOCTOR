from tkinter import messagebox
import pandas as pd
import numpy as np
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn. metrics import accuracy_score
dfb=pd.read_csv("heart.csv")
X = dfb.drop(columns="target", axis=1)
Y=dfb['target']
scaler2 =StandardScaler()
scaler2.fit(X)
standard=scaler2.transform(X)
x2=standard
y2=dfb["target"]
X_train2,X_test2,Y_train2,Y_test2 = train_test_split(x2,y2,test_size=0.2, stratify=Y, random_state=2)
classifier2=svm.SVC(kernel="linear")
classifier2.fit(X_train2, Y_train2)
X_train_prediction=classifier2.predict(X_train2)
training_data_accuracy=accuracy_score(X_train_prediction, Y_train2)
X_test_prediction=classifier2.predict(X_test2)
test_data_accuracy=accuracy_score(X_test_prediction, Y_test2)


'''def bps():
    i = a.get()
    j = b.get()
    k = c.get()
    l = d.get()
    m = e.get()
    n = f.get()
    o = g.get()
    p = h.get()
    # q = ii.get()
    # r = jj.get()'''
input_data = (1,11.28,0.9,34,23,1,0,2,1)
inasnp2 = np.asarray(input_data)
indere2 = inasnp2.reshape(1, -1)
std_data = scaler2.transform(indere2)
prediction2 = classifier2.predict(std_data)
if prediction2[0] == 0:
    print("hello")
else:
    print("done")