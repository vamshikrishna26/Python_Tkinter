from  tkinter import *
root=Tk()
root.title("frame program")
root.geometry("200x50")

top_frame=Frame(root)
top_frame.pack()
bottom_frame=Frame(root)
bottom_frame.pack(side="bottom")

red_button=Button(top_frame,text="red",fg="red")
red_button.pack(side="left")
blue_button=Button(top_frame,text="blue",fg="blue")
blue_button.pack(side="left")
orange_button=Button(top_frame,text="orange",fg="orange")
orange_button.pack(side="left")
pink_button=Button(bottom_frame,text="pink",fg="pink")
pink_button.pack(side="bottom")


root.mainloop()