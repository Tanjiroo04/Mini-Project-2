import tkinter as tk
from tkinter import messagebox
import csv
import os

# Function to calculate grade
def calculate_grade():
    try:
        name = entry_name.get()
        marks = [float(entry.get()) for entry in entries_marks]
        
        total = sum(marks)
        percentage = total / len(marks)

        # Grade logic
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        # Show result in label
        label_result.config(
            text=f"Total: {total} | Percentage: {percentage:.2f}% | Grade: {grade}"
        )

        # Save to CSV
        save_to_csv(name, marks, total, percentage, grade)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid marks for all subjects.")

# Function to save data to CSV
def save_to_csv(name, marks, total, percentage, grade):
    file_exists = os.path.isfile("student_grades.csv")
    with open("student_grades.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Name"] + [f"Subject{i+1}" for i in range(len(marks))] +
                            ["Total", "Percentage", "Grade"])
        writer.writerow([name] + marks + [total, percentage, grade])

# GUI Window
window = tk.Tk()
window.title("Student Grade Calculator")
window.geometry("400x400")
window.configure(bg="#f2f2f2")

# Name entry
tk.Label(window, text="Student Name:", font=("Arial", 12), bg="#f2f2f2").pack()
entry_name = tk.Entry(window, font=("Arial", 12))
entry_name.pack(pady=5)

# Marks entry for subjects
entries_marks = []
num_subjects = 5  # Change this if needed
for i in range(num_subjects):
    tk.Label(window, text=f"Subject {i+1} Marks:", font=("Arial", 12), bg="#f2f2f2").pack()
    entry = tk.Entry(window, font=("Arial", 12))
    entry.pack(pady=2)
    entries_marks.append(entry)

# Calculate button
tk.Button(window, text="Calculate Grade", font=("Arial", 12, "bold"), bg="green", fg="white",
          command=calculate_grade).pack(pady=10)

# Result label
label_result = tk.Label(window, text="", font=("Arial", 12, "bold"), bg="#f2f2f2", fg="blue")
label_result.pack(pady=10)

window.mainloop()
