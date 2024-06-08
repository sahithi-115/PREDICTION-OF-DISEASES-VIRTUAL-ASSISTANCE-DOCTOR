from tkinter import *
#from PIL import ImageTk, Image
from tkinter import messagebox
import pandas as pd
import numpy as np
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn. metrics import accuracy_score
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#diadeaties
df=pd.read_csv("diabetes.csv")
X = df.drop(columns="Outcome", axis=1)
Y=df['Outcome']
scaler =StandardScaler()
scaler.fit(X)
standard=scaler.transform(X)
x=standard
y=df["Outcome"]
X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.2, stratify=Y, random_state=2)
classifier=svm.SVC(kernel="linear")
classifier.fit(X_train, Y_train)
X_train_prediction=classifier.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction, Y_train)
X_test_prediction=classifier.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction, Y_test)
def aidia():
    ai = Toplevel()

    def send():
        send = "You => " + e.get()
        txt.insert(END, "\n" + send)
        if (e.get() == "hello"):
            txt.insert(END, "\n" + "Doc => Hi there ,I'am your vitual doctor")
        elif (e.get() == "i have doubts on sugar"):
            txt.insert(END, "\n" + "Doc => how can i help you")
        elif (e.get() == "i have sugar"):
            txt.insert(END,
                       "\n" + "here are some suggestions:" + "\n" + "1.daily do yoga." + "\n" + "2.use medicenes regularly(glycomate.)")
        elif (e.get() == "i dont have sugar"):
            txt.insert(END,
                       "\n" + "Doc => Here are some precautions:" + "\n" + "1.Are you having genetic sugar?" + "\n" + "2.do exersise regularly.")

        else:
            txt.insert(END, "\n" + "Doc => Sorry I didnt get it")
        e.delete(0, END)

    txt = Text(ai, bg="slategrey", fg="lightcoral")
    txt.grid(row=0, column=0, columnspan=2)
    ai.config(bg="lightsteelblue")
    ai.title("Diabeties chat bot")
    e = Entry(ai, width=100, bg="whitesmoke", fg="salmon")
    send = Button(ai, text="send", command=send).grid(row=1, column=1)
    e.grid(row=1, column=0)
    ai.title("CHATBOT")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#heart
dfh=pd.read_csv("heart.csv")
X = dfh.drop(columns="target", axis=1)
Y=dfh['target']
scaler1 =StandardScaler()
scaler1.fit(X)
standard=scaler1.transform(X)
x1=standard
y1=dfh["target"]
X_train1,X_test1,Y_train1,Y_test1 = train_test_split(x1, y1, test_size=0.2, stratify=Y, random_state=2)
classifier1=svm.SVC(kernel="linear")
classifier1.fit(X_train1, Y_train1)
X_train_prediction=classifier1.predict(X_train1)
training_data_accuracy=accuracy_score(X_train_prediction, Y_train1)
X_test_prediction=classifier1.predict(X_test1)
test_data_accuracy=accuracy_score(X_test_prediction, Y_test1)
def heartai():
    ai = Toplevel()

    def send():
        send = "You => " + e.get()
        txt.insert(END, "\n" + send)
        if (e.get() == "hello"):
            txt.insert(END, "\n" + "Doc => Hi there ,I'am your vitual doctor")
        elif (e.get() == "i have doubts on heart issues"):
            txt.insert(END, "\n" + "Doc => are you having ribcage/left chest pain")
        elif (e.get() == "yes"):
            txt.insert(END,
                       "\n" + "here are some suggestions:" + "\n" + "1.use (aspirin) tablet." + "\n" + "2.Immediately consult a doctor.)")
        elif (e.get() == "no"):
            txt.insert(END,
                       "\n" + "Doc => you are safe,Here are some precautions:" + "\n" + "1.Avoid smoking & Drinking" + "\n" + "2.Dont take more stress.")

        else:
            txt.insert(END, "\n" + "Doc => Sorry I didnt get it")
        e.delete(0, END)

    txt = Text(ai)
    txt.grid(row=0, column=0, columnspan=2)
    e = Entry(ai, width=100)
    send = Button(ai, text="send", command=send).grid(row=1, column=1)
    e.grid(row=1, column=0)
    ai.title("CHATBOT")


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def changeOnHover(button, color1,color2):
    button.bind("<Enter>", func=lambda e: button.config(background=color1))
    button.bind("<Leave>", func=lambda e: button.config(background=color2))
health=Tk()
health.title("health")
health.geometry("500x500")
health.config(bg="lightskyblue")
def Diabeties():
    shekar=messagebox.askquestion("hello", "Are you sure")
    if shekar=="yes":
        dia = Toplevel(health)
        dia.title("Diadieties")
        dia.geometry("600x600")
        dia.config(bg="gainsboro")
        def sugar():
            i = a.get()
            j = b.get()
            k = c.get()
            l = d.get()
            m = e.get()
            n = f.get()
            o = g.get()
            p = h.get()
            input_data = (6, 148, 72, 35, 0, 33.6, 0.627, 50)
            inasnp = np.asarray(input_data)
            indere = inasnp.reshape(1, -1)
            std_data = scaler.transform(indere)
            prediction1 = classifier.predict(std_data)
            if prediction1[0] == 0:
                messagebox.showinfo("Report", "You are not Having Diabeties")
            else:
                messagebox.showinfo("Report", "You are  Having Diabeties"+"\n"+"If you want You can contact the Virtual Doctor")

        Label(dia, text="Pregnancies", font=("arial", 20), bg="gainsboro", fg="mintcream").place(x=8, y=50)
        a = Entry(dia, bg="gainsboro", fg="indianred", borderwidth=3, width=18)
        a.place(x=160, y=55)
        Label(dia, text="Glucose", font=("arial", 20), bg="gainsboro", fg="mintcream").place(x=320, y=45)
        b = Entry(dia, bg="gainsboro", fg="indianred", borderwidth=3, width=18)
        b.place(x=430, y=50)
        Label(dia, text="BP", font=("arial", 20), bg="gainsboro", fg="mintcream").place(x=30, y=150)
        c = Entry(dia, bg="gainsboro", fg="indianred", borderwidth=3, width=18)
        c.place(x=160, y=150)
        Label(dia, text="St.ness", font=("arial", 20), bg="gainsboro", fg="mintcream").place(x=330, y=148)
        d = Entry(dia, bg="gainsboro", fg="indianred", borderwidth=3, width=18)
        d.place(x=430, y=152)
        Label(dia, text="Insulin", font=("arial", 20), bg="gainsboro", fg="mintcream").place(x=30, y=240)
        e = Entry(dia, bg="gainsboro", fg="indianred", borderwidth=3, width=18)
        e.place(x=160, y=243)
        Label(dia, text="BMI", font=("arial", 20), bg="gainsboro", fg="mintcream").place(x=320, y=245)
        f = Entry(dia, bg="gainsboro", fg="indianred", borderwidth=3, width=18)
        f.place(x=430, y=245)
        Label(dia, text="DPF", font=("arial", 20), bg="gainsboro", fg="mintcream").place(x=30, y=335)
        g = Entry(dia, bg="gainsboro", fg="indianred", borderwidth=3, width=18)
        g.place(x=160, y=335)
        Label(dia, text="Age", font=("arial", 20), bg="gainsboro", fg="mintcream").place(x=320, y=335)
        h = Entry(dia, bg="gainsboro", fg="indianred", borderwidth=3, width=18)
        h.place(x=430, y=338)
        Button(dia, text="submit", font=("arial", 15), bg="red", fg="Gold", borderwidth=3, width=15,
               command=sugar).place(x=200, y=400)
        Button(dia, text="AI", font=("arial", 15), bg="green", fg="Gold", borderwidth=3, width=15, command=heartai,
               ).place(x=400, y=550)
    else:
        messagebox.showinfo("hello","please select your option")
def Heart():
    shekar=messagebox.askquestion("hello", "Are you sure")
    if shekar=="yes":
        heart = Toplevel()
        heart.title("Heart")
        heart.geometry("600x600")
        heart.config(bg="seashell")
        def attack():
            i = a.get()
            j = b.get()
            k = c.get()
            l = d.get()
            m = e.get()
            n = f.get()
            o = g.get()
            p = h.get()
            q = ii.get()
            r = jj.get()
            input_data1 = (63,1,3,145,233,1,0,150,0,2.3,0,0,1)
            inasnp1 = np.asarray(input_data1)
            indere1 = inasnp1.reshape(1, -1)
            std_data = scaler1.transform(indere1)
            prediction1 = classifier1.predict(std_data)
            if prediction1[0] == 0:
                messagebox.showinfo("Report", "You are Safe"+"\n"+"You are not Having Diabeties")
            else:
                messagebox.showinfo("Report", "You are  Having Heart Disease" + "\n" + "If you want you can contact the Virtual Doctor"+"\n"+"Please contact")

        Label(heart, text="Age", font=("arial", 20), bg="seashell", fg="orchid").place(x=50, y=50)
        a=Entry(heart, bg="seashell", fg="indianred", borderwidth=3, width=18)
        a.place(x=130, y=55)
        Label(heart, text="Gender", font=("arial", 20), bg="seashell", fg="orchid").place(x=280, y=45)
        b=Entry(heart, bg="seashell", fg="indianred", borderwidth=3, width=18)
        b.place(x=420, y=50)
        Label(heart, text="CP", font=("arial", 20), bg="seashell", fg="orchid").place(x=50, y=150)
        c=Entry(heart, bg="seashell", fg="indianred", borderwidth=3, width=18)
        c.place(x=130, y=150)
        Label(heart, text="Trestbps", font=("arial", 20), bg="seashell", fg="orchid").place(x=270, y=148)
        d=Entry(heart, bg="seashell", fg="indianred", borderwidth=3, width=18)
        d.place(x=420, y=150)
        Label(heart, text="Chol", font=("arial", 20), bg="seashell", fg="orchid").place(x=50, y=240)
        e=Entry(heart, bg="seashell", fg="indianred", borderwidth=3, width=18)
        e.place(x=130, y=243)
        Label(heart, text="FBS", font=("arial", 20), bg="seashell", fg="orchid").place(x=280, y=245)
        f=Entry(heart, bg="seashell", fg="indianred", borderwidth=3, width=18)
        f.place(x=420, y=245)
        Label(heart, text="Restecg", font=("arial", 20), bg="seashell", fg="orchid").place(x=20, y=335)
        g=Entry(heart, bg="seashell", fg="indianred", borderwidth=3, width=18)
        g.place(x=130, y=335)
        # Entry(heart,  bg="seashell", fg="Gold", borderwidth=3, width=18).place(x=130, y=335)
        Label(heart, text="Exang", font=("arial", 20), bg="seashell", fg="orchid").place(x=280, y=340)
        h=Entry(heart, bg="seashell", fg="indianred", borderwidth=3, width=18)
        h.place(x=130, y=335)
        Label(heart, text="Slope", font=("arial", 20), bg="seashell", fg="orchid").place(x=280, y=335)
        ii=Entry(heart, bg="seashell", fg="indianred", borderwidth=3, width=18)
        ii.place(x=130, y=335)
        Label(heart, text="thal", font=("arial", 20), bg="seashell", fg="orchid").place(x=280, y=335)
        jj=Entry(heart, bg="seashell", fg="indianred", borderwidth=3, width=18)
        jj.place(x=420, y=335)

        Button(heart, text="submit", font=("arial", 15), bg="seashell", fg="Gold", borderwidth=3, width=15,command=attack).place(x=180,
                                                                                                                  y=400)
        Button(heart, text="AI", font=("arial", 15), bg="green", fg="Gold", borderwidth=3, width=15,command=heartai
               ).place(x=400, y=550)

    else:
        messagebox.showinfo("hello","please select your option")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Blood Plessure
dfp=pd.read_csv("heart.csv")
X = dfp.drop(columns="target", axis=1)
Y=dfp['target']
scaler2 =StandardScaler()
scaler2.fit(X)
standard=scaler2.transform(X)
x2=standard
y2=dfh["target"]
X_train2,X_test2,Y_train2,Y_test2 = train_test_split(x2, y2, test_size=0.2, stratify=Y, random_state=2)
classifier2=svm.SVC(kernel="linear")
classifier2.fit(X_train2, Y_train2)
X_train_prediction2=classifier2.predict(X_train2)
training_data_accuracy2=accuracy_score(X_train_prediction2, Y_train2)
X_test_prediction2=classifier2.predict(X_test2)
test_data_accuracy2=accuracy_score(X_test_prediction2, Y_test2)
def bloodai():
    ai = Toplevel()

    def send():
        send = "You => " + e.get()
        txt.insert(END, "\n" + send)
        if (e.get() == "hello"):
            txt.insert(END, "\n" + "Doc => Hi there ,I'am your vitual doctor")
        elif (e.get() == "i have doubts on bp"):
            txt.insert(END, "\n" + "Doc => please enter your values.")
        elif (e.get() == "140 and 100"):
            txt.insert(END,
                       "\n" + "You are having HYPERTENSION, few suggestions:" + "\n" + "1.Dont feel stress." + "\n" + "2.use medicenes regularly(cilidin.)")
        elif (e.get() == "100 and 60"):
            txt.insert(END,
                       "\n" + "Doc =>YOU are having HYPOTENSION, Here are some precautions:" + "\n" + "1.sit or lie down few minutes" + "\n" + "2.use vasopressor.")

        else:
            txt.insert(END, "\n" + "Doc => Sorry I didnt get it")
        e.delete(0, END)

    txt = Text(ai, bg="slategrey", fg="lightcoral")
    txt.grid(row=0, column=0, columnspan=2)
    ai.config(bg="lightsteelblue")
    ai.title("Diabeties chat bot")
    e = Entry(ai, width=100, bg="whitesmoke", fg="salmon")
    send = Button(ai, text="send", command=send).grid(row=1, column=1)
    e.grid(row=1, column=0)
    ai.title("CHATBOT")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Bp():
    shekar=messagebox.askquestion("hello", "Are you sure")
    if shekar=="yes":
        blood = Toplevel()
        blood.title("Brain")
        blood.geometry("600x600")
        blood.config(bg="thistle")
        def bps():
            i = a.get()
            j = b.get()
            k = c.get()
            l = d.get()
            m = e.get()
            n = f.get()
            o = g.get()
            p = h.get()
            #q = ii.get()
            #r = jj.get()
            input_data2 = (55,1,0,140,217,0,1,111,1,5.6,0,0,3)
            inasnp2 = np.asarray(input_data2)
            indere2 = inasnp2.reshape(1, -1)
            std_data2 = scaler2.transform(indere2)
            prediction2 = classifier2.predict(std_data2)
            if prediction2[0]==0:
                messagebox.showinfo("Report", "You are Safe"+"\n"+"You are not Having BloodPressure")
            else:
                messagebox.showinfo("Report", "You are  Having BloodPressure" + "\n" + "If you want you can contact the Virtual Doctor"+"\n"+"Please contact")
        Label(blood, text="Haemoglobin", font=("arial", 20), bg="thistle", fg="papayawhip").place(x=30, y=50)
        a = Entry(blood, bg="gainsboro", fg="indianred", borderwidth=3, width=18)
        a.place(x=190, y=55)
        Label(blood, text="Genetic", font=("arial", 20), bg="thistle", fg="papayawhip").place(x=320, y=45)
        b = Entry(blood, bg="gainsboro", fg="indianred", borderwidth=3, width=18)
        b.place(x=430, y=50)
        Label(blood, text="Age", font=("arial", 20), bg="thistle", fg="papayawhip").place(x=50, y=150)
        c = Entry(blood, bg="gainsboro", fg="indianred", borderwidth=3, width=18)
        c.place(x=190, y=150)
        Label(blood, text="BMI", font=("arial", 20), bg="thistle", fg="papayawhip").place(x=330, y=148)
        d = Entry(blood, bg="gainsboro", fg="indianred", borderwidth=3, width=18)
        d.place(x=430, y=150)
        Label(blood, text="Smoking", font=("arial", 20), bg="thistle", fg="papayawhip").place(x=50, y=240)
        e = Entry(blood, bg="gainsboro", fg="indianred", borderwidth=3, width=18)
        e.place(x=190, y=243)
        Label(blood, text="Alcohol", font=("arial", 20), bg="thistle", fg="papayawhip").place(x=320, y=245)
        f = Entry(blood, bg="gainsboro", fg="indianred", borderwidth=3, width=18)
        f.place(x=430, y=245)
        Label(blood, text="Stress", font=("arial", 20), bg="thistle", fg="papayawhip").place(x=50, y=335)
        g = Entry(blood, bg="gainsboro", fg="indianred", borderwidth=3, width=18)
        g.place(x=190, y=335)
        Label(blood, text="Chronic", font=("arial", 20), bg="thistle", fg="papayawhip").place(x=320, y=335)
        h = Entry(blood, bg="gainsboro", fg="indianred", borderwidth=3, width=18)
        h.place(x=430, y=338)
        Button(blood, text="submit", font=("arial", 15), bg="red", fg="Gold", borderwidth=3, width=15,command=bps).place(
            x=220, y=400)
        Button(blood, text="AI", font=("arial", 15), bg="green", fg="Gold", borderwidth=3, width=15,command=bloodai
               ).place(x=400, y=550)


    else:
        messagebox.showinfo("hello","please select your option")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Bcancer
df=pd.read_csv("diabetes.csv")
X = df.drop(columns="Outcome", axis=1)
Y=df['Outcome']
scaler =StandardScaler()
scaler.fit(X)
standard=scaler.transform(X)
x=standard
y=df["Outcome"]
X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size=0.2, stratify=Y, random_state=2)
classifier=svm.SVC(kernel="linear")
classifier.fit(X_train, Y_train)
X_train_prediction=classifier.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction, Y_train)
X_test_prediction=classifier.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction, Y_test)
def bcancerai():
    ai = Toplevel()

    def send():
        send = "You => " + e.get()
        txt.insert(END, "\n" + send)
        if (e.get() == "hello"):
            txt.insert(END, "\n" + "Doc => Hi there ,I'am your vitual doctor")
        elif (e.get() == "i have doubts on breast cancer"):
            txt.insert(END, "\n" + "Doc => how can i help you")
        elif (e.get() == "will there be any issues by feeding mil to baby?"):
            txt.insert(END, "\n" + "YES:" + "\n" + "1.But,low chances")
        elif (e.get() == "Is there any proper method to predict breast cancer?"):
            txt.insert(END, "\n" + "yes" + "\n" + "1.THERMOLYTIX SCREENING")

        else:
            txt.insert(END, "\n" + "Doc => Sorry I didnt get it")
        e.delete(0, END)

    txt = Text(ai, bg="slategrey", fg="lightcoral")
    txt.grid(row=0, column=0, columnspan=2)
    ai.config(bg="lightsteelblue")
    ai.title("Diabeties chat bot")
    e = Entry(ai, width=100, bg="whitesmoke", fg="salmon")
    send = Button(ai, text="send", command=send).grid(row=1, column=1)
    e.grid(row=1, column=0)
    ai.title("CHATBOT")


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Bcancer():
    shekar=messagebox.askquestion("hello", "Are you sure")
    if shekar=="yes":
        bcancer = Toplevel()
        bcancer.title("bcancer")
        bcancer.geometry("600x600")
        bcancer.config(bg="lightyellow")
        def breastcancer():
            a = i.get()
            b = j.get()
            c = k.get()
            d = l.get()
            e = m.get()
            f = n.get()
            g = o.get()
            h = p.get()
            input_data = (6, 148, 72, 35, 0, 33.6, 0.627, 50)
            inasnp = np.asarray(input_data)
            indere = inasnp.reshape(1, -1)
            std_data = scaler.transform(indere)
            prediction4 = classifier.predict(std_data)
            if prediction4[0] == 0:
                messagebox.showinfo("Report", "You are Safe"+"\n"+"You are not Having Breast Cancer")
            else:
                messagebox.showinfo("Report", "You are  Having Breast Cancer" + "\n" + "If you want you can contact the Virtual Doctor"+"\n"+"Please contact")
        Label(bcancer, text="Radius", font=("arial", 20), bg="lightyellow", fg="rosybrown").place(x=40, y=50)
        i = Entry(bcancer, bg="wheat", fg="indianred", borderwidth=3, width=18)
        i.place(x=130, y=55)
        Label(bcancer, text="Perimeter", font=("arial", 20), bg="lightyellow", fg="rosybrown").place(x=280, y=45)
        j = Entry(bcancer, bg="wheat", fg="indianred", borderwidth=3, width=18)
        j.place(x=420, y=50)
        Label(bcancer, text="Area", font=("arial", 20), bg="lightyellow", fg="rosybrown").place(x=50, y=150)
        k = Entry(bcancer, bg="wheat", fg="indianred", borderwidth=3, width=18)
        k.place(x=130, y=150)
        Label(bcancer, text="Smoothmess", font=("arial", 20), bg="lightyellow", fg="rosybrown").place(x=270, y=148)
        l = Entry(bcancer, bg="wheat", fg="indianred", borderwidth=3, width=18)
        l.place(x=420, y=150)
        Label(bcancer, text="Con.Points", font=("arial", 20), bg="lightyellow", fg="rosybrown").place(x=10, y=240)
        m = Entry(bcancer, bg="wheat", fg="indianred", borderwidth=3, width=18)
        m.place(x=130, y=243)
        Label(bcancer, text="Symmetry", font=("arial", 20), bg="lightyellow", fg="rosybrown").place(x=280, y=245)
        n = Entry(bcancer, bg="wheat", fg="indianred", borderwidth=3, width=18)
        n.place(x=420, y=245)
        Label(bcancer, text="Fractal", font=("arial", 20), bg="lightyellow", fg="rosybrown").place(x=50, y=335)
        o = Entry(bcancer, bg="wheat", fg="indianred", borderwidth=3, width=18)
        o.place(x=130, y=335)
        Label(bcancer, text="Texture", font=("arial", 20), bg="lightyellow", fg="rosybrown").place(x=280, y=335)
        p = Entry(bcancer, bg="wheat", fg="indianred", borderwidth=3, width=18)
        p.place(x=420, y=338)
        Button(bcancer, text="submit", font=("arial", 15), bg="red", fg="Gold", width=15,command=breastcancer).place(
                x=200, y=400)
        Button(bcancer, text="AI", font=("arial", 15), bg="green", fg="Gold", borderwidth=3, width=15,command=bcancerai
               ).place(x=400, y=550)

    else:
        messagebox.showinfo("hello","please select your option")
sideframe=Frame(health, width=80, height=75, bg="honeydew").place(anchor=N, width=10000)
label = Label(health,text="Predicting the Healty Condition", font=("ds-digital", 25), bg="honeydew", fg="orange").place(anchor=N, x=250)
label = Label(health, text="Please select the option:", font=("ds-digital", 20), bg="lightskyblue", fg="Gold").place(anchor=N,x=150, y=90)
d=Button(health, text="Diabeties", font=("ds-digital", 20), bg="oldlace", fg="teal", width=25,command=Diabeties)
d.place(anchor=N,x=250,y=150 )
cvd=Button(health, text="Cardio Vascular Disease", font=("ds-digital", 20), bg="oldlace", fg="teal", width=25,command=Heart)
cvd.place(anchor=N,x=250,y=210 )
bt=Button(health, text="Blood Pressure", font=("ds-digital", 20), bg="oldlace", fg="teal", width=25,command=Bp)
bt.place(anchor=N,x=250,y=270 )
bc=Button(health, text="Breast cancer", font=("ds-digital", 20), bg="oldlace", fg="teal", width=25,command=Bcancer)
bc.place(anchor=N,x=250,y=330 )
changeOnHover(d, "red", "oldlace")
changeOnHover(cvd, "red", "oldlace")
changeOnHover(bt, "red", "oldlace")
changeOnHover(bc, "red", "oldlace")
mainloop()