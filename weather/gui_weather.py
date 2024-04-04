from tkinter import Tk 
from PIL import Image,ImageTk
from tkinter import *
import support
import datetime
import time
import customtkinter
from PIL import ImageTk,Image

from weather_api import  weathers

w = weathers()
w_data = w.weather()

print(w_data)




screen  = Tk()
screen.geometry("500x500")
screen.title('Weather')

now = datetime.datetime.now()

# day = datetime.datetime.now().time()


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


def dates()->tuple:
    
    days = ['Monday','Tuesday','Wednesday','Friday','Saturday','Sunday']
    day = datetime.date.today().weekday()

    current_time = now.strftime("%H:%M")
    current_time = current_time+'pm' if str(current_time)[0]=='1' or str(current_time)[0]=='2' else current_time+' am'
    print( current_time)
    print(days[int(day)])

    mydate=datetime.datetime.strftime( datetime.datetime.now(),'%B')
    print(mydate)

    datee = datetime.date.today().day
    print(f'{datee}th')
    return tuple([current_time,str(days[int(day)]),str(mydate),datee])


datess = dates()





icon = PhotoImage(file='r.png')
screen.iconphoto(TRUE,icon)

frame  =  customtkinter.CTkFrame(screen,width=300,height=500,corner_radius=20,fg_color='#f29552')
frame.pack()


day_n = Label(frame,activeforeground='#9c9895',text=f'{datess[1]},{datess[-1]}th {datess[2]}',height=2,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',font=("Antique", 15))
day_n.place(x=83,y=2)

time_n = Label(frame,activeforeground='#9c9895',text=f'{datess[0]} ',height=1,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',font=("Antique", 20))
time_n.place(x=95,y=50)

location_n = Label(frame,activeforeground='#9c9895',text=f'Delhi ',height=1,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',font=("Antique", 10))
location_n.place(x=140,y=99)
imgg = ImageTk.PhotoImage(Image.open('two_2_img.png').resize((150,150)))

img_n = Label(frame,activeforeground='#9c9895',image=imgg,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',font=("Antique", 10))
img_n.place(x=80,y=129)






import math
cel = math.floor(kelvin_to_celsius(w_data['main']['temp']))

monthes_n = Label(frame,activeforeground='#9c9895',text=f'{cel}°c',height=1,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',font=("Antique", 30))
monthes_n.place(x=125,y=310)


temp_n = Label(frame,activeforeground='#9c9895',text=f'{datess[1]}',height=1,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',font=("Antique", 30))
temp_n.place(x=110,y=370)

line  = customtkinter.CTkFrame(frame,width=190,height=1,bg_color='white')
line.place(x=65,y=430)

cloudes = ImageTk.PhotoImage(Image.open('three_3_img.png').resize((20,20)))

cloude_img = Label(frame,activeforeground='#9c9895',image=cloudes,height=15,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552')
cloude_img.place(x=39,y=439)
cloude_n = Label(frame,activeforeground='#9c9895',text=f'Cloudes',height=1,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',font=("Antique", 10))
cloude_n.place(x=25,y=460)
cloude_n = Label(frame,activeforeground='#9c9895',text=f'{w_data['clouds']['all']}%',height=1,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',font=("Antique", 10))
cloude_n.place(x=35,y=420)


humidty = ImageTk.PhotoImage(Image.open('hum.png').resize((17,17)))

humidty_img = Label(frame,activeforeground='#9c9895',image=humidty,height=15,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',)
humidty_img.place(x=129,y=440)
humidity_na = Label(frame,activeforeground='#9c9895',text=f'Humidity',height=1,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',font=("Antique", 10))
humidity_na.place(x=115,y=460)
humidity_n = Label(frame,activeforeground='#9c9895',text=f'{w_data['main']['humidity']}%',height=1,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',font=("Antique", 10))
humidity_n.place(x=125,y=420)

air = ImageTk.PhotoImage(Image.open('air.png').resize((25,25)))

air_img = Label(frame,activeforeground='#9c9895',image=air,height=15,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',)
air_img.place(x=209,y=442)
air_na = Label(frame,activeforeground='#9c9895',text=f'Air',height=1,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',font=("Antique", 10))
air_na.place(x=209,y=460)
air_n = Label(frame,activeforeground='#9c9895',text=f'{w_data['wind']['speed']}m/s',height=1,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',font=("Antique", 10))
air_n.place(x=205,y=420)






screen.config(bg='white')
screen.mainloop()
