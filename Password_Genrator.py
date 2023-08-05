from tkinter import *
from tkinter import messagebox
import random
root = Tk()
root.title("Password Genrator")
root.geometry("700x500")
g=""
def generate_password():
    E3.config(state="normal")
    E3.delete("1.0",END)
    try:
        length = int( E2.get("1.0",END))
        global g
        for i in range(0,length):
            a=random.randint(65,90)
            a=chr(a)
            b=random.randint(97,122)
            b=chr(b)
            c=["?","@","!","$","&"]
            c=random.choice(c)
            d=str(random.randint(0,9))
            h=[a,b,c,d]
            f=random.choice(h)
            g+=f
        
        E3.insert(END,g)
        E3.config(state="disabled")
    except:
         messagebox.showwarning("warning","Insert the Length properly: ",parent=root)

    
def accept():
     messagebox.showinfo("GENRATED PASSWORD",g,parent=root)

def reset():
     E3.config(state="normal")
     E1.delete("1.0",END)
     E2.delete("1.0",END)
     E3.delete("1.0",END)


Label(root,text="Password Generator",font=('arial',20,'bold','underline'),fg="blue").place(x=180,y=10)
Label(root,text="Enter User name: ",font=('arial',15)).place(x=50,y=70)
E1=Text(root,width=30,height=1,border=5,font=('arial',10))
E1.place(x=250,y=70)




Label(root,text="Enter password length: ",font=('arial',15)).place(x=5,y=120)
E2=Text(root,width=30,height=1,border=5,font=('arial',10))
E2.place(x=250,y=120)


scrollbar = Scrollbar(root)
scrollbar.place(x=480, y=170, height=25)

Label(root,text="Genrated password: ",font=('arial',15)).place(x=30,y=170)
E3=Text(root,width=30,height=1,border=5,font=('arial',10))
E3.place(x=250,y=170)

E3.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=E3.yview)

Generate_Password=Button(root,text="GENERATE PASSWORD",font=('arial',15),width=30,height=1,bg='blue',fg='white',command=generate_password)
Generate_Password.place(x=210,y=220)

Accept=Button(root,text="ACCEPT",font=('arial',15),width=15,height=1,bg='white',fg='blue',command=accept)
Accept.place(x=280,y=285)

Reset=Button(root,text="RESET",font=('arial',15),width=15,height=1,bg='white',fg='blue',command=reset)
Reset.place(x=280,y=350)

root.mainloop()
