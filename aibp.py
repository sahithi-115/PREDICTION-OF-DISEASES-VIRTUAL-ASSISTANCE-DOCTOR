from tkinter import *
ai = Toplevel()
def send():
    send="You => "+e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hello"):
        txt.insert(END,"\n"+"Doc => Hi there ,I'am your vitual doctor")
    elif(e.get()=="i have doubts on bp"):
        txt.insert(END, "\n" + "Doc => please enter your values.")
    elif(e.get()=="140 and 100"):
        txt.insert(END, "\n" + "You are having HYPERTENSION, few suggestions:"+"\n"+"1.Dont feel stress."+"\n"+"2.use medicenes regularly(cilidin.)")
    elif(e.get() == "100 and 60"):
            txt.insert(END, "\n" + "Doc =>YOU are having HYPOTENSION, Here are some precautions:"+"\n"+"1.sit or lie down few minutes"+"\n"+"2.use vasopressor.")

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
