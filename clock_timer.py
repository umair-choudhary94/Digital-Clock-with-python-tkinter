from tkinter import *
import time 
root = Tk()
root.geometry('600x200')
root.title('Clock-By Umair choudhary')
root.configure(bg='black')
# root.wm_iconbitmap('clock.ico')
root.minsize(600,200)#it is your Gui minsize
root.maxsize(700,200)#it is your Gui mazsize
def clock():
    hour = time.strftime('%I')# to get hours
    minute = time.strftime('%M')# to get minute 
    second = time.strftime('%S')# to get second
    am_pm = time.strftime('%p')# to get am and pm
    day = time.strftime('%A')# to get day
    time_zone = time.strftime('%Z')# to get time zone
    label.config(text=hour +":"+minute+":"+second +" "+am_pm)
    label.after(1000,clock)# 1000= 1second
    label2.config(text=time_zone+' | '+day)
label= Label(root,text="",bg='black',fg='green',font=('helvetica',50))
label.pack(pady=20)
label2= Label(root,text="",bg='black',fg='green',font=('helvetica',10))
label2.pack(fill=BOTH)

clock()
root.mainloop()