from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import string, random 

root= Tk()
root.geometry("500x500")
root.title("password generator")
root.config(bg="beige")
root.resizable(False,False)

def password_generator():
    try:

        length_password = int(solidbox.get())
        small_letters= string.ascii_lowercase
        capital_letters= string.ascii_uppercase
        digits= string.digits
        special_character= string.punctuation
        all_list = []
        all_list.extend(list(small_letters))
        all_list.extend(list(capital_letters))
        all_list.extend(list(digits))
        all_list.extend(list(special_character))
        random.shuffle(all_list)
        password.set("".join(all_list[0:length_password]))
    except:
        messagebox.askretrycancel("A problem has been occured","Please try again")


all_no={1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"10",11:"11",12:"12",13:"13",14:"14",15:"15",16:"16",17:"17",18:"18",19:"19",20:"20"}

Title= Label(root,text="password generator",bg="beige",fg="black",font=("futura",15,"bold"))
Title.pack(anchor="center",pady="20px")

length= Label(root,text="select the length of your password",bg="beige",fg="darkgreen",font=("ubuntu",12))
length.place(x="20px",y="70px")

def on_enter(e):
    generate_btn['bg'] = "grey"
    generate_btn['fg'] = "white"

def on_leave(e):
    generate_btn['bg'] ="orange"
    generate_btn['fg'] = "black"

solidbox=IntVar()
selector= Combobox(root,textvariable=solidbox, state="readonly")
selector['values'] = [l for l in all_no.keys()]
selector.current(7)
selector.place(x="240px",y="72px")

generate_btn = Button(root,text="Generate Password",bg="orange",fg="black",font=("ubuntu",15),cursor="hand2",command=password_generator)
generate_btn.bind("<Enter>",on_enter)
generate_btn.bind("<Leave>",on_leave)
generate_btn.pack(anchor="center",pady="50px")


result_label= Label(root,text="Generate password Here: ",bg="beige",fg="darkgreen",font=("ubuntu",12))
result_label.place(x="20px",y="160px")

password=StringVar()
password_final= Entry(root,textvariable=password,state="readonly",fg="blue",font=("ubuntu",15))
password_final.place(x="200px",y="160px")
root.mainloop()


