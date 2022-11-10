from tkinter import *
root=Tk()
root.title(" WIKIPEDIA ")
root_label=Label(text="""
Attributes: A set of properties of a widget that defines its visual appearance on the computer screen 
\nand how it responds to user events. Here we’ll discuss the attributes of Label and Pack.
\nAttributes of Label: The Label widget is a standard Tkinter widget used to display a text or image on the screen. 
\nThere are a lot of attributes of the Label widget. Some important attributes are
""",bg="black",fg="white",pady=10,padx=10,font=("comicsansms",10,"bold"),borderwidth=20,relief=SUNKEN


                 )
root_label.pack(side=BOTTOM,anchor="se",fill=Y)
root.mainloop()

