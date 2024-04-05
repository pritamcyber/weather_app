from tkinter import Tk 
from PIL import Image,ImageTk
from tkinter import *
import support
import datetime
import time
import customtkinter
from PIL import ImageTk,Image
from tkinter import ttk
import threading
from functions import functions


from weather_api import  weathers

w = weathers()
w_data = w.weather()

print(w_data)




screen  = Tk()
screen.config(background='black')
screen.geometry("700x500")
screen.title('Weather')
screen.maxsize(width=700,height=500)

now = datetime.datetime.now()

# day = datetime.datetime.now().time()


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


def dates()->tuple:
    
    days = ['Monday','Tuesday','Wednesday','Friday','Saturday','Sunday']
    day = datetime.date.today().weekday()

    current_time = now.strftime( '%H:%M:%S')
    current_time = current_time+'pm' if str(current_time)[0]=='1' or str(current_time)[0]=='2' else current_time+' am'
    print( current_time)
    print(days[int(day)])

    mydate=datetime.datetime.strftime( datetime.datetime.now(),'%B')
    print(mydate)

    datee = datetime.date.today().day
    print(f'{datee}th')
    return tuple([current_time,str(days[int(day)]),str(mydate),datee])


datess = dates()
# time_n = Label(frame,activeforeground='#9c9895',text=f'{datess[0]} ',height=1,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',font=("Antique", 20))
# time_n.place(x=95,y=50)
def time_return():
    print('time')
    modifying_date()

def modifying_date():
    now = datetime.datetime.now()
    time_n.config(text=now.strftime( '%I:%M:%S %p'))
    screen.after(1000,time_return)
    print('one')
    


# re = 





icon = PhotoImage(file='r.png')
screen.iconphoto(TRUE,icon)


framel  = customtkinter.CTkFrame(screen,corner_radius=10,bg_color='orange',height=500,fg_color='black') 
styler = ttk.Style()
styler.theme_use('default')
styler.configure('Treeview',
                        background = '#D3D3D3',
                        foreground='black',
                        rowheight='10',
                        fieldbackground = '#D3D3D3',borderwidth=0, relief="flat",highlightthickness=0, bd=0)
styler.map('Treeview',background=[('selected','#347083')])

# scrollbar = Scrollbar(framel)
# scrollbar.pack(side = RIGHT,fill=Y)

my_tree = ttk.Treeview(framel, selectmode = 'extended',show =('tree',))
my_tree.config(height=16)
# scrollbar.config(command = my_tree.yview)

names = ('State',)

my_tree['columns'] = names


my_tree.column('#0',stretch=NO,width=0,minwidth=0)
# my_tree.column('#1',stretch=YES,width=0,minwidth=0)

# my_tree.config(style=style)
# my_tree.columnconfigure(r/)

# em.data.heading(em)
# my_tree.tag_configure('oddrow',background='white')
# my_tree.tag_configure('evenrow',background='#8db2f2')
for i in names:
    my_tree.column(i,width=200,anchor=W,minwidth=20)
    my_tree.heading(i,text=i,anchor=W)

my_tree.tag_configure('oddrow',background = '#f0a573')
my_tree.tag_configure('evenrow',background = '#ed8e4e')


count = 0
indian_states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur","Meghalaya", "Mizoram"
]
rows = indian_states
global kkk
kkk = 0
for i in rows:
    if kkk %2 ==0:
        my_tree.insert(parent='',index='end',iid =kkk,text='',values=i,tags=('evenrow',))
    else:
        my_tree.insert(parent='',index='end',iid =kkk,text='',values=i,tags=('oddrow',))
    kkk +=1
# my_tree.pack()
my_tree.pack(side='left' ,fill='both',expand=True)

framel.pack(fill='x',side='left')




# right column frame

framer  = customtkinter.CTkFrame(screen,corner_radius=10,bg_color='black',height=300) 

right_state = [ 
    "Nagaland", "Odisha","Punjab","Rajasthan", "Sikkim", "Tamil Nadu",
    "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Andaman and Nicobar Islands", "Chandigarh",
    "Dadra and Nagar Haveli and Daman and Diu", "Lakshadweep", "Delhi", "Puducherry"]

style = ttk.Style()
style.theme_use('default')
style.configure('Treeview',
                        background = '#D3D3D3',
                        foreground='black',
                        rowheight='30',
                        fieldbackground = '#D3D3D3',borderwidth=0, relief="flat")
style.map('Treeview',background=[('selected','#347083')])

# scrollbar = Scrollbar(framel)
# scrollbar.pack(side = RIGHT,fill=Y)

my_treer = ttk.Treeview(framer, selectmode = 'extended',show =('tree',))
my_treer.config(height=16)
# scrollbar.config(command = my_tree.yview)

names = ('State',)

my_treer['columns'] = names


my_treer.column('#0',stretch=YES,width=0,minwidth=0)

# em.data.heading(em)
my_treer.tag_configure('oddrow',background = '#f0a573')
my_treer.tag_configure('evenrow',background = '#ed8e4e')
for i in names:
    my_treer.column(i,width=200,anchor=W,minwidth=20)
    my_treer.heading(i,text=i,anchor=W)

# my_treer.tag_configure('oddrow',background = 'white')
# my_treer.tag_configure('evenrow',background = 'lightblue')


count = 0

rows = right_state
kkk = 0
for i in rows:
    if kkk %2 ==0:
        my_treer.insert(parent='',index='end',iid =kkk,text='',values=i,tags=('evenrow',))
    else:
        my_treer.insert(parent='',index='end',iid =kkk,text='',values=i,tags=('oddrow',))
    kkk +=1
# my_tree.pack()
my_treer.pack(side='left' ,fill='both',expand=True)

framer.pack(fill='x',side='right')



# main frame
frame  =  customtkinter.CTkFrame(screen,width=300,height=500,corner_radius=10,fg_color='#f29552',border_color='#f29552',bg_color='green')
# frame.configure(background_corner_colors = 'white')
frame.pack()


day_n = Label(frame,activeforeground='#9c9895',text=f'{datess[1]},{datess[-1]}th {datess[2]}',height=2,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',font=("Antique", 15))
day_n.place(x=83,y=2)

time_n = Label(frame,activeforeground='#9c9895',text=f'{datess[0]} ',height=1,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',font=("Antique", 20))
time_n.place(x=95,y=50)

location_n = Label(frame,activeforeground='#9c9895',text=f'Delhi ',height=1,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',font=("Antique", 10))
location_n.place(x=130,y=99)
imgg = ImageTk.PhotoImage(Image.open('two_2_img.png').resize((180,180)))

img_n = Label(frame,activeforeground='#9c9895',image=imgg,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',font=("Antique", 10))
img_n.place(x=50,y=129)






import math
cel = math.floor(kelvin_to_celsius(w_data['main']['temp']))

monthes_n = Label(frame,activeforeground='#9c9895',text=f'{cel}°c',height=1,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',font=("Antique", 30))
monthes_n.place(x=115,y=310)


temp_n = Label(frame,activeforeground='#9c9895',text=f'{datess[1]}',height=1,activebackground='#9c9895',fg='#dbd7d5',bg='#f29552',font=("Antique", 30))
temp_n.place(x=97,y=370)

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



T =threading.Thread(target=modifying_date)
T.start()

my_tree.bind('<<TreeviewSelect>>', lambda a:functions.item_selected())



screen.config(bg='white')
screen.mainloop()
