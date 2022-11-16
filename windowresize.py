from tkinter import *
root=Tk()
root.title("widget resolver")
root.geometry("300x250")

def set_widget():
    height_value=height_user.get()
    widht_value=widht_user.get()
    root.geometry(f"{height_value}x{widht_value}")
Label(text="Window Resizer", font="comicsansms 11 bold", pady=20).grid(column=4)
Label(text="enter the height",font="comicsansms 11 bold", pady=7).grid(row=1,column=4)
Label(text="enter the width",font="comicsansms 11 bold", pady=6).grid(row=2,column=4)
height_user=StringVar()
widht_user=StringVar()
Entry(root,textvariable=height_user).grid(row=1,column=5)
Entry(root,textvariable=widht_user).grid(row=2,column=5)
Button(root,text="submit",command=set_widget).grid(row=3,column=5)
root.mainloop()