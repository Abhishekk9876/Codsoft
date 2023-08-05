# Python program to create a simple GUI
# calculator using Tkinter
# import everything from tkinter module

from tkinter import *

# Function to update expression
# in the text entry box

def get(num):
    T.insert(END,num)

# Function to clear the contents
# of text entry box

def Clear():
    T.delete(0,END)
def equal():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
    # Put that code inside the try block
    # which may generate the error
    try:
        # eval function evaluate the expression
        result=eval(T.get())
        Clear()
        T.insert(0,result)
    except:
        Clear()
        T.insert(0,"Error")

# create a GUI window
root=Tk()
root.geometry("220x295")
root.title("Calculator")


#Creted a frame
#f=Frame(root,borderwidth=8,relief=SUNKEN)
#f.pack(fill="both")
T=Entry(root,width=33,relief=RAISED,borderwidth=6)
T.grid(row=0,columnspan=5)

# create a Buttons and place at a particular
# location inside the frame window .
# when user press the button, the command or
# function affiliated to that button is executed .

B1=Button(root,text="1",fg='white', bg='grey', width=5,height=3,command=lambda :get(1) ,relief=RAISED,borderwidth=6)
B2=Button(root,text="2",fg='white', bg='grey', width=5,height=3,command=lambda :get(2),relief=RAISED,borderwidth=6)
B3=Button(root,text="3",fg='white', bg='grey', width=5,height=3,command=lambda :get(3),relief=RAISED,borderwidth=6)
B10=Button(root,text="+",fg='white', bg='grey', width=5,height=3,command=lambda :get("+"),relief=RAISED,borderwidth=6)
B4=Button(root,text="4",fg='white', bg='grey', width=5,height=3,command=lambda :get(4),relief=RAISED,borderwidth=6)
B5=Button(root,text="5",fg='white', bg='grey', width=5,height=3,command=lambda :get(5),relief=RAISED,borderwidth=6)
B6=Button(root,text="6",fg='white', bg='grey', width=5,height=3,command=lambda :get(6),relief=RAISED,borderwidth=6)
B11=Button(root,text="-",fg='white', bg='grey', width=5,height=3,command=lambda :get("-"),relief=RAISED,borderwidth=6)
B7=Button(root,text="7",fg='white', bg='grey', width=5,height=3,command=lambda :get(7),relief=RAISED,borderwidth=6)
B8=Button(root,text="8",fg='white', bg='grey', width=5,height=3,command=lambda :get(8),relief=RAISED,borderwidth=6)
B9=Button(root,text="9",fg='white', bg='grey', width=5,height=3,command=lambda :get(9),relief=RAISED,borderwidth=6)
B12=Button(root,text="*",fg='white', bg='grey', width=5,height=3,command=lambda :get("*"),relief=RAISED,borderwidth=6)
B13=Button(root,text="/",fg='white', bg='grey', width=5,height=3,command=lambda :get("/"),relief=RAISED,borderwidth=6)
B0=Button(root,text="0",fg='white', bg='grey', width=5,height=3,command=lambda :get(0),relief=RAISED,borderwidth=6)
AC=Button(root,text="AC",fg='white', bg='grey', width=5,height=3,command=lambda :Clear(),relief=RAISED,borderwidth=6)
Eq=Button(root,text="=",fg='white', bg='grey', width=5,height=3,command=lambda :equal(),relief=RAISED,borderwidth=6)
B1.grid(row=1,column=0)
B2.grid(row=1,column=1)
B3.grid(row=1,column=2)
B10.grid(row=1,column=3)
B4.grid(row=2,column=0)
B5.grid(row=2,column=1)
B6.grid(row=2,column=2)
B11.grid(row=2,column=3)
B7.grid(row=3,column=0)
B8.grid(row=3,column=1)
B9.grid(row=3,column=2)
B12.grid(row=3,column=3)
B13.grid(row=4,column=3)
B0.grid(row=4,column=1)
AC.grid(row=4,column=0)
Eq.grid(row=4,column=2)

# start the GUI
root.mainloop()
