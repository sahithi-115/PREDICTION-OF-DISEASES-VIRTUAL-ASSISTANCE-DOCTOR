from tkinter import *
ai = Toplevel()
def send():
    send="You => "+e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hello"):
        txt.insert(END,"\n"+"Doc => Hi there ,I'am your vitual doctor")
    elif(e.get()=="i have doubts on sugar"):
        txt.insert(END, "\n" + "Doc => how can i help you")
    elif(e.get()=="i have sugar"):
        txt.insert(END, "\n" + "here are some suggestions:"+"\n"+"1.daily do yoga."+"\n"+"2.use medicenes regularly(glycomate.)")
    elif(e.get() == "i dont have sugar"):
            txt.insert(END, "\n" + "Doc => Here are some precautions:"+"\n"+"1.Are you having genetic sugar?"+"\n"+"2.do exersise regularly.")

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
