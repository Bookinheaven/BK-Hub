import tkinter as tk

main_window = tk.Tk()
main_window.geometry("600x600")

frame1 = tk.Frame()
frame2 = tk.Frame()

lable1 = tk.Label(master=frame1,text="Frame 1 Widgets 1")
#lable2 = tk.Label(master=frame1,text="Frame 1 Widgets 2")

lable1.pack()
#lable2.pack()


flable1 = tk.Label(master=frame2,text="Frame 2 Widgets 1")
flable2 = tk.Label(master=frame2,text="Frame 2 Widgets 2")

flable1.pack()
flable2.pack()

lable2 = tk.Label(master=frame1,text="Frame 1 Widgets 2")   #order won't change after swap
lable2.pack()

#frame1.pack()
frame2.pack()   #order changes after swap
frame1.pack()

main_window.mainloop()