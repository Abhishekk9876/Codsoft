from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
import requests
import datetime

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")

root.resizable(False,False)


def search():
    state=state_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+state+"&appid=7f01d2a7d51f245841048b0c979068ac").json()
    w.config(text = data["wind"]["speed"])
    h.config(text = data["main"]["humidity"])
    c.config(text = data["weather"][0]["main"])
    d.config(text = data["weather"][0]["description"])
    temp = str(int(data["main"]["temp"]-273.15))
    t.config(text = (temp,"°"))      #temp kaa data hme kelvin me milega isiliye umse -273.5 taaki celcious me convert ho jaae or fir data ko string me convert kr diya h
    p.config(text = data["main"]["pressure"])


    local_time = datetime.datetime.now()
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    #Weather
    

    
image_icon=PhotoImage(file="image/logo.png")
root.iconphoto(False,image_icon)

#search box
search_image=PhotoImage(file="image/search.png")
myimage=Label(image=search_image)        #PhotoImage' object has no attribute 'place' that's why we have put the image to a label
myimage.place(x=20,y=20)

                     
#Combobox
state_name=StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(root,value=list_name,font=("Time new Roman",20,"bold"),textvariable=state_name)
com.place(x=50,y=40)
com.set("Select State")
com.focus()                  # focus means that the widget is ready to receive keyboard input without the user having to manually click on it or activate it.

#search icon
search_icon=PhotoImage(file="image/search_icon.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=search)
myimage_icon.place(x=400,y=34)

#logo
Logo_image=PhotoImage(file="image/logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)


#Bottom box
Frame_image=PhotoImage(file="image/box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400)

label3=Label(root,text="DISCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,'bold'),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,'bold'),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,'bold'),bg="#1ab5ef")
d.place(x=400,y=430)
p=Label(text="...",font=("arial",20,'bold'),bg="#1ab5ef")
p.place(x=680,y=430)










root.mainloop()
