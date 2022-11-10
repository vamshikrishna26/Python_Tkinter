from tkinter import *
photo_root=Tk()
photo_root.title("my GUI program")
photo_root.geometry("1350x1000")
photo=PhotoImage(file="John-Wick-Chapter-4-SDCC-Title-Card.png")
photo_label=Label(image=photo)
photo_label.pack()

photo_root.mainloop()
