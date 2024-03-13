import tkinter as tk
from tkinter import messagebox


class BMI_Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Tracker")
        self.root.geometry("300x250")

        self.bmi_records = []  # List to store BMI data with names

        self.input_window()

    def input_window(self):
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        tk.Label(self.input_frame, text="Enter Name: ").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.input_frame, text="Enter Weight (kg): ").grid(row=1, column=0)
        self.weight_entry = tk.Entry(self.input_frame)
        self.weight_entry.grid(row=1, column=1)

        tk.Label(self.input_frame, text="Enter Height (m): ").grid(row=2, column=0)
        self.height_entry = tk.Entry(self.input_frame)
        self.height_entry.grid(row=2, column=1)

        calculate_button = tk.Button(self.input_frame, text="Calculate BMI", command=self.calculate_bmi)
        calculate_button.grid(row=3, columnspan=2, pady=10)

    def calculate_bmi(self):
        try:
            name = self.name_entry.get()
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())
            bmi = weight / (height * height)

            self.display_window(name, bmi, weight, height)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid name, weight, and height.")

    def display_window(self, name, bmi, weight, height):
        display_window = tk.Toplevel(self.root)
        display_window.title("BMI Information")

        label = tk.Label(display_window, text=f"{name}'s BMI is: {bmi:.2f}")
        label.pack()

        result_label = tk.Label(display_window, text=self.get_bmi_category(bmi))
        result_label.pack()

        save_button = tk.Button(display_window, text="Save BMI",
                                command=lambda: self.save_bmi(name, bmi, weight, height))
        save_button.pack()

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "You are underweight."
        elif 18.5 <= bmi < 25:
            return "You are within a healthy weight range."
        else:
            return "You are overweight."

    def save_bmi(self, name, bmi, weight, height):
        self.bmi_records.append((name, weight, height, bmi))  # Append BMI data with name to the list
        messagebox.showinfo("Success", "BMI data saved successfully!")

    def view_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("BMI History")

        if not self.bmi_records:
            messagebox.showinfo("No Data", "No BMI data found.")
        else:
            for entry in self.bmi_records:
                tk.Label(history_window,
                         text=f"Name: {entry[0]}, Weight: {entry[1]} kg, Height: {entry[2]} m, BMI: {entry[3]:.2f}").pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = BMI_Calculator(root)

    history_button = tk.Button(root, text="View BMI History", command=app.view_history)
    history_button.pack(pady=10)

    root.mainloop()
