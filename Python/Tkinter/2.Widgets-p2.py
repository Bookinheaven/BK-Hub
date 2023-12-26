import tkinter as tk 
main_window = tk.Tk()
main_window.geometry("600x600")

textbox = tk.Text()
textbox.pack()

def fun():
    #Get
    _1st_line = textbox.get("1.0","1.5")
    print(_1st_line)

    _2nd_line = textbox.get("2.0","2.5")
    print(_2nd_line)

    full_text = textbox.get("1.0", tk.END)
    print(full_text)

    #Delete
    textbox.delete("1.0")
    _1st_line = textbox.get("1.0", "1.4")
    print(_1st_line) #1.0 == 1 represents line and 0 represents its still on the first letter
    #near end there will be newline character

    textbox.delete("1.0")  
    _newline_ = textbox.get("1.0")
    print(_newline_)

    textbox.delete("1.0", tk.END)  
    full_text = textbox.get("1.0", tk.END)
    print(full_text)

    #Insert
    textbox.insert("1.0", "Hello")
    full_text = textbox.get("1.0", tk.END)
    print(full_text)

button = tk.Button(
    main_window, 
    text="Check",
    command=fun,
    foreground="red",
    background="white",
    width=20,
    height=10
    )
button.pack()


tk.mainloop()