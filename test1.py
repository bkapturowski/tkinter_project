from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from tkinter.ttk import Combobox
import openpyxl, xlrd
from openpyxl import Workbook
import pathlib


background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

root = Tk()
root.title("Student Registration System")
root.geometry("1250x700+210+100")
root.config(bg=background)

file = pathlib.Path('Student_data')
if file.exists():
    pass
else:
    file = Workbook()
    sheet = file.active
    sheet['A1'] = "Registration No."
    sheet['B1'] = "Name"
    sheet['C1'] = "Class"
    sheet['D1'] = "Gender"
    sheet['E1'] = "DOB"
    sheet['F1'] = "Date of Registration"
    sheet['G1'] = "Religion"
    sheet['H1'] = "Skill"
    sheet['I1'] = "Father Name"
    sheet['J1'] = "Mother Name"
    sheet['K1'] = "Fathers Occupation"
    sheet['L1'] = "Mothers Occupation"

    file.save('Student_data')

#top frames
Label(root, text="Email: kaptur2601@gmail.com", width=10, height=3, bg="#f0687c", anchor='e').pack(side=TOP, fill=X)
Label(root, text="STUDENT REGISTRATION", width=10, height=2, bg="#f36464",fg='#fff', font='arial 20 bold').pack(side=TOP, fill=X)

#search box to update

Search = StringVar()
Entry(root, textvariable=Search,width=15,bd=2,font="arial 20").place(x=820,y=70)
iamgeicon3 = PhotoImage(file="Images/search.png")
Srch = Button(root,text='Search', compound=LEFT, image=iamgeicon3,width=123,bg='#68ddfa', font="arial 13 bold")
Srch.place(x=1060, y=66)

imageicon4 = PhotoImage(file="Images/Layer 4.png")
Update_button = Button(root,image=imageicon4, bg = "#c36464")
Update_button.place(x=10,y=64)

#Registration and Date

Label(root, text="Registration No:", font="arial 13", fg=framebg,bg=background).place(x=30,y=150)
Label(root, text="Date:", font="arial 13", fg=framebg,bg=background).place(x=500,y=150)

Registration = StringVar()
Date = StringVar()


reg_entry = Entry(root,textvariable=Registration,width=15,font="arial 10")
reg_entry.place(x=160,y=150)

#registratio_no()

today = date.today()
d1 = today.strftime("%d/%m/%Y")
date_entry = Entry(root,textvariable=Date,width=15,font="arial 10")
date_entry.place(x=550,y=150)

Date.set(d1)


#Student details

obj=LabelFrame(root, text="Student's Details", font=20,bd=2,width=900,bg=framebg,fg=framefg,height=250,relief=GROOVE)
obj.place(x=30,y=200)

Label(obj,text="Full Name:", font="arial 13",bg=framebg,fg=framefg).place(x=30,y=50)
Label(obj,text="Date of Birth:", font="arial 13",bg=framebg,fg=framefg).place(x=30,y=100)
Label(obj,text="Gender:", font="arial 13",bg=framebg,fg=framefg).place(x=30,y=150)

Label(obj,text="Class:", font="arial 13",bg=framebg,fg=framefg).place(x=500,y=50)
Label(obj,text="Religion:", font="arial 13",bg=framebg,fg=framefg).place(x=500,y=100)
Label(obj,text="Skills:", font="arial 13",bg=framebg,fg=framefg).place(x=500,y=150)

Name = StringVar()
name_entry = Entry(obj,textvariable=Name,width=20,font="arial 10")
name_entry.place(x=160,y=50)

radio = IntVar()

#Parents details

obj2=LabelFrame(root, text="Parent's Details", font=20,bd=2,width=900,bg=framebg,fg=framefg,height=220,relief=GROOVE)
obj2.place(x=30,y=470)

































root.mainloop()