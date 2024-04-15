from tkinter import messagebox

def close_window(event, app):
    confirmed = messagebox.askokcancel("Confirm Close", "Do you want to close the app?")
    if confirmed:
        app.destroy()
def center_screen(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height= window.winfo_screenheight()
    x_coordinate = int((screen_width)/2 - (width / 2))
    y_coordinate = int((screen_height)/2 - (height / 2))
    window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")
