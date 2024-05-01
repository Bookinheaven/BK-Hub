import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  
        bmi = weight / (height * height)
        result_label.config(text=f"BMI: {bmi:.2f}")
        if bmi < 18:
            category_label.config(text="Underweight")
        elif 18 <= bmi < 25:
            category_label.config(text="Normal")
        elif 25 <= bmi < 30:
            category_label.config(text="Overweight")
        else:
            category_label.config(text="Obese")
    except ValueError:
        result_label.config(text="Please enter valid weight and height.")

root = tk.Tk()
root.title("BMI Calculator")

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=5)

height_label = tk.Label(root, text="Height (cm):")
height_label.grid(row=1, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

category_label = tk.Label(root, text="")
category_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
