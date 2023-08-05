from tkinter import *
import mysql.connector as msc
import subprocess

root = Tk()
root.geometry("550x365+300+200")
bg_image = PhotoImage(file="image/background_image.png")
Label(root,image=bg_image).place(x=0,y=0)
root.resizable(False,False)

mydb=msc.connect(host="localhost",user="root",passwd="", database="quiz_game")
mycur=mydb.cursor()

table_name=""

def new_quiz():
    root.withdraw()     # Close the new_quiz window  
    window=Toplevel()
    window.title("Quiz_name")
    window.geometry("550x365+300+200")
    window.resizable(False,False)
    quiz_name_image = PhotoImage(file="image/background_image.png")
    Label(window,image=quiz_name_image).place(x=0,y=0)

    #back Button
    def back():
        window.withdraw()     # Close the new_quiz window
        root.deiconify()      # Show the root window again

    back_image = PhotoImage(file="image/back.png")
    back_button = Button(window,image=back_image,bd=0,command=back)
    back_button.place(x=3,y=3)

    #home button
    def home():
        window.destroy()
        subprocess.Popen(['python', 'Quiz_Game.py'])

    home_image = PhotoImage(file="image/home.png")
    home_button = Button(window,image=home_image,bd=0,command=home)
    home_button.place(x=490,y=10)

    #submit Button
    def Submit():
        status_label = Label(window, text="", fg="black")
        status_label.pack()

        #adding table to database
        table_name = quiz_name.get()
        if not table_name:
            status_label.config(text="Quiz name name cannot be empty", fg="red")
            return
        else:
            create_table_query = f"""
                CREATE TABLE {table_name}(ques TEXT, op_A varchar(50), op_B varchar(50), op_C varchar(50), op_D varchar(50), correct_option varchar(50))"""
            try:
                # Execute the CREATE TABLE query
                mycur.execute(create_table_query)
                status_label.config(text=f"Quiz '{table_name}' table created successfully", fg="green")
            except msc.Error as err:
                status_label.config(text=f"Error: {err}", fg="red")
        mydb.commit()

        #creating new window to insert Ques and it's option
        window.withdraw()
        window1=Toplevel(root)
        window1.title("Faculty Login")
        window1.geometry('890x555+500+100')
        window1.resizable(False,False)

        bg_image2 = PhotoImage(file="image/image1.png")
        Label(window1,image=bg_image2).place(x=0,y=0)

        def Clear():
            ques.delete("1.0",END)
            op_A.delete("1.0",END)
            op_B.delete("1.0",END)
            op_C.delete("1.0",END)
            op_D.delete("1.0",END)
            mycur.close()
            mydb.close()
    
        def add():
            question = ques.get("1.0",END)
            option_A = op_A.get("1.0",END)
            option_B = op_B.get("1.0",END)
            option_C = op_C.get("1.0",END)
            option_D = op_D.get("1.0",END)
            correct_ans = corr_ans.get("1.0",END)
            mycur.execute(f"INSERT INTO {table_name} (ques, op_A, op_B, op_C, op_D, correct_option) VALUES ('{question}', '{option_A}', '{option_B}', '{option_C}', '{option_D}', '{correct_ans}')")
            mydb.commit()
            print("Added")
        def add_more():
            pass
    
        def back():
            window1.withdraw()     # Close the new_quiz window
            window.deiconify()      # Show the root window again

        back_image1 = PhotoImage(file="image/back.png")
        back_button1 = Button(window1,image=back_image1,bd=0,command=back)
        back_button1.place(x=3,y=3)
         #Question Box
        ques=Text(window1,height=5,width=70,fg="black",border=2,bg='white',font=('arial',15))
        ques.place(x=55,y=25)

        #option Label and Entry box
        Label(window1,text="A",font=("Helvetica",15,"bold")).place(x=90,y=180)
        op_A=Text(window1,font=("Helvetica",10),height=3,width=30)
        op_A.place(x=120,y=170)

        Label(window1,text="B",font=("Helvetica",15,"bold")).place(x=455,y=180)
        op_B=Text(window1,font=("Helvetica",10),height=3,width=30)
        op_B.place(x=485,y=170)

        Label(window1,text="C",font=("Helvetica",15,"bold")).place(x=90,y=300)
        op_C=Text(window1,font=("Helvetica",10),height=3,width=30)
        op_C.place(x=120,y=290)

        Label(window1,text="D",font=("Helvetica",15,"bold")).place(x=455,y=300)
        op_D=Text(window1,font=("Helvetica",10),height=3,width=30)
        op_D.place(x=485,y=290)

        
        Label(window1,text="Enter the correct answer : ",font=("Helvetica",15,"bold")).place(x=75,y=400)
        corr_ans=Text(window1,font=("Helvetica",10),height=3,width=30)
        corr_ans.place(x=375,y=390)

        

        clear_button=Button(window1, text ="Clear",font=("Helvetica",12,"bold"), relief=RAISED,border=10,bg="green",command=Clear)
        clear_button.place(x=255,y=460)

        add_button=Button(window1, text ="add",font=("Helvetica",12,"bold"), relief=RAISED,border=10,bg="green",command=add)
        add_button.place(x=350,y=460)
   

        add_more_button=Button(window1, text ="Add More",font=("Helvetica",12,"bold"), relief=RAISED,border=10,bg="green",command=add_more)
        add_more_button.place(x=450,y=460)
    


        

        window1.mainloop()

    #Quiz name label and Entry         
    Label(window,text="Enter Quiz Name ",font=("Helvetica",20,"bold"),bg="black",fg="white").place(x=180,y=90)
    quiz_name=Entry(window,width=25,fg="black",border=2,bg='white',font=('arial',15))
    quiz_name.place(x=170,y=150)
    quiz_name.focus()
   
    #Submit Button
    B3=Button(window, text ="Submit",font=("Helvetica",12,"bold"), relief=RAISED,border=10,bg="purple",command = Submit)
    B3.place(x=250,y=200)
   
    window.mainloop()


    

B1 = Button(root, text ="Creat New Quiz",font=("Helvetica",12,"bold"), relief=RAISED,border=10,bg="purple",command = new_quiz)
B1.place(x=220,y=90)

B2 = Button(root, text ="Review Old Quiz",font=("Helvetica",12,"bold"), relief=RAISED,border=10,bg="purple") 
B2.place(x=220,y=200)


root.mainloop()
