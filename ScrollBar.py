from tkinter import *
root=Tk()
root.title("Scrollbar")
root.geometry("500x400")
scrollbar=Scrollbar(root)
scrollbar.pack(fill=Y,side=RIGHT)
listbox=Listbox(root,yscrollcommand=scrollbar.set)
for i in range(100):
    listbox.insert(END,f"item:{i}")
listbox.pack(fill="both")
scrollbar.config(command=listbox.yview)
root.mainloop()