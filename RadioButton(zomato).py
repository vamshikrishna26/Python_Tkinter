from tkinter import *
from tkinter import messagebox as tsmg
root=Tk()
root.title("Zomato")
root.geometry("500x400")
def get_order():
    print(f"you have ordered {variable_val1.get()} from Non-Veg Menu")
    print(f"you have ordered {variable_val2.get()} from Veg Menu")
    tsmg.showinfo("Order",f"you have ordered\n{variable_val1.get()}\n{variable_val2.get()}")

Label(root,text="Drive-In",bg="yellow",fg="red",font=("comicsansms",12,"bold"),relief=RIDGE).pack()
Label(root,text="MENU",bg="purple",font=("comicsansms",12,"bold"),relief=SUNKEN).pack(anchor="w")
Label(root,text="Non-Veg",font=("comicsansms",12,"bold"),relief=RIDGE).pack(anchor="w")
variable_val1=StringVar()
variable_val1.set("radio")
Radiobutton(root,text="Chicken",variable=variable_val1,value="Chicken").pack(anchor="w")
Radiobutton(root,text="Mutton",variable=variable_val1,value="Mutton").pack(anchor="w")
Radiobutton(root,text="Fish",variable=variable_val1,value="Fish").pack(anchor="w")
Label(root,text="Veg",font=("comicsansms",12,"bold"),relief=RIDGE).pack(anchor="w")
variable_val2=StringVar()
variable_val2.set("radio")
Radiobutton(root,text="Panner",variable=variable_val2,value="Panner").pack(anchor="w")
Radiobutton(root,text="Panner Tikka",variable=variable_val2,value="Panner Tikka").pack(anchor="w")
Radiobutton(root,text="Butter Masala",variable=variable_val2,value="Butter Masala").pack(anchor="w")
Button(root,text="Order Now",bg="red",command=get_order).pack()


root.mainloop()