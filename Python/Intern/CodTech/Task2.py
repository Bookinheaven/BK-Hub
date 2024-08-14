import tkinter as tk
from tkinter import messagebox

class StudentGrades:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def calculate_average(self):
        total_grades = sum(sum(grades) for grades in self.grades.values())
        num_grades = sum(len(grades) for grades in self.grades.values())
        return total_grades / num_grades if num_grades > 0 else 0

    def calculate_gpa(self, average):
        if average >= 90:
            return 4.0, 'A'
        elif average >= 80:
            return 3.0, 'B'
        elif average >= 70:
            return 2.0, 'C'
        elif average >= 60:
            return 1.0, 'D'
        else:
            return 0.0, 'F'
    
    def get_grades_summary(self):
        summary = "\nGrades by Subject:\n"
        for subject, grades in self.grades.items():
            summary += f"{subject}: {grades}\n"
        average = self.calculate_average()
        gpa, letter_grade = self.calculate_gpa(average)
        summary += f"\nOverall Average Grade: {average:.2f}\n"
        summary += f"GPA: {gpa:.2f}\n"
        summary += f"Letter Grade: {letter_grade}\n"
        return summary

class StudentGradesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Grades and GPA Calculator")
        self.geometry("500x600")
        self.student_grades = StudentGrades()

        self.create_widgets()

    def create_widgets(self):
        # Subject Entry
        tk.Label(self, text="Subject:").pack(pady=10)
        self.subject_entry = tk.Entry(self, width=30)
        self.subject_entry.pack()

        # Grade Entry
        tk.Label(self, text="Grade:").pack(pady=10)
        self.grade_entry = tk.Entry(self, width=30)
        self.grade_entry.pack()

        # Buttons
        add_button = tk.Button(self, text="Add Grade", command=self.add_grade)
        add_button.pack(pady=10)

        display_button = tk.Button(self, text="Display Grades and GPA", command=self.display_grades)
        display_button.pack(pady=10)

        clear_button = tk.Button(self, text="Clear Grades", command=self.clear_grades)
        clear_button.pack(pady=10)

        # Text area to display grades and GPA
        self.result_text = tk.Text(self, height=15, width=50)
        self.result_text.pack(pady=10)
        self.result_text.config(state=tk.DISABLED)

    def add_grade(self):
        subject = self.subject_entry.get()
        try:
            grade = float(self.grade_entry.get())
            if 0 <= grade <= 100:
                self.student_grades.add_grade(subject, grade)
                messagebox.showinfo("Success", f"Added grade {grade} for {subject}.")
                self.subject_entry.delete(0, tk.END)
                self.grade_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Invalid Input", "Grade must be between 0 and 100.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for grade.")

    def display_grades(self):
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        summary = self.student_grades.get_grades_summary()
        self.result_text.insert(tk.END, summary)
        self.result_text.config(state=tk.DISABLED)

    def clear_grades(self):
        self.student_grades = StudentGrades()
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state=tk.DISABLED)
        messagebox.showinfo("Success", "All grades have been cleared.")

if __name__ == "__main__":
    app = StudentGradesApp()
    app.mainloop()
