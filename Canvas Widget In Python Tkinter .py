from tkinter import *
root=Tk()
root.title("canvas")
canvas_height=800
canvas_weight=400
root.geometry(f"{canvas_height}x{canvas_weight}")
canvas_wieget=Canvas(root,height=canvas_height,width=canvas_weight)
#canvas_wieget.create_line(10,7,5,200,fill="black")
canvas_wieget.create_rectangle(3,5,350,200,fill="blue")
canvas_wieget.create_oval(3,5,350,200,fill="red")
canvas_wieget.create_arc(3,5,350,200,fill="skyblue")
#canvas_wieget.create_text(200,200,text="vamshi krishna",fill="red")
canvas_wieget.pack()
root.mainloop()