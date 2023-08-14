import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 6:
            messagebox.showerror("Error", "Password length should be at least 6 characters.")
            return

        complexity = complexity_var.get()

        characters = ""
        if complexity == "Weak":
            characters = string.ascii_letters
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits
        elif complexity == "Strong":
            characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        password_label.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid password length.")

# Create the main application window
app = tk.Tk()
app.title("Password Generator")

# Create and place widgets in the window
label_length = tk.Label(app, text="Enter the password length:")
label_length.pack()

entry_length = tk.Entry(app)
entry_length.pack()

label_complexity = tk.Label(app, text="Select  password complexity:")
label_complexity.pack()

complexity_var = tk.StringVar()
complexity_choices = ["Weak", "Medium", "Strong"]
complexity_var.set("Weak")  # Default complexity is Weak

for choice in complexity_choices:
    radio_btn = tk.Radiobutton(app, text=choice, variable=complexity_var, value=choice)
    radio_btn.pack()

generate_btn = tk.Button(app, text="Generate Password", command=generate_password)
generate_btn.pack()

password_label = tk.Label(app, text="Generated Password:")
password_label.pack()

app.mainloop()
