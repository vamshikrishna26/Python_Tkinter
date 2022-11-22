from tkinter import *
from tkinter import messagebox as tmsg
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Registration Form")
        self.geometry("500x400")

    def label(self):
        self.label1=Label(self,text="Username",font=("comicsansms",15,"bold"))
        self.label1.grid(row=0,column=1,padx=20,pady=10)
        self.label2=Label(self,text="Password",font=("comicsansms",15,"bold"))
        self.label2.grid(row=1,column=1,padx=20,pady=10)

    def entry(self):
        self.inputname=StringVar()
        self.inputpass=StringVar()
        self.entry1=Entry(self,textvariable=self.inputname)
        self.entry1.grid(row=0,column=2)
        self.entry2 = Entry(self, textvariable=self.inputpass,show='*')
        self.entry2.grid(row=1, column=2)

    def getting_information(self):
        print("Welcome")
        tmsg.showinfo("Login page",f"you are successfully login through {self.inputname.get()} and {self.inputpass.get()}")
    def button(self):
        self.buttonb1=Button(self,text="Login",relief=SUNKEN,command=self.getting_information)
        self.buttonb1.grid(row=3,column=2)
if __name__ == '__main__':
    window=GUI()
    window.label()
    window.entry()
    window.button()
    window.getting_information()
    window.mainloop()