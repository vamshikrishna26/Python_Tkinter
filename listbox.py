from tkinter import *

def add():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1
i=0
root=Tk()
lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"first listbox")
Button(root,text="add item",command=add).pack()

root.mainloop()