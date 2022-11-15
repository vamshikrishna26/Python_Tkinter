from tkinter import *
root=Tk()
def harry(event):
    print(f"you clicked on the button at{event.x} and {event.y}")
canvas_height=200
canvas_width=400
root.title("YOUTUBE")
Label(root,text="Scout",font=("comicsansms",7,"bold"),bg="black",fg="skyblue",relief=SUNKEN).pack()
button1=Button(root,text="SUBSCRIBE",font=("comicsansms",7,"bold"),bg="red",fg="white",relief=SUNKEN)
button1.pack()
button1.bind('<Button-1>',harry)
button1.bind('<Double-1>',quit)
root.mainloop()