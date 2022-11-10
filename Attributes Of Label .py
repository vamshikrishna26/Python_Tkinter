from tkinter import *
root=Tk()
root.geometry("1100x1100")
root.title(" WIKIPEDIA  ")
root_label=Label(text="""Abdul Rashid Salim Salman Khan (Hindi: [səlˈmɑːn xɑːn]; 27 December 1965)[2] is an Indian actor, 
\nfilm producer, and television personality who works in Hindi films.
 \nIn a film career spanning over thirty years, Khan has received numerous awards, including two National Film Awards as a film producer, 
 \nand two Filmfare Awards as an actor.[3] He is cited in the media as one of the most commercially successful actors of Indian cinema. 
 \nForbes has included Khan in listings of the highest-paid celebrities in the world, in 2015 and 2018, with him being the highest-ranked Indian in the latter year""",
                 bg="red",fg="blue",padx=100,pady=123,font=("comicsansms",12,"bold"),borderwidth=20,relief=SUNKEN

                 )
root_label.pack()

root.mainloop()
