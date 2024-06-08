from tkinter import *
from PIL import ImageTk, Image

dia = Tk()
dia.title("Diadieties")
dia.geometry("600x600")
dia.config(bg="gainsboro")
#mg =Image.open("D:\python projects\health project\diabeties1.jpg")
#bg = ImageTk.PhotoImage(img).
#label = Label(dia, image=bg)
#label.place(x = 0,y = 0)


#print(i,j,k,l,m,n,o,p)
def sugar():
    i = a.get()
    j = b.get()
    k = c.get()
    l = d.get()
    m = e.get()
    n = f.get()
    o = g.get()
    p = h.get()
    print(i,j)

Label(dia, text="Pregnancies", font=("arial", 20), bg="gainsboro", fg="thistle").place(x=30, y=50)
a=Entry(dia,  bg="gainsboro", fg="Gold", borderwidth=3, width=18)
a.place(x=160, y=55)
Label(dia, text="Glucose", font=("arial", 20), bg="gainsboro", fg="papayawhip").place(x=320, y=45)
b=Entry(dia,  bg="gainsboro", fg="Gold", borderwidth=3, width=18)
b.place(x=430, y=50)
Label(dia, text="BP", font=("arial", 20), bg="gainsboro", fg="beige").place(x=50, y=150)
c=Entry(dia,  bg="gainsboro", fg="Gold", borderwidth=3, width=18)
c.place(x=130, y=150)
Label(dia, text="St.ness", font=("arial", 20), bg="gainsboro", fg="Gold").place(x=330, y=148)
d=Entry(dia,  bg="gainsboro", fg="Gold", borderwidth=3, width=18)
d.place(x=430, y=150)
Label(dia, text="Insulin", font=("arial", 20), bg="gainsboro", fg="white").place(x=50, y=240)
e=Entry(dia,  bg="gainsboro", fg="Gold", borderwidth=3, width=18)
e.place(x=140, y=243)
Label(dia, text="BMI", font=("arial", 20), bg="gainsboro", fg="Gold").place(x=320, y=245)
f=Entry(dia,  bg="gainsboro", fg="Gold", borderwidth=3, width=18)
f.place(x=430, y=245)
Label(dia, text="DPF", font=("arial", 20), bg="gainsboro", fg="Gold").place(x=50, y=335)
g=Entry(dia,  bg="gainsboro", fg="Gold", borderwidth=3, width=18)
g.place(x=130, y=335)
Label(dia, text="Age", font=("arial", 20), bg="gainsboro", fg="Gold").place(x=320, y=335)
h=Entry(dia,  bg="gainsboro", fg="Gold", borderwidth=3, width=18)
h.place(x=430, y=338)
Button(dia,text="submit", font=("arial", 15), bg="gainsboro", fg="Gold", borderwidth=3, width=15,command=sugar).place(x=180, y=400)


mainloop()
