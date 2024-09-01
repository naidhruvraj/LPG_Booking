from tkinter import *
import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk
import tkinter as tk
import pickle
import datetime
import random
import tkinter.font as tkfont
from tkinter import font

def back3():
    alter()

#updating address
    
def transform():
    global screen
    global y
    new_ad=newad.get()
    new_add.delete(0,END)
    f=open("sem2 python/database","rb")
    l=[]
    while True:
        try:
            data=pickle.load(f)
            l.append(data)
        except EOFError:
            break
    f.close()
    if new_ad!="":
        for i in l:
            if i["address"]==mobi["address"]:
                i["address"]=new_ad
                l1=Label(screen,text="UPDATED SUCCESSFULLY",fg="green",height=1,width=30,compound=CENTER)
                l1.place(x=525,y=700)
                l1.config(font=("Courier", 20,"bold italic"))
                break
        f=open("sem2 python/database","wb")
        for i in l:
            pickle.dump(i,f)
        f.close()
    else:
        l=Label(screen,text="PLEASE FILL THE DETAILS",fg="red",height=1,width=30,compound=CENTER)
        l.place(x=525,y=700)
        l.config(font=("Courier", 20,"bold italic"))

#entering new address
        
def add_change():
    Quit()
    global screen
    global new_add
    global newad
    global mobi
    screen = Tk()
    newad=StringVar()
    gif2= PhotoImage(file='sem2 python/BG3.gif')
    gif4= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/adminbg.png')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    m=up_num1
    f=open("sem2 python/database","rb")
    l=[]
    while True:
        try:
            data=pickle.load(f)
            l.append(data)
        except EOFError:
            break
    f.close()
    for mobi in l:
        if m in mobi.keys():
            Label2=Label(canvas,height=30,width=350,image=gif4,text = "WELCOME TO THE UPDATE AREA",font=("Courier", 15,"bold italic"),compound='center')
            Label2.place(relx=0.5,rely=0.02,anchor='center')
            Label3=Label(canvas,height=30,width=250,image=gif2,text = "Mobile number",font=("Courier", 15,"bold italic"),compound='center')
            Label3.place(relx=0.4,rely=0.22,anchor='center')
            Label4=Label(canvas,height=30,width=255,image=gif4,text = m,font=("Courier", 15,"bold italic"),compound='center')
            Label4.place(relx=0.6,rely=0.22,anchor='center')
            Label3=Label(canvas,height=30,width=250,image=gif4,text = "Old Address",font=("Courier", 15,"bold italic"),compound='center')
            Label3.place(relx=0.4,rely=0.32,anchor='center')
            Label4=Label(canvas,height=30,width=255,image=gif2,text = mobi["address"],font=("Courier", 15,"bold italic"),compound='center')
            Label4.place(relx=0.6,rely=0.32,anchor='center')
            Label3=Label(canvas,height=30,width=250,image=gif2,text = "New Address",font=("Courier", 15,"bold italic"),compound='center')
            Label3.place(relx=0.4,rely=0.42,anchor='center')
            new_add=Entry(canvas,textvariable = newad,font=("Courier", 20,"bold italic"),width=16)
            new_add.place(x=795,y=347)
            Label3=Label(canvas,height=30,width=250,image=gif4,text = "Name",font=("Courier", 15,"bold italic"),compound='center')
            Label3.place(relx=0.4,rely=0.12,anchor='center')
            Label4=Label(canvas,height=30,width=255,image=gif2,text = mobi["name"],font=("Courier", 15,"bold italic"),compound='center')
            Label4.place(relx=0.6,rely=0.12,anchor='center')
            B2=Button(screen,image=gif4,compound=CENTER,text='UPDATE',height= 30,width=180,command=transform)
            B2.config(font=("Courier", 20,"bold italic"))
            B2.place(x=671,y=460)
            break
    Q=Button(screen,image=gif2,compound=CENTER,text='BACK',height= 40,width=180,command=back3)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=1.0, y=0, anchor="ne")
    canvas.pack()
    screen.mainloop()

#updating delivery
    
def deli_update():
    global screen
    global y
    new_deli1=newdeli.get()
    f=open("sem2 python/database","rb")
    l=[]
    while True:
        try:
            data=pickle.load(f)
            l.append(data)
        except EOFError:
            break
    f.close()
    if new_deli1!="":
        if new_deli1=="Delivered":
            for i in l:
                if i["delivery"]==y["delivery"]:
                    i["delivery"]="Delivered"
                    i["order_time"]="No"
                    i["booking_id"]="No"
                    l1=Label(screen,text="UPDATED SUCCESSFULLY",fg="green",height=1,width=30,compound=CENTER)
                    l1.place(x=525,y=700)
                    l1.config(font=("Courier", 20,"bold italic"))
            f=open("sem2 python/database","wb")
            for i in l:
                pickle.dump(i,f)
            f.close()
        else:
            if int(new_deli1[6:10])>=y["order_time"][2]:
                if int(new_deli1[3:5])>=y["order_time"][1]:
                    if int(new_deli1[:2])>=y["order_time"][0]:
                        for i in l:
                            if i["delivery"]==y["delivery"]:
                                i["delivery"][0]=int(new_deli1[:2])
                                i["delivery"][1]=int(new_deli1[3:5])
                                i["delivery"][2]=int(new_deli1[6:10])
                                l1=Label(screen,text="UPDATED SUCCESSFULLY",fg="green",height=1,width=30,compound=CENTER)
                                l1.place(x=525,y=700)
                                l1.config(font=("Courier", 20,"bold italic"))
                                y=i
                                break
                        f=open("sem2 python/database","wb")
                        for i in l:
                            pickle.dump(i,f)
                        f.close()
                    else:
                        l=Label(screen,text="Invalid date",fg="red",height=1,width=30,compound=CENTER)
                        l.place(x=525,y=700)
                        l.config(font=("Courier", 20,"bold italic"))
                        new_deli.delete(0,END)
                else:
                    l1=Label(screen,text="Invalid date",fg="red",height=1,width=30,compound=CENTER)
                    l1.place(x=525,y=700)
                    l1.config(font=("Courier", 20,"bold italic"))
                    new_deli.delete(0,END)
            else:
                l1=Label(screen,text="Invalid date",fg="red",height=1,width=30,compound=CENTER)
                l1.place(x=525,y=700)
                l1.config(font=("Courier", 20,"bold italic"))
                new_deli.delete(0,END)
        
    else:
        l=Label(screen,text="PLEASE FILL THE DETAILS",fg="red",height=1,width=30,compound=CENTER)
        l.place(x=525,y=700)
        l.config(font=("Courier", 20,"bold italic"))

#entering new delivery
        
def deli_change():
    global screen
    global new_deli
    global newdeli
    if y["delivery"]=="No orders placed" or y["delivery"]=="Delivered":
        l1=Label(screen,text="No order placed currently",fg="green",height=1,width=30,compound=CENTER)
        l1.place(x=525,y=700)
        l1.config(font=("Courier", 20,"bold italic"))
    else:
        Quit()
        screen = Tk()
        newdeli=StringVar()
        gif2= PhotoImage(file='sem2 python/BG3.gif')
        gif4= PhotoImage(file='sem2 python/A.png')
        bg=PhotoImage(file='sem2 python/adminbg.png')
        screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
        Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
        screen.overrideredirect(True)
        #bg
        canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
        canvas.create_image(1, 1, image=bg, anchor=NW)
        m=up_num1
        Label2=Label(canvas,height=30,width=350,image=gif4,text = "WELCOME TO THE UPDATE AREA",font=("Courier", 15,"bold italic"),compound='center')
        Label2.place(relx=0.5,rely=0.02,anchor='center')
        Label3=Label(canvas,height=30,width=250,image=gif2,text = "Mobile number",font=("Courier", 15,"bold italic"),compound='center')
        Label3.place(relx=0.4,rely=0.22,anchor='center')
        Label4=Label(canvas,height=30,width=255,image=gif4,text = m,font=("Courier", 15,"bold italic"),compound='center')
        Label4.place(relx=0.6,rely=0.22,anchor='center')
        Label3=Label(canvas,height=30,width=250,image=gif4,text = "Name",font=("Courier", 15,"bold italic"),compound='center')
        Label3.place(relx=0.4,rely=0.12,anchor='center')
        Label4=Label(canvas,height=30,width=255,image=gif2,text = y["name"],font=("Courier", 15,"bold italic"),compound='center')
        Label4.place(relx=0.6,rely=0.12,anchor='center')
        Label3=Label(canvas,height=30,width=250,image=gif4,text = "Old Delivery date",font=("Courier", 15,"bold italic"),compound='center')
        Label3.place(relx=0.4,rely=0.32,anchor='center')
        Label4=Label(canvas,height=30,width=255,image=gif2,text ="{}-{}-{}".format( y["delivery"][0],y["delivery"][1],y["delivery"][2]),font=("Courier", 15,"bold italic"),compound='center')
        Label4.place(relx=0.6,rely=0.32,anchor='center')
        Label3=Label(canvas,height=30,width=250,image=gif2,text = "New Delivery date",font=("Courier", 15,"bold italic"),compound='center')
        Label3.place(relx=0.4,rely=0.42,anchor='center')
        new_deli=Entry(canvas,textvariable = newdeli,font=("Courier", 20,"bold italic"),width=16)
        new_deli.place(x=795,y=347)
        B2=Button(screen,image=gif4,compound=CENTER,text='UPDATE',height= 30,width=180,command=deli_update)
        B2.config(font=("Courier", 20,"bold italic"))
        B2.place(x=671,y=460)
        Q=Button(screen,image=gif2,compound=CENTER,text='BACK',height= 40,width=180,command=back3)
        Q.config(font=("Courier", 20,"bold italic"))
        Q.place(relx=1.0, y=0, anchor="ne")
        canvas.pack()
        screen.mainloop()
        
#update page
        
def alter():
    Quit()
    global screen
    screen = Tk()
    gif2= PhotoImage(file='sem2 python/BG3.gif')
    gif4= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/adminbg.png')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Label2=Label(canvas,height=30,width=350,image=gif4,text = "WELCOME TO THE UPDATE AREA",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.5,rely=0.02,anchor='center')
    Label3=Label(canvas,height=30,width=350,image=gif2,text = "Which one to be updated?",font=("Courier", 15,"bold italic"),compound='center')
    Label3.place(relx=0.5,rely=0.22,anchor='center')
    B2=Button(screen,image=gif4,compound=CENTER,text='ADDRESS',height= 30,width=180,command=add_change)
    B2.config(font=("Courier", 20,"bold italic"))
    B2.place(x=450,y=330)
    B2=Button(screen,image=gif4,compound=CENTER,text='DELIVERY',height= 30,width=180,command=deli_change)
    B2.config(font=("Courier", 20,"bold italic"))
    B2.place(x=911,y=330)
    Q=Button(screen,image=gif2,compound=CENTER,text='BACK',height= 40,width=180,command=admin)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=1.0, y=0, anchor="ne")
    canvas.pack()
    screen.mainloop()

   
def change():
    global screen
    global y
    global up_num1
    up_num1=unum.get()
    up_num.delete(0,END)
    if up_num1!="":
        if len(up_num1)==10:
            flag=False
            f=open("sem2 python/database","rb")
            l=[]
            while True:
                try:
                    data=pickle.load(f)
                    l.append(data)
                except EOFError:
                    break
            f.close()
            for y in l:
                if up_num1 in y.keys():
                    flag=True
                    break
            if flag==False:
                l1=Label(screen,text="MOBILE NUMBER NOT FOUND",fg="red",height=1,width=30,compound=CENTER)
                l1.place(x=525,y=700)
                l1.config(font=("Courier", 20,"bold italic"))
            else:
                alter()
        else:
            l=Label(screen,text="ENTER VALID MOBILE NUMBER",fg="red",height=1,width=30,compound=CENTER)
            l.place(x=525,y=700)
            l.config(font=("Courier", 20,"bold italic"))
    else:
        l=Label(screen,text="PLEASE FILL THE DETAILS",fg="red",height=1,width=30,compound=CENTER)
        l.place(x=525,y=700)
        l.config(font=("Courier", 20,"bold italic"))
        
def update():
    Quit()
    global screen
    global unum
    global up_num
    screen = Tk()
    unum=StringVar()
    gif2= PhotoImage(file='sem2 python/BG3.gif')
    gif4= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/adminbg.png')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Label2=Label(canvas,height=30,width=350,image=gif4,text = "WELCOME TO THE UPDATE AREA",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.5,rely=0.02,anchor='center')
    Label3=Label(canvas,height=30,width=250,image=gif2,text = "Mobile number",font=("Courier", 15,"bold italic"),compound='center')
    Label3.place(relx=0.4,rely=0.32,anchor='center')
    up_num=Entry(canvas,textvariable = unum,font=("Courier", 20,"bold italic"),width=18)
    up_num.place(x=755,y=260)
    B2=Button(screen,image=gif4,compound=CENTER,text='UPDATE',height= 30,width=180,command=change)
    B2.config(font=("Courier", 20,"bold italic"))
    B2.place(x=671,y=460)
    Q=Button(screen,image=gif2,compound=CENTER,text='BACK',height= 40,width=180,command=admin)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=1.0, y=0, anchor="ne")
    canvas.pack()
    screen.mainloop()
    
def del_rec():
    global screen
    del_num1=dnum.get()
    del_num.delete(0,END)
    if del_num1!="":
        if len(del_num1)==10:
            flag=False
            f=open("sem2 python/database","rb")
            l=[]
            while True:
                try:
                    data=pickle.load(f)
                    l.append(data)
                except EOFError:
                    break
            f.close()
            for z in l:
                if del_num1 in z.keys():
                    l.remove(z)
                    flag=True
                    break
            if flag==False:
                l1=Label(screen,text="MOBILE NUMBER NOT FOUND",fg="red",height=1,width=30,compound=CENTER)
                l1.place(x=525,y=700)
                l1.config(font=("Courier", 20,"bold italic"))
            else:
                l1=Label(screen,text="DELETION SUCCESSFULL",fg="green",height=1,width=30,compound=CENTER)
                l1.place(x=525,y=700)
                l1.config(font=("Courier", 20,"bold italic"))
                f=open("sem2 python/database","wb")
                for i in l:
                    pickle.dump(i,f)
                f.close()
        else:
            l=Label(screen,text="ENTER VALID MOBILE NUMBER",fg="red",height=1,width=30,compound=CENTER)
            l.place(x=525,y=700)
            l.config(font=("Courier", 20,"bold italic"))
    else:
        l=Label(screen,text="PLEASE FILL THE DETAILS",fg="red",height=1,width=30,compound=CENTER)
        l.place(x=525,y=700)
        l.config(font=("Courier", 20,"bold italic"))
        
def delete():
    Quit()
    global screen
    global dnum
    global del_num
    screen = Tk()
    dnum=StringVar()
    gif2= PhotoImage(file='sem2 python/BG3.gif')
    gif4= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/adminbg.png')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Label2=Label(canvas,height=30,width=350,image=gif4,text = "WELCOME TO THE DELETION AREA",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.5,rely=0.02,anchor='center')
    Label3=Label(canvas,height=30,width=250,image=gif2,text = "Mobile number",font=("Courier", 15,"bold italic"),compound='center')
    Label3.place(relx=0.4,rely=0.32,anchor='center')
    del_num=Entry(canvas,textvariable = dnum,font=("Courier", 20,"bold italic"),width=18)
    del_num.place(x=755,y=260)
    B2=Button(screen,image=gif4,compound=CENTER,text='DELETE',height= 30,width=180,command=del_rec)
    B2.config(font=("Courier", 20,"bold italic"))
    B2.place(x=671,y=460)
    Q=Button(screen,image=gif2,compound=CENTER,text='BACK',height= 40,width=180,command=admin)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=1.0, y=0, anchor="ne")
    canvas.pack()
    screen.mainloop()

def display():
    Quit()
    global screen
    screen = Tk()
    gif2= PhotoImage(file='sem2 python/BG3.gif')
    gif4= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/adminbg.png')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Label2=Label(canvas,height=30,width=350,image=gif4,text = "WELCOME TO THE VIEW AREA",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.5,rely=0.02,anchor='center')
    Label3=Label(canvas,height=30,width=250,image=gif2,text = "Mobile number",font=("Courier", 15,"bold italic"),compound='center')
    Label3.place(relx=0.4,rely=0.22,anchor='center')
    Label4=Label(canvas,height=30,width=250,image=gif4,text = mobile_num1,font=("Courier", 15,"bold italic"),compound='center')
    Label4.place(relx=0.6,rely=0.22,anchor='center')
    Label3=Label(canvas,height=30,width=250,image=gif4,text = "Address",font=("Courier", 15,"bold italic"),compound='center')
    Label3.place(relx=0.4,rely=0.32,anchor='center')
    Label4=Label(canvas,height=30,width=250,image=gif2,text = z["address"],font=("Courier", 15,"bold italic"),compound='center')
    Label4.place(relx=0.6,rely=0.32,anchor='center')
    Label3=Label(canvas,height=30,width=250,image=gif4,text = "Name",font=("Courier", 15,"bold italic"),compound='center')
    Label3.place(relx=0.4,rely=0.12,anchor='center')
    Label4=Label(canvas,height=30,width=250,image=gif2,text = z["name"],font=("Courier", 15,"bold italic"),compound='center')
    Label4.place(relx=0.6,rely=0.12,anchor='center')
    Label3=Label(canvas,height=30,width=250,image=gif2,text = "Delivery",font=("Courier", 15,"bold italic"),compound='center')
    Label3.place(relx=0.4,rely=0.42,anchor='center')
    if(z["delivery"]!="No orders placed" and z["delivery"]!="Delivered"):
        Label4=Label(canvas,height=30,width=250,image=gif4,text = "{}-{}-{}".format(z["delivery"][0],z["delivery"][1],z["delivery"][2]),font=("Courier", 15,"bold italic"),compound='center')
        Label4.place(relx=0.6,rely=0.42,anchor='center')
    else:
        Label4=Label(canvas,height=30,width=250,image=gif4,text = z["delivery"],font=("Courier", 15,"bold italic"),compound='center')
        Label4.place(relx=0.6,rely=0.42,anchor='center')
    Label3=Label(canvas,height=30,width=250,image=gif4,text = "Complaints",font=("Courier", 15,"bold italic"),compound='center')
    Label3.place(relx=0.4,rely=0.52,anchor='center')
    Label4=Label(canvas,height=30,width=250,image=gif2,text = z["complaint"],font=("Courier", 15,"bold italic"),compound='center')
    Label4.place(relx=0.6,rely=0.52,anchor='center')
    if (z["delivery"]!="No orders placed" and z["delivery"]!="Delivered")and z["complaint"]=="No":
        Label3=Label(canvas,height=30,width=250,image=gif2,text = "Booking_id",font=("Courier", 15,"bold italic"),compound='center')
        Label3.place(relx=0.4,rely=0.62,anchor='center')
        Label4=Label(canvas,height=30,width=250,image=gif4,text = z["booking_id"],font=("Courier", 15,"bold italic"),compound='center')
        Label4.place(relx=0.6,rely=0.62,anchor='center')
        Label3=Label(canvas,height=30,width=250,image=gif4,text = "Date of order",font=("Courier", 15,"bold italic"),compound='center')
        Label3.place(relx=0.4,rely=0.72,anchor='center')
        Label4=Label(canvas,height=30,width=250,image=gif2,text = "{}-{}-{}".format(z["order_time"][0],z["order_time"][1],z["order_time"][2]),font=("Courier", 15,"bold italic"),compound='center')
        Label4.place(relx=0.6,rely=0.72,anchor='center')
    elif (z["delivery"]=="No orders placed" or z["delivery"]=="Delivered") and z["complaint"]!="No":
        Label3=Label(canvas,height=30,width=250,image=gif2,text = "Date of complaint",font=("Courier", 15,"bold italic"),compound='center')
        Label3.place(relx=0.4,rely=0.62,anchor='center')
        Label4=Label(canvas,height=30,width=250,image=gif4,text = "{}-{}-{}".format(z["complaint_time"][0],z["complaint_time"][1],z["complaint_time"][2]),font=("Courier", 15,"bold italic"),compound='center')
        Label4.place(relx=0.6,rely=0.62,anchor='center')
    elif (z["delivery"]!="No orders placed" and z["delivery"]!="Delivered")and z["complaint"]!="No":
        Label3=Label(canvas,height=30,width=250,image=gif2,text = "Booking_id",font=("Courier", 15,"bold italic"),compound='center')
        Label3.place(relx=0.4,rely=0.62,anchor='center')
        Label4=Label(canvas,height=30,width=250,image=gif4,text = z["booking_id"],font=("Courier", 15,"bold italic"),compound='center')
        Label4.place(relx=0.6,rely=0.62,anchor='center')
        Label3=Label(canvas,height=30,width=250,image=gif4,text = "Date of order",font=("Courier", 15,"bold italic"),compound='center')
        Label3.place(relx=0.4,rely=0.72,anchor='center')
        Label4=Label(canvas,height=30,width=250,image=gif2,text = "{}-{}-{}".format(z["order_time"][0],z["order_time"][1],z["order_time"][2]),font=("Courier", 15,"bold italic"),compound='center')
        Label4.place(relx=0.6,rely=0.72,anchor='center')
        Label3=Label(canvas,height=30,width=250,image=gif2,text = "Date of complaint",font=("Courier", 15,"bold italic"),compound='center')
        Label3.place(relx=0.4,rely=0.82,anchor='center')
        Label4=Label(canvas,height=30,width=250,image=gif4,text = "{}-{}-{}".format(z["complaint_time"][0],z["complaint_time"][1],z["complaint_time"][2]),font=("Courier", 15,"bold italic"),compound='center')
        Label4.place(relx=0.6,rely=0.82,anchor='center')
    
    Q=Button(screen,image=gif2,compound=CENTER,text='BACK',height= 40,width=180,command=admin)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=1.0, y=0, anchor="ne")
    canvas.pack()
    screen.mainloop()
    
def search():
    global screen
    global z
    global mobile_num1
    mobile_num1=phnum.get()
    mobile_num.delete(0,END)
    if mobile_num1!="":
        if len(mobile_num1)==10:
            flag=False
            f=open("sem2 python/database","rb")
            l=[]
            while True:
                try:
                    data=pickle.load(f)
                    l.append(data)
                except EOFError:
                    break
            f.close()
            for z in l:
                if mobile_num1 in z.keys():
                    flag=True
                    break
            if flag==False:
                l1=Label(screen,text="MOBILE NUMBER NOT FOUND",fg="red",height=1,width=30,compound=CENTER)
                l1.place(x=525,y=700)
                l1.config(font=("Courier", 20,"bold italic"))
            else:
                display()
        else:
            l=Label(screen,text="ENTER VALID MOBILE NUMBER",fg="red",height=1,width=30,compound=CENTER)
            l.place(x=525,y=700)
            l.config(font=("Courier", 20,"bold italic"))
    else:
        l=Label(screen,text="PLEASE FILL THE DETAILS",fg="red",height=1,width=30,compound=CENTER)
        l.place(x=525,y=700)
        l.config(font=("Courier", 20,"bold italic"))
                
    
def view():
    Quit()
    global screen
    global phnum
    global mobile_num
    screen = Tk()
    phnum=StringVar()
    gif2= PhotoImage(file='sem2 python/BG3.gif')
    gif4= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/adminbg.png')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Label2=Label(canvas,height=30,width=350,image=gif4,text = "WELCOME TO THE VIEW AREA",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.5,rely=0.02,anchor='center')
    Label3=Label(canvas,height=30,width=250,image=gif2,text = "Mobile number",font=("Courier", 15,"bold italic"),compound='center')
    Label3.place(relx=0.4,rely=0.32,anchor='center')
    mobile_num=Entry(canvas,textvariable = phnum,font=("Courier", 20,"bold italic"),width=18)
    mobile_num.place(x=755,y=260)
    B2=Button(screen,image=gif4,compound=CENTER,text='SEARCH',height= 30,width=180,command=search)
    B2.config(font=("Courier", 20,"bold italic"))
    B2.place(x=671,y=460)
    Q=Button(screen,image=gif2,compound=CENTER,text='BACK',height= 40,width=180,command=admin)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=1.0, y=0, anchor="ne")
    canvas.pack()
    screen.mainloop()
    
def admin():
    Quit()
    global screen
    screen = Tk()
    gif2= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/adminbg.png')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Label2=Label(canvas,height=30,width=350,image=gif2,text = "WELCOME TO THE RECORDS AREA",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.5,rely=0.02,anchor='center')
    l1=Button(screen,image=gif2,compound=CENTER,text='UPDATE RECORD',height= 40,width=250,command=update)
    l1.config(font=("Courier", 20,"bold italic"))
    l1.place(relx=0.50,rely=0.45,anchor='center')
    l2=Button(screen,image=gif2,compound=CENTER,text='DELETE RECORD',height= 40,width=250,command=delete)
    l2.config(font=("Courier", 20,"bold italic"))
    l2.place(relx=0.50,rely=0.65,anchor='center')
    l3=Button(screen,image=gif2,compound=CENTER,text='VIEW RECORD',height= 40,width=250,command=view)
    l3.config(font=("Courier", 20,"bold italic"))
    l3.place(relx=0.50,rely=0.55,anchor='center')
    Q=Button(screen,image=gif2,compound=CENTER,text='BACK',height= 40,width=180,command=back)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=1.0, y=0, anchor="ne")
    canvas.pack()
    screen.mainloop()
    
def admin_verify():
    global screen
    username1 = user.get()
    password1 = pswd.get()
    username.delete(0, END)
    password.delete(0, END)
    if username1!="" and password1!="":
        f=open("sem2 python/admin","rb")
        data=pickle.load(f)
        f.close()
        for i in data:
            if i==username1 and data[i]==password1:
                admin()
            elif i==username1 and data[i]!=password1:
                l=Label(screen,text="INVALID PASSWORD",fg="red",height=1,width=30,compound=CENTER)
                l.place(x=450,y=650)
                l.config(font=("Courier", 20,"bold italic"))
            else:
                l=Label(screen,text="USER NAME NOT FOUND",fg="red",height=1,width=30,compound=CENTER)
                l.place(x=450,y=650)
                l.config(font=("Courier", 20,"bold italic"))
    else:
        l=Label(screen,text="PLEASE FILL THE DETAILS",fg="red",height=1,width=30,compound=CENTER)
        l.place(x=450,y=650)
        l.config(font=("Courier", 20,"bold italic"))

def admin_screen():
    Quit()
    global screen
    global user
    global pswd
    global username
    global password
    screen = Tk()
    user=StringVar()
    pswd=StringVar()
    gif2= PhotoImage(file='sem2 python/BG3.gif')
    bg1=PhotoImage(file='sem2 python/login1.png')
    gif3= PhotoImage(file='sem2 python/BG2.gif')
    gif4= PhotoImage(file='sem2 python/A.png')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg1, anchor=NW)
    #login credentials
    Label1=Label(canvas,height=35,width=170,image=gif2,text = "USERNAME",font=("Courier", 25,"bold italic"),compound='center')
    Label1.place(relx=0.65,rely=0.45,anchor='center')
    username=Entry(canvas,textvariable = user,font=("Courier", 20,"bold italic"),width=18)
    username.place(x=1095,y=372)
    Label2=Label(canvas,height=35,width=170,image=gif2,text = "PASSWORD",font=("Courier", 25,"bold italic"),compound='center')
    Label2.place(relx=0.65,rely=0.55,anchor='center')
    password=Entry(canvas,textvariable = pswd,font=("Courier", 20,"bold italic"),width=18,show="*")
    password.place(x=1095,y=458)
    B=Button(canvas, text = "Login",image=gif4, width = 150, height = 60,fg="red",font=("Courier", 35,"bold italic"),compound='center', command = admin_verify)
    B.place(x=950,y=600)
    Q=Button(screen,image=gif2,compound=CENTER,text='BACK',height= 40,width=180,command=back)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=1.0, y=0, anchor="ne")
    canvas.pack()
    screen.mainloop()
    
def back1():
    second_screen()
    
def back():
    Quit()
    main_screen()

def Quit():
    screen.destroy()

def registration():
    #Quit()
    global screen
    name1_reg=name.get()
    mobile1_reg = number_reg.get()
    log_pwd1_reg = pwd_reg.get()
    relog_pwd1_reg=repwd_reg.get()
    address1_reg=add_reg.get()
    name_reg.delete(0,END)
    mobile_reg.delete(0, END)
    log_pwd_reg.delete(0, END)
    relog_pwd_reg.delete(0, END)
    address_reg.delete(0,END)
    if mobile1_reg!="" and log_pwd1_reg!="" and relog_pwd1_reg!="":
        if len(mobile1_reg)==10:
            flag=True
            f=open("sem2 python/database","rb")
            l=[]
            while True:
                try:
                    data=pickle.load(f)
                    l.append(data)
                except EOFError:
                    break
            f.close()
            for i in l:
                if mobile1_reg in i.keys():
                    flag=False
            if flag==True:  
                if log_pwd1_reg == relog_pwd1_reg:
                    f=open("sem2 python/database","ab")
                    d={}
                    d["name"]=name1_reg
                    d[mobile1_reg]=log_pwd1_reg
                    d["address"]=address1_reg
                    d["delivery"]="No orders placed"
                    d["complaint"]="No"
                    d["booking_id"]="No"
                    d["complaint_time"]="No"
                    d["delivery"]="No orders placed"
                    d["order_time"]="No"
                    d["current_time"]="No"
                    d["customer_care"]="No"
                    pickle.dump(d,f)
                    f.close()
                    l=Label(screen,text="SUCCESSFUL!!!",fg="green",height=1,width=30,compound=CENTER)
                    l.place(x=525,y=500)
                    l.config(font=("Courier", 20,"bold italic"))
                else:
                    l=Label(screen,text="PASSWORD CONFIRMATION FAILED",fg="red",height=1,width=30,compound=CENTER)
                    l.place(x=525,y=500)
                    l.config(font=("Courier", 20,"bold italic"))
            else:
                l=Label(screen,text="NUMBER ALREADY EXISTS!!!",fg="red",height=1,width=30,compound=CENTER)
                l.place(x=525,y=500)
                l.config(font=("Courier", 20,"bold italic"))
        else:
            l=Label(screen,text="INVALID MOBILE NUMBER",fg="red",height=1,width=30,compound=CENTER)
            l.place(x=525,y=500)
            l.config(font=("Courier", 20,"bold italic"))
    else:
        l=Label(screen,text="PLEASE FILL THE DETAILS",fg="red",height=1,width=30,compound=CENTER)
        l.place(x=525,y=500)
        l.config(font=("Courier", 20,"bold italic"))
            
    
    
def register():
    Quit()
    global screen
    global mobile_reg
    global number_reg
    global pwd_reg
    global log_pwd_reg
    global relog_pwd_reg
    global repwd_reg
    global address_reg
    global add_reg
    global name_reg
    global name
    screen = Tk()
    name=StringVar()
    add_reg=StringVar()
    number_reg=StringVar()
    pwd_reg=StringVar()
    repwd_reg=StringVar()
    gif2= PhotoImage(file='sem2 python/BG3.gif')
    bg=PhotoImage(file='sem2 python/secondbg.png')
    gif4= PhotoImage(file='sem2 python/A.png')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Q=Button(screen,image=gif2,compound=CENTER,text='BACK',height= 40,width=180,command=back1)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=1.0, y=0, anchor="ne")
    Label2=Label(canvas,height=30,width=250,image=gif2,text = "REGISTRATION",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.5,rely=0.02,anchor='center')
    Label1=Label(canvas,height=30,width=250,image=gif2,text = "Name",font=("Courier", 15,"bold italic"),compound='center')
    Label1.place(relx=0.4,rely=0.245,anchor='center')
    name_reg=Entry(canvas,textvariable = name,font=("Courier", 20,"bold italic"),width=18)
    name_reg.place(x=755,y=195)
    Label3=Label(canvas,height=30,width=250,image=gif2,text = "Mobile number",font=("Courier", 15,"bold italic"),compound='center')
    Label3.place(relx=0.4,rely=0.32,anchor='center')
    mobile_reg=Entry(canvas,textvariable = number_reg,font=("Courier", 20,"bold italic"),width=18)
    mobile_reg.place(x=755,y=260)
    Label4=Label(canvas,height=30,width=250,image=gif2,text = "Password",font=("Courier", 15,"bold italic"),compound='center')
    Label4.place(relx=0.4,rely=0.395,anchor='center')
    log_pwd_reg=Entry(canvas,textvariable = pwd_reg,font=("Courier", 20,"bold italic"),width=18,show="*")
    log_pwd_reg.place(x=755,y=325)
    Label5=Label(canvas,height=30,width=250,image=gif2,text = "Re-enter Password",font=("Courier", 15,"bold italic"),compound='center')
    Label5.place(relx=0.4,rely=0.47,anchor='center')
    relog_pwd_reg=Entry(canvas,textvariable = repwd_reg,font=("Courier", 20,"bold italic"),width=18,show="*")
    relog_pwd_reg.place(x=755,y=390)
    Label6=Label(canvas,height=30,width=250,image=gif2,text = "Enter Address",font=("Courier", 15,"bold italic"),compound='center')
    Label6.place(relx=0.4,rely=0.545,anchor='center')
    address_reg=Entry(canvas,textvariable = add_reg,font=("Courier", 20,"bold italic"),width=18)
    address_reg.place(x=755,y=455)
    B2=Button(screen,image=gif4,compound=CENTER,text='CREATE',height= 30,width=180,command=registration)
    B2.config(font=("Courier", 20,"bold italic"))
    B2.place(x=671,y=560)
    canvas.pack()
    screen.mainloop()

def back2():
    logged_in()
    
def submit():
    f=open("sem2 python/database","rb")
    l=[]
    while True:
        try:
            data=pickle.load(f)
            l.append(data)
        except EOFError:
            break
    f.close()
    for i in l:
        if i["name"]==n:
            i["complaint"]="No"
            i["complaint_time"]="No"
            i["current_time"]="No"
            i["customer_care"]="No"
    f=open("sem2 python/database","wb")
    for i in l:
        pickle.dump(i,f)
    f.close()
    logged_in()
            
    
def tq2():
    Quit()
    global screen
    screen = Tk()
    gif2= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/service.png')
    star=PhotoImage(file='sem2 python/star.png')
    star1=PhotoImage(file='sem2 python/star1.png')
    gif4= PhotoImage(file='sem2 python/A.png')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Label2=Label(canvas,height=30,width=370,image=gif2,text = "THANK YOU",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.49,rely=0.02,anchor='center')
    Q=Button(screen,image=gif2,compound=CENTER,text='BACK',height= 40,width=180,command=back2)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=1.0, y=0, anchor="ne")
    Q=Button(screen,image= star1,command=tq1)
    Q.place(relx=0.44, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq2)
    Q.place(relx=0.47, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq3)
    Q.place(relx=0.50, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq4)
    Q.place(relx=0.53, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq5)
    Q.place(relx=0.56, rely=0.5, anchor="ne")
    B1=Button(screen,image=gif4,compound=CENTER,text='SUBMIT',height= 30,width=120,command=submit)
    B1.config(font=("Courier", 20,"bold italic"))
    B1.place(x=713,y=680)
    canvas.pack()
    screen.mainloop()
def tq3():
    Quit()
    global screen
    screen = Tk()
    gif2= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/service.png')
    star=PhotoImage(file='sem2 python/star.png')
    star1=PhotoImage(file='sem2 python/star1.png')
    gif4= PhotoImage(file='sem2 python/A.png')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Label2=Label(canvas,height=30,width=370,image=gif2,text = "THANK YOU",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.49,rely=0.02,anchor='center')
    Q=Button(screen,image=gif2,compound=CENTER,text='BACK',height= 40,width=180,command=back2)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=1.0, y=0, anchor="ne")
    Q=Button(screen,image= star1,command=tq1)
    Q.place(relx=0.44, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq2)
    Q.place(relx=0.47, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq3)
    Q.place(relx=0.50, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq4)
    Q.place(relx=0.53, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq5)
    Q.place(relx=0.56, rely=0.5, anchor="ne")
    B1=Button(screen,image=gif4,compound=CENTER,text='SUBMIT',height= 30,width=120,command=submit)
    B1.config(font=("Courier", 20,"bold italic"))
    B1.place(x=713,y=680)
    canvas.pack()
    screen.mainloop()
def tq4():
    Quit()
    global screen
    screen = Tk()
    gif2= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/service.png')
    star=PhotoImage(file='sem2 python/star.png')
    star1=PhotoImage(file='sem2 python/star1.png')
    gif4= PhotoImage(file='sem2 python/A.png')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Label2=Label(canvas,height=30,width=370,image=gif2,text = "THANK YOU",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.49,rely=0.02,anchor='center')
    Q=Button(screen,image=gif2,compound=CENTER,text='BACK',height= 40,width=180,command=back2)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=1.0, y=0, anchor="ne")
    Q=Button(screen,image= star1,command=tq1)
    Q.place(relx=0.44, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq2)
    Q.place(relx=0.47, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq3)
    Q.place(relx=0.50, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq4)
    Q.place(relx=0.53, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq5)
    Q.place(relx=0.56, rely=0.5, anchor="ne")
    B1=Button(screen,image=gif4,compound=CENTER,text='SUBMIT',height= 30,width=120,command=submit)
    B1.config(font=("Courier", 20,"bold italic"))
    B1.place(x=713,y=680)
    canvas.pack()
    screen.mainloop()
def tq5():
    Quit()
    global screen
    screen = Tk()
    gif2= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/service.png')
    star=PhotoImage(file='sem2 python/star.png')
    star1=PhotoImage(file='sem2 python/star1.png')
    gif4= PhotoImage(file='sem2 python/A.png')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Label2=Label(canvas,height=30,width=370,image=gif2,text = "THANK YOU",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.49,rely=0.02,anchor='center')
    Q=Button(screen,image=gif2,compound=CENTER,text='BACK',height= 40,width=180,command=back2)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=1.0, y=0, anchor="ne")
    Q=Button(screen,image= star1,command=tq1)
    Q.place(relx=0.44, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq2)
    Q.place(relx=0.47, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq3)
    Q.place(relx=0.50, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq4)
    Q.place(relx=0.53, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq5)
    Q.place(relx=0.56, rely=0.5, anchor="ne")
    B1=Button(screen,image=gif4,compound=CENTER,text='SUBMIT',height= 30,width=120,command=submit)
    B1.config(font=("Courier", 20,"bold italic"))
    B1.place(x=713,y=680)
    canvas.pack()
    screen.mainloop()
def tq1():
    Quit()
    global screen
    screen = Tk()
    gif2= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/service.png')
    star=PhotoImage(file='sem2 python/star.png')
    star1=PhotoImage(file='sem2 python/star1.png')
    gif4= PhotoImage(file='sem2 python/A.png')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Label2=Label(canvas,height=30,width=370,image=gif2,text = "THANK YOU",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.49,rely=0.02,anchor='center')
    Q=Button(screen,image=gif2,compound=CENTER,text='BACK',height= 40,width=180,command=back2)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=1.0, y=0, anchor="ne")
    Q=Button(screen,image= star1,command=tq1)
    Q.place(relx=0.44, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq2)
    Q.place(relx=0.47, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq3)
    Q.place(relx=0.50, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq4)
    Q.place(relx=0.53, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq5)
    Q.place(relx=0.56, rely=0.5, anchor="ne")
    B1=Button(screen,image=gif4,compound=CENTER,text='SUBMIT',height= 30,width=120,command=submit)
    B1.config(font=("Courier", 20,"bold italic"))
    B1.place(x=713,y=680)
    canvas.pack()
    screen.mainloop()
def great():
    Quit()
    global screen
    screen = Tk()
    gif2= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/service.png')
    star=PhotoImage(file='sem2 python/star.png')
    gif3= PhotoImage(file='sem2 python/BG3.gif')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Q=Button(screen,image=gif2,compound=CENTER,text='BACK',height= 40,width=180,command=back2)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=1.0, y=0, anchor="ne")
    l1=Label(screen,text="We are happy for your problem being solved",fg="green",height=1,width=60,compound=CENTER)
    l1.place(x=286,y=200)
    l1.config(font=("Courier", 20,"bold italic"))
    l1=Label(screen,text="We never disappoint our customers",fg="green",height=1,width=60,compound=CENTER)
    l1.place(x=286,y=230)
    l1.config(font=("Courier", 20,"bold italic"))
    l1=Label(screen,text="Thank You and how about rating the service person",fg="green",height=1,width=60,compound=CENTER)
    l1.place(x=286,y=280)
    l1.config(font=("Courier", 20,"bold italic"))
    Q=Button(screen,image= star,command=tq1)
    Q.place(relx=0.44, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq2)
    Q.place(relx=0.47, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq3)
    Q.place(relx=0.5, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq4)
    Q.place(relx=0.53, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq5)
    Q.place(relx=0.56, rely=0.5, anchor="ne")
    canvas.pack()
    screen.mainloop()

def we_wait():
    l1=Label(screen,text="Sorry to hear that..",fg="red",height=1,width=70,compound=CENTER)
    l1.place(x=206,y=500)
    l1.config(font=("Courier", 20,"bold italic"))
    l1=Label(screen,text="We hope you have contacted the service person",fg="red",height=1,width=70,compound=CENTER)
    l1.place(x=206,y=530)
    l1.config(font=("Courier", 20,"bold italic"))
    l1=Label(screen,text="The agency trust that the person would reach your place in few minutes",fg="red",height=1,width=70,compound=CENTER)
    l1.place(x=206,y=560)
    l1.config(font=("Courier", 20,"bold italic"))
    
def my_complaint():
    Quit()
    global screen
    screen = Tk()
    gif2= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/adminbg.png')
    gif3= PhotoImage(file='sem2 python/BG3.gif')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Q=Button(screen,image=gif2,compound=CENTER,text='BACK',height= 40,width=180,command=back2)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=1.0, y=0, anchor="ne")
    f=open("sem2 python/database","rb")
    l=[]
    while True:
        try:
            data=pickle.load(f)
            l.append(data)
        except EOFError:
            break
    f.close()
    e = datetime.datetime.now()
    Label2=Label(canvas,height=30,width=370,image=gif2,text = "WELCOME BACK",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.5,rely=0.02,anchor='center')
    for i in l:
        if i["name"]==n:
            cur_l=[]
            cur_l.append(e.day)
            cur_l.append(e.month)
            cur_l.append(e.year)
            cur_l.append(e.hour)
            cur_l.append(e.minute)
            i["current_time"]=cur_l
            if ((i["current_time"][0]>i["complaint_time"][0] or i["current_time"][1]>i["complaint_time"][1] or i["current_time"][2]>i["complaint_time"][2] or i["current_time"][3]>i["complaint_time"][3]) or i["current_time"][4]>((i["complaint_time"][4])+5)):
                if i["customer_care"]=="No":
                    s=random.randint(9000000000,9999999999)
                    i["customer_care"]=s
                l1=Label(screen,text="We have found a service person to sovle your problem...",fg="green",height=1,width=60,compound=CENTER)
                l1.place(x=286,y=500)
                l1.config(font=("Courier", 20,"bold italic"))
                l1=Label(screen,text="We believe that your problem will be solved in no time",fg="green",height=1,width=60,compound=CENTER)
                l1.place(x=286,y=530)
                l1.config(font=("Courier", 20,"bold italic"))
                l1=Label(screen,text="Service person's CONTACT number : {}".format(i["customer_care"]),fg="green",height=1,width=60,compound=CENTER)
                l1.place(x=286,y=560)
                l1.config(font=("Courier", 20,"bold italic"))
                Label2=Label(canvas,height=30,width=400,image=gif3,text = "IS YOUR PROBLEM SOLVED?",font=("Courier", 15,"bold italic"),compound='center')
                Label2.place(relx=0.5,rely=0.2,anchor='center')
                Q=Button(screen,image=gif2,compound=CENTER,text='YES',height= 40,width=180,command=great)
                Q.config(font=("Courier", 20,"bold italic"))
                Q.place(relx=0.46, rely=0.34, anchor="ne")
                Q=Button(screen,image=gif2,compound=CENTER,text='NO',height= 40,width=180,command=we_wait)
                Q.config(font=("Courier", 20,"bold italic"))
                Q.place(relx=0.67, rely=0.34, anchor="ne")
            else:
                l1=Label(screen,text="Searching...",fg="red",height=1,width=67,compound=CENTER)
                l1.place(x=273,y=500)
                l1.config(font=("Courier", 20,"bold italic"))
                l1=Label(screen,text="Please wait till we find a right person to solve your problem",fg="red",height=1,width=67,compound=CENTER)
                l1.place(x=273,y=530)
                l1.config(font=("Courier", 20,"bold italic"))
                l1=Label(screen,text="Sorry for the inconvinience caused.",fg="red",height=1,width=67,compound=CENTER)
                l1.place(x=273,y=560)
                l1.config(font=("Courier", 20,"bold italic"))
    f=open("sem2 python/database","wb")
    for i in l:
        pickle.dump(i,f)
    f.close()
    canvas.pack()
    screen.mainloop()


def noproblem():
    global screen
    l=Label(screen,text="No Problem,We are always available here to serve you",fg="green",height=1,width=60,compound=CENTER)
    l.place(x=286,y=500)
    l.config(font=("Courier", 20,"bold italic"))
    l=Label(screen,text="",fg="green",height=1,width=60,compound=CENTER)
    l.place(x=286,y=530)
    l.config(font=("Courier", 20,"bold italic"))
    l=Label(screen,text="",fg="green",height=1,width=60,compound=CENTER)
    l.place(x=286,y=560)
    l.config(font=("Courier", 20,"bold italic"))
    
def sorry():
    global screen
    l=Label(screen,text="Sorry to hear that...",fg="red",height=1,width=60,compound=CENTER)
    l.place(x=286,y=500)
    l.config(font=("Courier", 20,"bold italic"))
    l=Label(screen,text="We would shortly assign a person to solve your problem",fg="red",height=1,width=60,compound=CENTER)
    l.place(x=286,y=530)
    l.config(font=("Courier", 20,"bold italic"))
    l=Label(screen,text="And we also ensure to avoid such mistakes in the future",fg="red",height=1,width=60,compound=CENTER)
    l.place(x=286,y=560)
    l.config(font=("Courier", 20,"bold italic"))
    f=open("sem2 python/database","rb")
    l=[]
    while True:
        try:
            data=pickle.load(f)
            l.append(data)
        except EOFError:
            break
    f.close()
    e = datetime.datetime.now()
    for i in l:
        if i["name"]==n:
            i["complaint"]="Yes"
            comp_l=[]
            comp_l.append(e.day)
            comp_l.append(e.month)
            comp_l.append(e.year)
            comp_l.append(e.hour)
            comp_l.append(e.minute)
            i["complaint_time"]=comp_l
    f=open("sem2 python/database","wb")
    for i in l:
        pickle.dump(i,f)
    f.close()
    
def complaint():
    Quit()
    global screen
    screen = Tk()
    gif2= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/adminbg.png')
    gif3= PhotoImage(file='sem2 python/BG3.gif')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Label2=Label(canvas,height=30,width=370,image=gif2,text = "WELCOME TO THE COMPLAIN SECTOR",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.5,rely=0.02,anchor='center')
    Label2=Label(canvas,height=30,width=400,image=gif3,text = "Are you sure?",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.5,rely=0.2,anchor='center')
    Label2=Label(canvas,height=30,width=400,image=gif3,text = "Do you want to place a complaint",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.5,rely=0.24,anchor='center')
    Q=Button(screen,image=gif2,compound=CENTER,text='YES',height= 40,width=180,command=sorry)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=0.46, rely=0.34, anchor="ne")
    Q=Button(screen,image=gif2,compound=CENTER,text='NO',height= 40,width=180,command=noproblem)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=0.67, rely=0.34, anchor="ne")
    Q=Button(screen,image=gif2,compound=CENTER,text='BACK',height= 40,width=180,command=back2)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=1.0, y=0, anchor="ne")
    canvas.pack()
    screen.mainloop()
    
def placed():
    global log_deli
    e = datetime.datetime.now()
    l=Label(screen,text="ORDER PLACED SUCCESSFULLY",fg="green",height=1,width=30,compound=CENTER)
    l.place(x=510,y=580)
    l.config(font=("Courier", 20,"bold italic"))
    l1=Label(screen,text="Order will be delivered on {}-{}-{}".format(e.day+1,e.month,e.year),fg="green",height=1,width=40,compound=CENTER)
    l1.place(x=440,y=710)
    l1.config(font=("Courier", 20,"bold italic"))
    l1=Label(screen,text="To the address {}.".format(datas["address"]),fg="green",height=1,width=40,compound=CENTER)
    l1.place(x=440,y=740)
    l1.config(font=("Courier", 20,"bold italic"))
    Label2=Label(screen,fg="red",width=400,text = "THANK YOU",font=("Courier", 25,"bold italic"),compound='center')
    Label2.place(relx=0.49,rely=0.45,anchor='center')
    f=open("sem2 python/database","rb")
    l=[]
    while True:
        try:
            data=pickle.load(f)
            l.append(data)
        except EOFError:
            break
    f.close()
    for i in l:
        if i["name"]==n:
            ord_ti=[]
            ord_ti.append(e.day)
            ord_ti.append(e.month)
            ord_ti.append(e.year)
            i["order_time"]=ord_ti
            deli=[]
            deli.append(e.day+1)
            deli.append(e.month)
            deli.append(e.year)
            i["delivery"]=deli
            log_deli=i
            i["booking_id"]=random.randint(100000,999999)
            l1=Label(screen,text="Your booking id is : {}".format(i["booking_id"]),fg="green",height=1,width=40,compound=CENTER)
            l1.place(x=440,y=670)
            l1.config(font=("Courier", 20,"bold italic"))
            break
    f=open("sem2 python/database","wb")
    for i in l:
        pickle.dump(i,f)
    f.close()
    
def logged_in():
    Quit()
    global screen
    global n
    screen = Tk()
    gif= PhotoImage(file='sem2 python/welcome.png')
    gif2= PhotoImage(file='sem2 python/BG3.gif')
    gif4= PhotoImage(file='sem2 python/BG2.gif')
    gif3= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/adminbg.png')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Head=Canvas(screen,bd=2,height=116,width=400,relief=RIDGE)
    Head.create_image(1, 1, image=gif, anchor=NW)
    Head.place(x=550,y=20)
    d=log_deli
    n=log_name
    Label2=Label(canvas,height=30,width=400,image=gif3,text ="Mr./Mrs. {}".format(n),font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.49,rely=0.19,anchor='center')
    if d=="No orders placed":
        Label2=Label(canvas,height=30,width=400,image=gif2,fg="red",text = "NO ORDERS PLACED",font=("Courier", 25,"bold italic"),compound='center')
        Label2.place(relx=0.5,rely=0.45,anchor='center')
        Q1=Button(screen,image=gif3,compound=CENTER,text='Place Order',height= 40,width=180,command=placed)
        Q1.config(font=("Courier", 20,"bold italic"))
        Q1.place(relx=0.56, rely=0.6, anchor="ne")
        Q=Button(screen,image=gif3,compound=CENTER,text='File a complaint',height= 40,width=300,command=complaint)
        Q.config(font=("Courier", 20,"bold italic"))
        Q.place(relx=0.6, rely=0.72, anchor="ne")
    elif d=="Delivered":
        Label2=Label(canvas,height=30,width=810,image=gif4,fg="green",text = "Your last order was delivered successfully",font=("Courier", 25,"bold italic"),compound='center')
        Label2.place(relx=0.5,rely=0.45,anchor='center')
        Q1=Button(screen,image=gif3,compound=CENTER,text='Place Order',height= 40,width=180,command=placed)
        Q1.config(font=("Courier", 20,"bold italic"))
        Q1.place(relx=0.56, rely=0.6, anchor="ne")
        Q=Button(screen,image=gif3,compound=CENTER,text='File a complaint',height= 40,width=300,command=complaint)
        Q.config(font=("Courier", 20,"bold italic"))
        Q.place(relx=0.6, rely=0.72, anchor="ne")
    else:
        
        mob=log_num
        e = datetime.datetime.now()
        f=open("sem2 python/database","rb")
        l=[]
        while True:
            try:
                data=pickle.load(f)
                l.append(data)
            except EOFError:
                break
        f.close()
        for i in l:
            if mob in i.keys():
                if e.day==i["delivery"][0] and e.month==i["delivery"][1] and e.year==i["delivery"][2]:
                    Label2=Label(canvas,height=30,width=800,image=gif4,fg="green",text = "Your order will be delivered soon today",font=("Courier", 25,"bold italic"),compound='center')
                    Label2.place(relx=0.5,rely=0.80,anchor='center')
                elif int(i["order_time"][0])+1<i["delivery"][0] or int(i["order_time"][1])+1<i["delivery"][1] or int(i["order_time"][2])+1<i["delivery"][2]:
                    Label2=Label(canvas,height=30,width=800,image=gif4,fg="red",text = "Sorry for the delay",font=("Courier", 25,"bold italic"),compound='center')
                    Label2.place(relx=0.5,rely=0.80,anchor='center')
                Label3=Label(canvas,height=30,width=250,image=gif2,text = "Delivery Date :",font=("Courier", 15,"bold italic"),compound='center')
                Label3.place(relx=0.4,rely=0.52,anchor='center')
                Label4=Label(canvas,height=30,width=250,image=gif2,text ="{}-{}-{}".format(i["delivery"][0],i["delivery"][1],i["delivery"][2]),font=("Courier", 15,"bold italic"),compound='center')
                Label4.place(relx=0.6,rely=0.52,anchor='center')
                Label3=Label(canvas,height=30,width=250,image=gif2,text = "Address :",font=("Courier", 15,"bold italic"),compound='center')
                Label3.place(relx=0.4,rely=0.62,anchor='center')
                Label4=Label(canvas,height=30,width=250,image=gif2,text =i["address"],font=("Courier", 15,"bold italic"),compound='center')
                Label4.place(relx=0.6,rely=0.62,anchor='center')
                Label3=Label(canvas,height=30,width=250,image=gif2,text = "Mobile number :",font=("Courier", 15,"bold italic"),compound='center')
                Label3.place(relx=0.4,rely=0.32,anchor='center')
                Label4=Label(canvas,height=30,width=250,image=gif2,text = mob,font=("Courier", 15,"bold italic"),compound='center')
                Label4.place(relx=0.6,rely=0.32,anchor='center')
                Label5=Label(canvas,height=30,width=250,image=gif2,text = "Booking id :",font=("Courier", 15,"bold italic"),compound='center')
                Label5.place(relx=0.4,rely=0.42,anchor='center')
                Label6=Label(canvas,height=30,width=250,image=gif2,text = i["booking_id"],font=("Courier", 15,"bold italic"),compound='center')
                Label6.place(relx=0.6,rely=0.42,anchor='center')
            
    f=open("sem2 python/database","rb")
    l=[]
    while True:
        try:
            data=pickle.load(f)
            l.append(data)
        except EOFError:
            break
    f.close()
    flag=False
    for i in l:
        if i["name"]==n and "complaint" in i.keys():
            if i["complaint"]=="No":
                Q=Button(screen,image=gif3,compound=CENTER,text='File a complaint',height= 40,width=300,command=complaint)
                Q.config(font=("Courier", 20,"bold italic"))
                Q.place(relx=0.6, rely=0.72, anchor="ne")
                flag=True
                break
    if flag==False:
        Q=Button(screen,image=gif3,compound=CENTER,text='My filed complaint',height= 40,width=300,command=my_complaint)
        Q.config(font=("Courier", 20,"bold italic"))
        Q.place(relx=0.6, rely=0.72, anchor="ne")
    Q=Button(screen,image=gif3,compound=CENTER,text='BACK',height= 40,width=180,command=back)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=1.0, y=0, anchor="ne")
    canvas.pack()
    screen.mainloop()
    
def login_verify():
    #Quit()
    global screen
    global log_name
    global log_deli
    global log_num
    global datas
    mobile1 = number.get()
    log_pwd1 = pwd.get()
    mobile.delete(0, END)
    log_pwd.delete(0, END)
    if mobile1!="" and log_pwd1!="":
        if len(mobile1)==10:
            flag=False
            f=open("sem2 python/database","rb")
            l=[]
            while True:
                try:
                    data=pickle.load(f)
                    l.append(data)
                except EOFError:
                    break
            f.close()
            for datas in l:
                if mobile1 in datas.keys():
                    if datas[mobile1]==log_pwd1:
                        flag=True
                        break
                    else:
                        l=Label(screen,text="INVALID PASSWORD",fg="red",height=1,width=30,compound=CENTER)
                        l.place(x=525,y=700)
                        l.config(font=("Courier", 20,"bold italic"))
                        flag="no"
            if flag==False:
                l=Label(screen,text="MOBILE NUMBER NOT FOUND",fg="red",height=1,width=30,compound=CENTER)
                l.place(x=525,y=700)
                l.config(font=("Courier", 20,"bold italic"))
            elif flag==True:
                log_name=datas["name"]
                log_deli=datas["delivery"]
                log_num=mobile1
                logged_in()
        else:
            l=Label(screen,text="ENTER VALID MOBILE NUMBER",fg="red",height=1,width=30,compound=CENTER)
            l.place(x=525,y=700)
            l.config(font=("Courier", 20,"bold italic"))
    else:
        l=Label(screen,text="PLEASE FILL THE DETAILS",fg="red",height=1,width=30,compound=CENTER)
        l.place(x=525,y=700)
        l.config(font=("Courier", 20,"bold italic"))
        
def second_screen():
    Quit()
    global screen
    global mobile
    global number
    global pwd
    global log_pwd
    screen = Tk()
    number=StringVar()
    pwd=StringVar()
    gif2= PhotoImage(file='sem2 python/BG3.gif')
    bg=PhotoImage(file='sem2 python/secondbg.png')
    gif4= PhotoImage(file='sem2 python/A.png')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Q=Button(screen,image=gif2,compound=CENTER,text='BACK',height= 40,width=180,command=back)
    Q.config(font=("Courier", 20,"bold italic"))
    Q.place(relx=1.0, y=0, anchor="ne")
    Label2=Label(canvas,height=30,width=250,image=gif2,text = "LOGIN Page",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.5,rely=0.02,anchor='center')
    Label3=Label(canvas,height=30,width=250,image=gif2,text = "Mobile number",font=("Courier", 15,"bold italic"),compound='center')
    Label3.place(relx=0.4,rely=0.32,anchor='center')
    mobile=Entry(canvas,textvariable = number,font=("Courier", 20,"bold italic"),width=18)
    mobile.place(x=755,y=260)
    Label4=Label(canvas,height=30,width=250,image=gif2,text = "Password",font=("Courier", 15,"bold italic"),compound='center')
    Label4.place(relx=0.4,rely=0.47,anchor='center')
    log_pwd=Entry(canvas,textvariable = pwd,font=("Courier", 20,"bold italic"),width=18,show="*")
    log_pwd.place(x=755,y=390)
    B2=Button(screen,image=gif4,compound=CENTER,text='Login',height= 30,width=180,command=login_verify)
    B2.config(font=("Courier", 20,"bold italic"))
    B2.place(x=671,y=460)
    Label1=Label(canvas,height=30,width=270,image=gif2,text = "Don't have an account?",font=("Courier", 15,"bold italic"),compound='center')
    Label1.place(relx=0.5,rely=0.68,anchor='center')
    B1=Button(screen,image=gif4,compound=CENTER,text='REGISTER',height= 30,width=180,command=register)
    B1.config(font=("Courier", 20,"bold italic"))
    B1.place(x=671,y=620)
    canvas.pack()
    screen.mainloop()


def tq22():
    Quit()
    global screen
    screen = Tk()
    gif2= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/service.png')
    star=PhotoImage(file='sem2 python/star.png')
    star1=PhotoImage(file='sem2 python/star1.png')
    q= PhotoImage(file='sem2 python/quit.gif')
    gif4= PhotoImage(file='sem2 python/A.png')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Label2=Label(canvas,height=30,width=370,image=gif2,text = "THANK YOU",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.49,rely=0.02,anchor='center')
    l1=Label(screen,text="We will be waiting...",fg="green",bg="yellow",height=1,width=60,compound=CENTER)
    l1.place(x=286,y=200)
    l1.config(font=("Courier", 20,"bold italic"))
    l1=Label(screen,text="To SERVE YOU",fg="green",bg="yellow",height=1,width=60,compound=CENTER)
    l1.place(x=286,y=230)
    l1.config(font=("Courier", 20,"bold italic"))
    Q=Button(screen,image= q,command=Quit)
    Q.place(relx=1.0, y=0, anchor="ne")
    Q=Button(screen,image= star1,command=tq11)
    Q.place(relx=0.44, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq22)
    Q.place(relx=0.47, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq33)
    Q.place(relx=0.50, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq44)
    Q.place(relx=0.53, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq55)
    Q.place(relx=0.56, rely=0.5, anchor="ne")
    canvas.pack()
    screen.mainloop()
def tq33():
    Quit()
    global screen
    screen = Tk()
    gif2= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/service.png')
    star=PhotoImage(file='sem2 python/star.png')
    q= PhotoImage(file='sem2 python/quit.gif')
    star1=PhotoImage(file='sem2 python/star1.png')
    gif4= PhotoImage(file='sem2 python/A.png')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Label2=Label(canvas,height=30,width=370,image=gif2,text = "THANK YOU",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.49,rely=0.02,anchor='center')
    l1=Label(screen,text="We will be waiting...",fg="green",bg="yellow",height=1,width=60,compound=CENTER)
    l1.place(x=286,y=200)
    l1.config(font=("Courier", 20,"bold italic"))
    l1=Label(screen,text="To SERVE YOU",fg="green",bg="yellow",height=1,width=60,compound=CENTER)
    l1.place(x=286,y=230)
    l1.config(font=("Courier", 20,"bold italic"))
    Q=Button(screen,image= q,command=Quit)
    Q.place(relx=1.0, y=0, anchor="ne")
    Q=Button(screen,image= star1,command=tq11)
    Q.place(relx=0.44, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq22)
    Q.place(relx=0.47, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq33)
    Q.place(relx=0.50, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq44)
    Q.place(relx=0.53, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq55)
    Q.place(relx=0.56, rely=0.5, anchor="ne")
    canvas.pack()
    screen.mainloop()
def tq44():
    Quit()
    global screen
    screen = Tk()
    gif2= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/service.png')
    star=PhotoImage(file='sem2 python/star.png')
    star1=PhotoImage(file='sem2 python/star1.png')
    q= PhotoImage(file='sem2 python/quit.gif')
    gif4= PhotoImage(file='sem2 python/A.png')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Label2=Label(canvas,height=30,width=370,image=gif2,text = "THANK YOU",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.49,rely=0.02,anchor='center')
    l1=Label(screen,text="We will be waiting...",fg="green",bg="yellow",height=1,width=60,compound=CENTER)
    l1.place(x=286,y=200)
    l1.config(font=("Courier", 20,"bold italic"))
    l1=Label(screen,text="To SERVE YOU",fg="green",bg="yellow",height=1,width=60,compound=CENTER)
    l1.place(x=286,y=230)
    l1.config(font=("Courier", 20,"bold italic"))
    Q=Button(screen,image= q,command=Quit)
    Q.place(relx=1.0, y=0, anchor="ne")
    Q=Button(screen,image= star1,command=tq11)
    Q.place(relx=0.44, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq22)
    Q.place(relx=0.47, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq33)
    Q.place(relx=0.50, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq44)
    Q.place(relx=0.53, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq55)
    Q.place(relx=0.56, rely=0.5, anchor="ne")
    canvas.pack()
    screen.mainloop()
def tq55():
    Quit()
    global screen
    screen = Tk()
    gif2= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/service.png')
    star=PhotoImage(file='sem2 python/star.png')
    star1=PhotoImage(file='sem2 python/star1.png')
    gif4= PhotoImage(file='sem2 python/A.png')
    q= PhotoImage(file='sem2 python/quit.gif')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Label2=Label(canvas,height=30,width=370,image=gif2,text = "THANK YOU",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.49,rely=0.02,anchor='center')
    l1=Label(screen,text="We will be waiting...",fg="green",bg="yellow",height=1,width=60,compound=CENTER)
    l1.place(x=286,y=200)
    l1.config(font=("Courier", 20,"bold italic"))
    l1=Label(screen,text="To SERVE YOU",fg="green",bg="yellow",height=1,width=60,compound=CENTER)
    l1.place(x=286,y=230)
    l1.config(font=("Courier", 20,"bold italic"))
    Q=Button(screen,image= q,command=Quit)
    Q.place(relx=1.0, y=0, anchor="ne")
    Q=Button(screen,image= star1,command=tq11)
    Q.place(relx=0.44, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq22)
    Q.place(relx=0.47, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq33)
    Q.place(relx=0.50, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq44)
    Q.place(relx=0.53, rely=0.5, anchor="ne")
    Q=Button(screen,image= star1,command=tq55)
    Q.place(relx=0.56, rely=0.5, anchor="ne")
    canvas.pack()
    screen.mainloop()
def tq11():
    Quit()
    global screen
    screen = Tk()
    gif2= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/service.png')
    star=PhotoImage(file='sem2 python/star.png')
    star1=PhotoImage(file='sem2 python/star1.png')
    gif4= PhotoImage(file='sem2 python/A.png')
    q= PhotoImage(file='sem2 python/quit.gif')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Label2=Label(canvas,height=30,width=370,image=gif2,text = "THANK YOU",font=("Courier", 15,"bold italic"),compound='center')
    Label2.place(relx=0.49,rely=0.02,anchor='center')
    l1=Label(screen,text="We will be waiting...",bg="yellow",fg="green",height=1,width=60,compound=CENTER)
    l1.place(x=286,y=200)
    l1.config(font=("Courier", 20,"bold italic"))
    l1=Label(screen,text="To SERVE YOU",fg="green",bg="yellow",height=1,width=60,compound=CENTER)
    l1.place(x=286,y=230)
    l1.config(font=("Courier", 20,"bold italic"))
    Q=Button(screen,image= q,command=Quit)
    Q.place(relx=1.0, y=0, anchor="ne")
    Q=Button(screen,image= star1,command=tq11)
    Q.place(relx=0.44, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq22)
    Q.place(relx=0.47, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq33)
    Q.place(relx=0.50, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq44)
    Q.place(relx=0.53, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq55)
    Q.place(relx=0.56, rely=0.5, anchor="ne")
    canvas.pack()
    screen.mainloop()    
def Quit1():
    Quit()
    global screen
    screen = Tk()
    gif2= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/service.png')
    star=PhotoImage(file='sem2 python/star.png')
    gif3= PhotoImage(file='sem2 python/BG3.gif')
    q= PhotoImage(file='sem2 python/quit.gif')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)
    #bg
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    Q=Button(screen,image= q,command=Quit1)
    Q.place(relx=1.0, y=0, anchor="ne")
    l1=Label(screen,text="THANK YOU",fg="green",bg="yellow",height=1,width=60,compound=CENTER)
    l1.place(x=286,y=200)
    l1.config(font=("Courier", 20,"bold italic"))
    l1=Label(screen,text="Please rate the APP",fg="green",bg="yellow",height=1,width=60,compound=CENTER)
    l1.place(x=286,y=230)
    l1.config(font=("Courier", 20,"bold italic"))
    Q=Button(screen,image= star,command=tq11)
    Q.place(relx=0.44, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq22)
    Q.place(relx=0.47, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq33)
    Q.place(relx=0.5, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq44)
    Q.place(relx=0.53, rely=0.5, anchor="ne")
    Q=Button(screen,image= star,command=tq55)
    Q.place(relx=0.56, rely=0.5, anchor="ne")
    canvas.pack()
    screen.mainloop()
def main_screen():
    global screen
    screen = Tk()
    gif= PhotoImage(file='sem2 python/welcome.png')
    gif2= PhotoImage(file='sem2 python/BG3.gif')
    #gif3= PhotoImage(file='sem2 python/BG2.gif')
    gif4= PhotoImage(file='sem2 python/A.png')
    bg=PhotoImage(file='sem2 python/bgnew.png')
    img=PhotoImage(file='sem2 python/lpg1.png')
    q= PhotoImage(file='sem2 python/quit.gif')
    screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))
    Width, Height = screen.winfo_screenwidth(), screen.winfo_screenheight()
    screen.overrideredirect(True)


    #background
    canvas = Canvas(screen,bd=10,height=Height,width=Width,relief=RIDGE)
    canvas.create_image(1, 1, image=bg, anchor=NW)
    canvas.create_image(688, 333, image=img, anchor=NW)
    #continue
    B=Button(screen,image=gif4,compound=CENTER,text='CONTINUE',height= 40,width=200,command=second_screen)
    B.config(font=("Courier", 20,"bold italic"))
    B.place(x=669,y=680)
    #welcome
    Head=Canvas(screen,bd=2,height=116,width=400,relief=RIDGE)
    Head.create_image(1, 1, image=gif, anchor=NW)
    Head.place(x=550,y=20)
    #quit
    Q=Button(screen,image= q,command=Quit1)
    Q.place(relx=1.0, y=0, anchor="ne")
    #admin login
    Label1=Label(canvas,height=30,width=150,image=gif2,text = "Admin Login?",font=("Gothic", 15,"bold italic"),compound='center')
    Label1.place(relx=0.85,rely=0.15,anchor='center')
    B1=Button(screen,image=gif4,compound=CENTER,text='ENTER',height= 30,width=120,command=admin_screen)
    B1.config(font=("Courier", 20,"bold italic"))
    B1.place(x=1241,y=170)
    canvas.pack()
    screen.mainloop()

main_screen()


