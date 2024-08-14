import tkinter as tk
 
# basic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Division by zero."

def exponentiate(x, y):
    return x ** y

def modulus(x, y):
    return x % y

# Calculator class with Tkinter GUI
class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")
        self.resizable(False, False)
        
        self.current_input = ""
        self.result_var = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Display area
        display_frame = tk.Frame(self,bg='red')
        display_frame.pack(expand=False, fill="both")
        
        result_display = tk.Entry(display_frame, textvariable=self.result_var, font=("Arial", 38), borderwidth=2)
        result_display.grid(row=0, column=0, sticky='nsew')
        
        # Buttons
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(expand=True, fill="both")
        # Buttons on screen
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0), ('CE', 5, 1), ('^', 5, 2), ('%', 5, 3),
        ]
        # Adding buttons on the screen using for loop
        for (text, row, col) in buttons:
            button = tk.Button(buttons_frame, text=text, font=("Arial", 18), bd=5, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")
        
        for i in range(6):
            buttons_frame.grid_rowconfigure(i, weight=1)
            if i < 4:
                buttons_frame.grid_columnconfigure(i, weight=1)
  
    # This function handles the on click event 
    def on_button_click(self, char):
        if char in '0123456789.':
            self.current_input += char
            self.result_var.set(self.current_input)
        elif char in '+-*/^%':
            self.current_input += f' {char} '
            self.result_var.set(self.current_input)
        elif char == '=':
            try:
                self.current_input = str(eval(self.current_input.replace('^', '**')))
                self.result_var.set(self.current_input)
            except Exception as e:
                self.result_var.set("Error")
                self.current_input = ""
        elif char == 'C':
            self.current_input = ""
            self.result_var.set(self.current_input)
        elif char == 'CE':
            self.current_input = self.current_input[:-1]
            self.result_var.set(self.current_input)
    
    def run(self):
        self.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
