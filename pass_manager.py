from tkinter import *
from tkinter import messagebox
import random

#---------------------Password Generator----------------------
def gen_pass():
    password_input.delete(0,END)
    alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num=['1','2','3','4','5','6','7','8','9','0']
    symbols=["!","@","#","%","&","*"]
    random_password=[]
    for i in range(random.randint(8,10)):
        random_password.append(random.choice(alpha))
    for i in range(random.randint(2,4)):
        random_password.append(random.choice(num))
    for i in range(random.randint(2,4)):
        random_password.append(random.choice(symbols))
    random.shuffle(random_password)
    rand_pass="".join(random_password)
    password_input.insert(0,rand_pass)
    

#----------------------Save Password-------------------------=
def save_entries():
    website=website_input.get()
    email=email_input.get()
    password=password_input.get()
    if len(password)==0 or len(website)==0:
        if len(website)==0:
            messagebox.showinfo(message="You have left website entry empty",title="Error")
        elif len(password)==0:
            messagebox.showinfo(message="You have left password field empty",title="Error")
    else:
        is_ok=messagebox.askyesno(title=website,message=f"These are the detailed which you have entered:\nEmail:{email}\nPassword:{password}")

        if is_ok:
            with open("entry.txt","a") as file:
                file.write(f"| {website} | {email} | {password} |\n")
                website_input.delete(0,END)
                password_input.delete(0,END)



#------------------------UI------------------------------------
window=Tk()
window.title("My Password Manager")
window.config(padx=100,pady=100)

canvas=Canvas(width=200,height=200)
img=PhotoImage(file=r"C:\Users\hp 840g2\Documents\python\my pass manager\logo.png")
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website:",)
website_label.grid(row=1,column=0)

website_input=Entry(width=35)
website_input.grid(row=1,column=1,columnspan=2)
website_input.focus()

email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)

email_input=Entry(width=35)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,"@gmail.com")

password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

password_input=Entry(width=35)
password_input.grid(row=3,column=1,columnspan=2)

password_button=Button(text="Password Generate",command=gen_pass)
password_button.grid(row=3,column=2)

submit_button=Button(text="Add",width=28,bg="white",command=save_entries)
submit_button.grid(row=4,column=1,columnspan=2)


window.mainloop()
