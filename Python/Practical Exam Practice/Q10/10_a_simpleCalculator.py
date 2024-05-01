"""
Design following basic mathematic operations such as addition, subtraction, multiplication, and
division for the two given numbers (input from user).
"""

from tkinter import *

main = Tk()
main.title("Simple Calculator")
main.configure(background='lightgray')
# should add error handling for this -_-
def add():
    text3.set(int(text1.get()) + int(text2.get()))

def mul():
    text3.set(int(text1.get()) * int(text2.get()))

def div():
    text3.set(int(text1.get()) // int(text2.get()))

def sub():
    text3.set(int(text1.get()) - int(text2.get()))
def clear():
    text3.set('Result')

label1 = Label(master=main, text='Simple Calculator', font=('Arial', 30), bg='lightgray')
label1.grid(row=0, column=0, columnspan=4,padx=10, pady=10)

text1 = StringVar(value='NUMBER e.g 1337')
entry1 = Entry(master=main, textvariable=text1, font=('Arial', 14), justify='center', fg='lightgray')
entry1.grid(row=1, column=0,padx=20, pady=20, ipadx=40,ipady=10, columnspan=2)

text2 = IntVar(value='NUMBER e.g 2108')
entry2 = Entry(master=main, textvariable=text2, font=('Arial', 14), justify='center', fg='lightgray')
entry2.grid(row=1, column=2,padx=20, pady=20,ipadx=40,ipady=10, columnspan=2)

but1 = Button(master=main, text='+ Add', font=('Arial', 12), fg='white', bg='blue', command=add)
but1.grid(row=2, column=0,padx=20, pady=20,ipadx=40,ipady=10)

but2 = Button(master=main, text='- Subtract', font=('Arial', 12), fg='white', bg='blue', command=sub)
but2.grid(row=2, column=1,padx=20, pady=20,ipadx=40,ipady=10)

but3 = Button(master=main, text='/ Divide', font=('Arial', 12), fg='white', bg='blue', command=div)
but3.grid(row=2, column=2,padx=20, pady=20,ipadx=40,ipady=10)

but4 = Button(master=main, text='* Multiply', font=('Arial', 12), fg='white', bg='blue', command=mul)
but4.grid(row=2, column=3,padx=20, pady=20,ipadx=40,ipady=10)

text3 = StringVar(value='Result')
entry3 = Entry(master=main, textvariable=text3, font=('Arial', 14), fg='lightgray', state='disabled')
entry3.grid(row=3, column=0,padx=20, pady=20,ipadx=120,ipady=10, columnspan=3)

but5 = Button(master=main, text='Clear', font=('Arial', 12), fg='white', bg='red', command=clear)
but5.grid(row=3, column=3,padx=20, pady=20,ipadx=40,ipady=10)

main.mainloop()