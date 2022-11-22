from tkinter import *
root=Tk()
def update():
    statusbar.set("busy...!!")
    import time
    label1.update()
    time.sleep(2)
    statusbar.set("ready now")


root.title("status bar")
root.geometry("500x400")
statusbar=StringVar()
statusbar.set("ready")
label1=Label(root,textvariable=statusbar,relief=SUNKEN,anchor="w",bg="red")
label1.pack(side=BOTTOM,fill=X)
Button(root,text="update",command=update).pack()
root.mainloop()