from tkinter import *
root=Tk()
user=Label(text="Enter your username : ")
password=Label(text="Enter your password : ")
user.grid(row=0,column=0)
password.grid(row=1,column=0)
uservalue=StringVar()
passvalue=StringVar()
user_entry=Entry(root,textvariable=uservalue)
pass_entry=Entry(root,textvariable=passvalue)
user_entry.grid(row=0,column=1)
pass_entry.grid(row=1,column=1)
def getsval():
    print(f"your username is :{uservalue.get()}")
    print(f"your password is :{passvalue.get()}")
button_p1=Button(text="submit",command=getsval)
button_p1.grid(row=2,column=1)
root.mainloop()