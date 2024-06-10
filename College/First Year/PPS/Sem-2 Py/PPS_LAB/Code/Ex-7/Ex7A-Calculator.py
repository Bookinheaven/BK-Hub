#Create a GUI application to design a simple calculator or a convertor as given below.
from tkinter import *

main = Tk()
main.geometry("400x400")

def add():
    var1 = int(labl2_var.get())
    var2 = int(labl3_var.get())
    result_var = var1+var2
    entr3.delete(0, END)
    entr3.insert(0, result_var)

def sub():
    var1 = int(labl2_var.get())
    var2 = int(labl3_var.get())
    result_var = var1-var2
    entr3.delete(0, END)
    entr3.insert(0, result_var)

def mul():
    var1 = int(labl2_var.get())
    var2 = int(labl3_var.get())
    result_var = var1*var2
    entr3.delete(0, END)
    entr3.insert(0, result_var)
 
def div():
    var1 = int(labl2_var.get())
    var2 = int(labl3_var.get())
    try:
        result_var = var1/var2
    except ZeroDivisionError:
        print("Error /0")
    else:
        entr3.delete(0, END)
        entr3.insert(0, result_var)


labl1 = Label(master=main, text="Calculator", font=("Arial",26))
labl1.grid(row=0, column=0,padx=2,pady=10)

Frame1 = Frame(master=main)
Frame1.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

labl2 = Label(master=Frame1, text="Type Value 1:", font=("Arial",13))
labl2.grid(row=1, column=0,padx=20,pady=5)

labl3 = Label(master=Frame1, text="Type Value 2:", font=("Arial",13))
labl3.grid(row=2, column=0,padx=20,pady=5)

labl2_var = StringVar()
entr1 = Entry(master=Frame1, textvariable=labl2_var)
entr1.grid(row=1, column=1,padx=10,pady=5)

labl3_var = StringVar()
entr2 = Entry(master=Frame1, textvariable=labl3_var)
entr2.grid(row=2, column=1,padx=10,pady=5)
Frame1.rowconfigure(3, weight=1)
Frame2 = Frame(master=Frame1)
Frame2.grid(row=3, column=1, sticky='nsew', padx=10, pady=10)

but1 = Button(master=Frame2, text='+',bg='green', fg='white', width=3, height=1, command=add)
but2 = Button(master=Frame2, text='-',bg='green', fg='white', width=3, height=1, command=sub)
but3 = Button(master=Frame2, text='x',bg='green', fg='white', width=3, height=1, command=mul)
but4 = Button(master=Frame2, text='/',bg='green', fg='white', width=3, height=1, command=div)

but1.grid(row=0, column=0,padx=(20,5),pady=5)
but2.grid(row=0, column=1,padx=5,pady=5)
but3.grid(row=0, column=2,padx=5,pady=5)
but4.grid(row=0, column=3,padx=5,pady=5)

res = Label(master=Frame1, text="Result:", font=("Arial",13))
res.grid(row=4, column=0,padx=20,pady=5)

entr3 = Entry(master=Frame1)
entr3.grid(row=4, column=1,padx=10,pady=5)

main.mainloop()