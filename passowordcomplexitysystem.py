import tkinter as tk
from tkinter import ttk

import re

# Function to check password complexity
def check_password(event=None):
    password = password_var.get()
    
    if 8 <= len(password) <= 20:
        length_label.config(fg="green", text="✔ 8-20 Characters")
    else:
        length_label.config(fg="red", text="✖ 8-20 Characters")

    if re.search(r"[A-Z]", password):
        capital_label.config(fg="green", text="✔ At least one capital letter")
    else:
        capital_label.config(fg="red", text="✖ At least one capital letter")

    if re.search(r"\d", password):
        number_label.config(fg="green", text="✔ At least one number")
    else:
        number_label.config(fg="red", text="✖ At least one number")

    if re.search(r"\s", password):
        space_label.config(fg="red", text="✖ No spaces allowed")
    else:
        space_label.config(fg="green", text="✔ No spaces")

# Show/hide password
def toggle_password():
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# GUI Setup
root = tk.Tk()
root.title("Password Complexity Checker")
root.geometry("400x300")
root.resizable(False, False)

password_var = tk.StringVar()
show_var = tk.BooleanVar()

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
password_entry = tk.Entry(root, textvariable=password_var, show="*", font=("Arial", 12), width=30)
password_entry.pack()
password_entry.bind("<KeyRelease>", check_password)

show_checkbox = tk.Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password)
show_checkbox.pack(pady=5)

# Requirements display
length_label = tk.Label(root, text="✖ 8-20 Characters", fg="gray", font=("Arial", 10))
length_label.pack()

capital_label = tk.Label(root, text="✖ At least one capital letter", fg="gray", font=("Arial", 10))
capital_label.pack()

number_label = tk.Label(root, text="✖ At least one number", fg="gray", font=("Arial", 10))
number_label.pack()

space_label = tk.Label(root, text="✔ No spaces", fg="gray", font=("Arial", 10))
space_label.pack()

root.mainloop()
