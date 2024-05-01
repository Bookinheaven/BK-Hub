from tkinter import *
from tkinter.ttk import Combobox
main = Tk()
main.geometry("500x300")
main.title("Registration Form")
main.columnconfigure(0, weight=1)

title_label = Label(master=main, text="Registration Form", font=("Arial",20))
title_label.grid(row=0, column=0,padx=3,pady=2)

full_name_label = Label(master=main, text="Full name", font=("Arial",16))
full_name_label.grid(row=1, column=0,padx=10, pady=3, sticky='w')
labl2 = Label(master=main, text="Email", font=("Arial",16))
labl2.grid(row=2, column=0,padx=10, pady=3, sticky='w')
labl3 = Label(master=main, text="Gender", font=("Arial",16))
labl3.grid(row=3, column=0,padx=10, pady=3, sticky='w')
labl4 = Label(master=main, text="Country", font=("Arial",16))
labl4.grid(row=4, column=0,padx=10, pady=3, sticky='w')
labl5 = Label(master=main, text="Programming", font=("Arial",16))
labl5.grid(row=6, column=0,padx=10, pady=3, sticky='w')

full_name_entry_var = StringVar()
full_name_entry = Entry(master=main, textvariable=full_name_entry_var, width=30)
full_name_entry.grid(row=1, column=0,padx=40, pady=5)

email_entry_var = StringVar()
email_entry = Entry(master=main, textvariable=email_entry_var, width=30)
email_entry.grid(row=2, column=0,padx=40, pady=5)

gender_var = StringVar(value="Male")
male_radio = Radiobutton(master=main, text="Male", variable=gender_var, value="Male")
male_radio.grid(row=3, column=0, padx=(30,130), pady=5, sticky='s')
female_radio = Radiobutton(master=main, text="Female", variable=gender_var, value="Female")
female_radio.grid(row=3, column=0, padx=(100,70), pady=5, sticky='s')

comb_var = StringVar(value="select your country")
com = Combobox(master=main, values=["select your country","India", "USA", "UK"], textvariable=comb_var)
com.grid(row=4, column=0, padx=40, pady=5)

lang_var_java = StringVar(value='off')
lang_var_python = StringVar(value='on')
java_check = Checkbutton(main, text="Java", variable=lang_var_java, onvalue="1", offvalue="0")
python_check = Checkbutton(main, text="Python", variable=lang_var_python, onvalue="1", offvalue="0")
java_check.grid(row=6, column=0, padx=(30,130), pady=5, sticky='s')
python_check.grid(row=6, column=0, padx=(100,70), pady=5, sticky='s')

def getvalues():
    full_name = full_name_entry_var.get()
    email = email_entry_var.get()
    gender = gender_var.get()
    country = comb_var.get()
    lang = ""
    if lang_var_java.get() == "1":
        lang = "Java"
    if lang_var_python.get() == "1":
        if lang:
            lang += ", Python"
        else:
            lang = "Python"

    print(f"Fullname: {full_name}\nEmail: {email}\nGender: {gender}\nCountry: {country}\nProgramming: {lang}")

sumbit = Button(master=main, text="Select", bg='red',fg= 'white', command=getvalues)
sumbit.grid(row=7, column=0, padx=40, pady=5)
main.mainloop()