from tkinter import *
diaai= Tk()
def send():
    send="You => "+e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hello,i'am your virtual doctor,how may i help you?"):
        txt.insert(END,"\n"+"Bot => ")
    elif(e.get()=="hi"):
        txt.insert(END, "\n" + "Bot => hello")
    elif(e.get()=="how are you"):
        txt.insert(END, "\n" + "Bot => fine and you")
    elif(e.get()=="fine"):
        txt.insert(END, "\n" + "Bot => Nice To Hear")
    else:
        txt.insert(END,"\n"+"Bot => sorry I didnt get it")
    e.delete(0,END)
txt=Text(diaai,bg="pink",fg="black")
txt.grid(row=0,column=0)
e=Entry(diaai,width=100, borderwidth=10, bg="aqua", fg="white",font=("Bold",10))
send=Button(diaai,text="send",bg="red", fg="gold", command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
diaai.title("CHATBOT")
diaai.config(bg="plum")
mainloop()



