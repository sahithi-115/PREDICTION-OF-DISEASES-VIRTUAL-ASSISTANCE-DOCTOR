from tkinter import *
ai = Toplevel()
def send():
    send="You => "+e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hello"):
        txt.insert(END,"\n"+"Doc => Hi there ,I'am your vitual doctor")
    elif(e.get()=="i have doubts on heart issues"):
        txt.insert(END, "\n" + "Doc => are you having ribcage/left chest pain")
    elif(e.get()=="yes"):
        txt.insert(END, "\n" + "here are some suggestions:"+"\n"+"1.use (aspirin) tablet."+"\n"+"2.Immediately consult a doctor.)")
    elif(e.get() == "no"):
            txt.insert(END, "\n" + "Doc => you are safe,Here are some precautions:"+"\n"+"1.Avoid smoking & Drinking"+"\n"+"2.Dont take more stress.")

    else:
        txt.insert(END,"\n"+"Doc => Sorry I didnt get it")
    e.delete(0,END)







txt=Text(ai)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(ai,width=100)
send=Button(ai,text="send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
ai.title("CHATBOT")
mainloop()


