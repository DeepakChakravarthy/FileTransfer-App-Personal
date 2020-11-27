from tkinter import *
from tkinter import messagebox
from mega import Mega
import tkinter.filedialog
top=Tk()
mega = Mega()
variable=StringVar()
Password=StringVar()
w = Label(top, text="Enter Email")
w.place(x=100,y=100)
w1=Label(top,text="Password")
w1.place(x=100,y=200)
Emaile = Entry(top,textvariable=variable)
Emaile.place(x=200,y=100)
Passworde=Entry(top,textvariable=Password)
Passworde.place(x=200,y=200)
def dc():
        m = mega.login(variable.get(), Password.get())
        messagebox.showinfo("Login Processing","Login Processing")
        ask = tkinter.filedialog.askopenfilename()
        file = m.upload(ask)
btn = Button(top,text="Login",command=dc)
btn.place(x=300,y=300)
top.geometry("700x700")
top.title("File Transfer")
top.mainloop()