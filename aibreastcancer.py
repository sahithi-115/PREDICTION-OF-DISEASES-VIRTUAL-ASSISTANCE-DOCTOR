from tkinter import *
ai = Toplevel()
def send():
    send="You => "+e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hello"):
        txt.insert(END,"\n"+"Doc => Hi there ,I'am your vitual doctor")
    elif(e.get()=="i have doubts on breast cancer"):
        txt.insert(END, "\n" + "Doc => how can i help you")
    elif(e.get()=="will there be any issues by feeding mil to baby?"):
        txt.insert(END, "\n" + "YES:"+"\n"+"1.But,low chances")
    elif(e.get() == "Is there any proper method to predict breast cancer?"):
        txt.insert(END, "\n" + "yes"+"\n"+"1.THERMOLYTIX SCREENING")

    else:
        txt.insert(END,"\n"+"Doc => Sorry I didnt get it")
    e.delete(0,END)








txt=Text(ai,bg="slategrey",fg="lightcoral")
txt.grid(row=0,column=0,columnspan=2)
ai.config(bg="lightsteelblue")
ai.title("Diabeties chat bot")
e=Entry(ai,width=100,bg="whitesmoke",fg="salmon")
send=Button(ai,text="send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
ai.title("CHATBOT")
mainloop()
