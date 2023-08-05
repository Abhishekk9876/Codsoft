from tkinter import *
import subprocess

root = Tk()
root.geometry("550x365+300+200")
bg_image = PhotoImage(file="image/background_image.png")
Label(root,image=bg_image).place(x=0,y=0)
root.resizable(False,False)



def F_login():
    root.destroy()
    subprocess.Popen(['python', 'Quiz_game_F.py'])

B1 = Button(root, text ="Student Login",font=("Helvetica",12,"bold"), relief=RAISED,border=10,bg="purple")
B1.place(x=220,y=90)

B1 = Button(root, text ="faculty Login",font=("Helvetica",12,"bold"), relief=RAISED,border=10,bg="purple",command = F_login) 
B1.place(x=220,y=200)





root.mainloop()
