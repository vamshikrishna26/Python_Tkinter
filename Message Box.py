from tkinter import *
from tkinter import messagebox as tmsg
root=Tk()
root.title("PY-charm")
root.geometry("500x400")
main_menu=Menu(root)
def help():
    a=tmsg.showinfo("Help","Please try later")

def rate():
    value=tmsg.askquestion("Review","How was your experience ????")
    print(value)
    if value=="yes":
        msg="rate us on playstore"
    else:
        msg="what want wrong..we will contact you soon"
    tmsg.showinfo("Experience",msg)

def backup():
    b=tmsg.askokcancel("No internet", " pls try again")
    print(b)
    if b:
        print("check your internet cable")
    else:
        print("you cancelled")
text_menu=Menu(main_menu,tearoff=0)
text_menu.add_command(label="New project")
text_menu.add_command(label="New")
text_menu.add_command(label="save")
text_menu.add_command(label="open")
text_menu.add_command(label="setting")
edit_menu=Menu(main_menu,tearoff=0)
edit_menu.add_command(label="cut")
edit_menu.add_command(label="copy")
edit_menu.add_command(label="delete")
edit_menu.add_command(label="find")
view_menu=Menu(main_menu,tearoff=0)
view_menu.add_command(label="Tool window")
view_menu.add_command(label="Tool bar")
view_menu.add_command(label="Recent files")
run_menu=Menu(main_menu,tearoff=0)
run_menu.add_command(label="Run")
run_menu.add_command(label="debug")
window_menu=Menu(main_menu,tearoff=0)
window_menu.add_command(label="Notifications")
window_menu.add_command(label="Background Task")
help_menu=Menu(main_menu,tearoff=0)
help_menu.add_command(label="Help",command=help)
help_menu.add_command(label="Rate us",command=rate)
help_menu.add_command(label="backup",command=backup)

root.config(menu=main_menu)
main_menu.add_cascade(label="Files",menu=text_menu)
main_menu.add_cascade(label="Edit",menu=edit_menu)
main_menu.add_cascade(label="View",menu=view_menu)
main_menu.add_cascade(label="Run",menu=run_menu)
main_menu.add_cascade(label="Window",menu=window_menu)
main_menu.add_cascade(label="Help",menu=help_menu)
root.mainloop()