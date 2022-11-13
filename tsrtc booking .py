from tkinter import *
root=Tk()
def get_vals():
    print("successful completed :)")
root.title("TSRTC BOOKING CENTRE")
root.geometry("500x300")
Label(text=" WELCOME TO TSRTC TRAVELS ",font=("comicsansms",11,"bold")).grid(row=0,column=3,pady=11)
Label(text="Name : ",font=("comicsansms",11,"bold")).grid(row=1,column=3)
Label(text=" Phone.Number :",font=("comicsansms",11,"bold")).grid(row=2,column=3)
Label(text=" Gender:",font=("comicsansms",11,"bold")).grid(row=3,column=3)
Label(text=" Emergency number :",font=("comicsansms",11,"bold")).grid(row=4,column=3)
Label(text="Payment mode :",font=("comicsansms",11,"bold")).grid(row=5,column=3)

namevalue=StringVar()
phnovalue=StringVar()
gendervalue=StringVar()
Enumbervalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

Entry(root,textvariable=namevalue).grid(row=1,column=4)
Entry(root,textvariable=phnovalue).grid(row=2,column=4)
Entry(root,textvariable=gendervalue).grid(row=3,column=4)
Entry(root,textvariable=Enumbervalue).grid(row=4,column=4)
Entry(root,textvariable=paymentmodevalue).grid(row=5,column=4)
Checkbutton(text="you want any meals ? ",variable=foodservicevalue).grid(row=6,column=4)

Button(text="Submit",command=get_vals).grid(row=7,column=4)


root.mainloop()