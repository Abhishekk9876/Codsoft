from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("ToDo List")
root.geometry("900x700")
root.resizable(False,False)

entries = []  # List to store Entry widgets
i=0
j=8
def Submit():
    a = item.get("1.0",END)
    global i,j
    entries.append(a)  # Store the entry in the list
    # Create a new Entry widget for the next input
    new_entry = Text(root, width=25,height=2, fg="black", border=5, bg='white', font=('arial', 20))
    if(len(entries)>15):
        messagebox.showwarning("warning","""Queue is full no more templates
                        will be provided reuse the used templates""",parent=root)
    elif(len(entries)>7):
        new_entry.place(x=490, y=(len(entries)-j)*100+180)
        scrollbar = Scrollbar(root)
        scrollbar.place(x=880, y=(len(entries)-j)*100+180, height=70)
        new_entry.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=new_entry.yview)
        j=j+1
    else:
        new_entry.place(x=30, y=(len(entries)-i)*100+180)
        scrollbar = Scrollbar(root)
        scrollbar.place(x=420, y=(len(entries)-i)*100+180, height=70)
        new_entry.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=new_entry.yview)
        i = i+1
    entries.append(new_entry)
    new_entry.insert(END,a)    

Frame(root, width=900, height=130, bg='#24AD36').place(x=0,y=0)
Label(root, text="ToDo List", font=('Comic Sans MS',30,'bold'),bg='#24AD36').place(x=40,y=30)
Label(root, text="Add Items", font=('arial',20,'bold')).place(x=30,y=140)

scrollbar = Scrollbar(root)
scrollbar.place(x=420, y=180, height=70)


item = Text(root, width=25, height=2, fg="black", border=5, bg='white', font=('arial', 20))
item.place(x=30, y=180)

item.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=item.yview)


submit = Button(root, text="Submit", width=10, height=2, bg='grey', fg='white', command=Submit)
submit.place(x=490, y=180)


root.mainloop()


