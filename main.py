import tkinter as tk
from tkinter import messagebox

# Tkinter UI setup
root = tk.Tk()
root.title("Login System")

# UI Elements
tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Login").pack()
tk.Button(root, text="Signup").pack()

root.mainloop()


<<<<<<< HEAD
def signup():
    username = entry_user.get()
    password = entry_pass.get()
    messagebox.showinfo("Success", "Signup successful!")
    
tk.Button(root, text="Signup", command=signup).pack()


def login():
    username = entry_user.get()
    password = entry_pass.get()
    if username and password:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Please fill in both fields")

tk.Button(root, text="Login", command=login).pack()


tk.Label(root, text="Please Login or Signup").pack()
tk.Button(root, text="Login", command=login).pack()
tk.Button(root, text="Signup", command=signup).pack()
=======

import tkinter as tk

# Tkinter UI setup for adding shifts
root = tk.Tk()
root.title("Add Shift")

tk.Label(root, text="Employee Name").pack()
entry_employee = tk.Entry(root)
entry_employee.pack()

tk.Label(root, text="Shift Time").pack()
entry_shift = tk.Entry(root)
entry_shift.pack()

tk.Button(root, text="Add Shift").pack()

root.mainloop()



def add_shift():
    employee = entry_employee.get()
    shift_time = entry_shift.get()
    messagebox.showinfo("Success", f"Shift for {employee} at {shift_time} added.")

tk.Button(root, text="Add Shift", command=add_shift).pack()


import sqlite3

conn = sqlite3.connect("shifts.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS shifts (id INTEGER PRIMARY KEY, employee TEXT, shift_time TEXT)''')
conn.commit()

def add_shift():
    employee = entry_employee.get()
    shift_time = entry_shift.get()
    cursor.execute("INSERT INTO shifts (employee, shift_time) VALUES (?, ?)", (employee, shift_time))
    conn.commit()
    messagebox.showinfo("Success", f"Shift for {employee} at {shift_time} added.")

tk.Button(root, text="Add Shift", command=add_shift).pack()


tk.Label(root, text="Enter Shift Details").pack()
tk.Button(root, text="Add Shift", command=add_shift).pack()



>>>>>>> 39bc0a78a0849ad60c5a779e6e4f68be1e80f507


import tkinter as tk

# Tkinter UI setup for updating shifts
root = tk.Tk()
root.title("Update Shift")

tk.Label(root, text="Shift ID").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="New Shift Time").pack()
entry_shift = tk.Entry(root)
entry_shift.pack()

tk.Button(root, text="Update Shift").pack()

root.mainloop()



import tkinter as tk

# Tkinter UI setup for deleting shifts
root = tk.Tk()
root.title("Delete Shift")

tk.Label(root, text="Shift ID").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Button(root, text="Delete Shift").pack()

root.mainloop()



def delete_shift():
    shift_id = entry_id.get()
    messagebox.showinfo("Success", f"Shift {shift_id} deleted.")

tk.Button(root, text="Delete Shift", command=delete_shift).pack()



import sqlite3

conn = sqlite3.connect("shifts.db")
cursor = conn.cursor()

def delete_shift():
    shift_id = entry_id.get()
    cursor.execute("DELETE FROM shifts WHERE id = ?", (shift_id,))
    conn.commit()
    messagebox.showinfo("Success", f"Shift {shift_id} deleted.")

tk.Button(root, text="Delete Shift", command=delete_shift).pack()



tk.Label(root, text="Enter Shift ID to Delete").pack()
tk.Button(root, text="Delete Shift", command=delete_shift).pack()

