import tkinter as tk

main_window = tk.Tk()
"""
#pack()
frame1 = tk.Frame(master=main_window, width=100, height=100, bg="red")
#frame1.pack()
#frame1.pack(fill=tk.X)
#frame1.pack(fill=tk.Y, side=tk.LEFT)
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=main_window, width=50, height=50, bg="yellow")
#frame2.pack()
#frame2.pack(fill=tk.X)
#frame2.pack(fill=tk.Y, side=tk.LEFT)
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=main_window, width=25, height=25, bg="blue")
#frame3.pack()
#frame3.pack(fill=tk.X)
#frame3.pack(fill=tk.Y, side=tk.LEFT)
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
"""

"""
#place()
frame = tk.Frame(master=main_window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
label2.place(x=75, y=75)
"""

#grid()
"""
for i in range(3):
    main_window.columnconfigure(i, weight=1, minsize=75)
    main_window.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        frame = tk.Frame(
            master=main_window,
            relief=tk.RAISED,
            borderwidth=1
        )
        #frame.grid(row=i, column=j)
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        #label.pack()
        label.pack(padx=5, pady=5)
"""
main_window.columnconfigure(0, minsize=250)
main_window.rowconfigure([0, 1], minsize=100)

"""
Sticky
North - n
South - s
East - e
West - w
"""

"""
label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky="ne")

label2 = tk.Label(text="B")
label2.grid(row=1, column=0, sticky="sw")
"""
"""
label1 = tk.Label(text="1", bg="black", fg="white")
label2 = tk.Label(text="2", bg="black", fg="white")
label3 = tk.Label(text="3", bg="black", fg="white")
label4 = tk.Label(text="4", bg="black", fg="white")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky="ew")
label3.grid(row=0, column=2, sticky="ns")
label4.grid(row=0, column=3, sticky="nsew")
"""

"""
.grid()	       |    .pack()
sticky="ns"	   |    fill=tk.Y
sticky="ew"	   |    fill=tk.X
sticky="nsew"  |	fill=tk.BOTH
""" 
#.grid() is a powerful geometry manager. It’s often easier to understand than .pack() and is much more flexible than .place(). 
#When you’re creating new Tkinter applications, you should consider using .grid() as your primary geometry manager.

main_window.mainloop()  


