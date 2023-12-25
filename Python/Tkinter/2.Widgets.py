import tkinter as tk 
main_window = tk.Tk()
main_window.geometry("600x600")
#Label 
label = tk.Label(
    main_window, 
    text="This is a Label",
    foreground="white",
    background="#B64027",
    width=40,
    height=20
    )
label.pack()

#Buttton 
button = tk.Button(
    text="I'm Not A Button",
    width=25,
    height=5,
    background="white",
    foreground="#B64027"
)
button.pack()

#Entry
entry = tk.Entry(
    foreground="yellow",
    background="blue",
    width=50,
)
entry.pack()

#Input in entry
def datain():
    #Normal Data Entry
    data = entry.get()
    print(f"Data In: {data}")
    
    #Delete
    entry.delete(0)
    data = entry.get()
    print(f"Data Deleted: {data}")

    #Delete Multiple
    entry.delete(0, 4)
    data = entry.get()
    print(f"Multiple Data Deleted: {data}")

    #Delete End
    entry.delete(0, tk.END)
    data = entry.get()
    print(f"End Data Deleted: {data}")
    
    #Insert
    entry.insert(0, "Hello ")
    data = entry.get()
    print(f"Data Inserted: {data}")



button1 = tk.Button(
    text="Check",
    width=15,
    height=5,
    background="yellow",
    foreground="blue",
    command=datain
)
button1.pack()

tk.mainloop()