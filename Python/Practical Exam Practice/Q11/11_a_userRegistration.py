"""
b Create GUI application to design a Registration form.
"""

from tkinter import *
from tkinter.ttk import Combobox

main = Tk()
main.title("Registration Form")
main.geometry("900x900")
label1 = Label(master=main, text='User Registration Form', font=('Arial', 25), fg='red')
label1.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

name_label = Label(master=main, text='Name', font=('Arial', 20), fg='blue')
name_label.grid(row=1, column=0, padx=10,pady=10)

gender_label = Label(master=main, text='Gender', font=('Arial', 20), fg='blue')
gender_label.grid(row=2, column=0, padx=10,pady=10)

country_label = Label(master=main, text='Country', font=('Arial', 20), fg='blue')
country_label.grid(row=3, column=0, padx=10,pady=10)

hobbie_label = Label(master=main, text='Hobbies', font=('Arial', 20), fg='blue')
hobbie_label.grid(row=4, column=0, padx=10,pady=10)

name = StringVar()
male = IntVar()
female = IntVar()
opt = StringVar()
name_entry = Entry(master=main, bg='gray', font=('Arial', 18), textvariable=name)
name_entry.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

male_radio = Radiobutton(master=main, text='Male', font=('Arial', 18), variable=male, value=0)
male_radio.grid(row=2, column=1, padx=5,pady=10)

female_radio = Radiobutton(master=main, text='Female', font=('Arial', 18), variable=female, value=1)
female_radio.grid(row=2, column=2, padx=5,pady=10)

op = Combobox(master=main, values=['India','Us','Japan'], textvariable=opt, font=('Arial', 14))
op.grid(row=3, column=1, columnspan=2, padx=10,pady=10)
# a = ['India','Us','Japan']
# op = OptionMenu(main, opt, *a)
# op.grid(row=3, column=1, columnspan=2, padx=10,pady=10)

che1 = StringVar(value=0)
che2 = StringVar(value=0)
che3 = StringVar(value=0)
che4 = StringVar(value=0)

check1 = Checkbutton(main, text="Volleyball", onvalue=1, offvalue=0,font=('Arial', 14), variable=che1)
check1.grid(row=4, column=1, padx=10,pady=10)

check2 = Checkbutton(main, text="PC Games", onvalue=1, offvalue=0,font=('Arial', 14), variable=che2)
check2.grid(row=4, column=2, padx=10,pady=10)

check3 = Checkbutton(main, text="Football", onvalue=1, offvalue=0,font=('Arial', 14), variable=che3)
check3.grid(row=5, column=1, padx=10,pady=10)

check4 = Checkbutton(main, text="Videography", onvalue=1, offvalue=0,font=('Arial', 14), variable=che4)
check4.grid(row=5, column=2, padx=10,pady=10)

def buttonclick():
      x = [name, male, female, opt, che1, che2,che3,che4]
      for k in x: 
          print(k.get())
button = Button(master=main, text='Submit', font=('Arial', 16), fg='white',bg='black', command=buttonclick)
button.grid(row=6, column=0,padx=10, pady=10)
main.mainloop()