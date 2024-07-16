#Creating a to do list 
import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    aim= aentry.get()
    if aim != "":
        listbox.insert(tk.END, aim)
        aentry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a selected task from the list
def delete_task():
    try:
        # Get the selected task
        aindex = listbox.curselection()[0]
        listbox.delete(aindex)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to clear all tasks from the list
def clear_tasks():
    listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create the task entry widget
aentry = tk.Entry(root, width=50)
aentry.grid(row=0, column=0, padx=10, pady=10)

# Create the add task button
add = tk.Button(root, text="Add Task", command=add_task)
add.grid(row=0, column=1, padx=10, pady=10)

# Create the listbox to hold the tasks
listbox = tk.Listbox(root, height=10, width=50)
listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create the delete selected task button
delete = tk.Button(root, text="Delete Task", command=delete_task)
delete.grid(row=2, column=0, padx=10, pady=10)

# Create the clear all tasks button
clear = tk.Button(root, text="Clear All", command=clear_tasks)
clear.grid(row=2, column=1, padx=10, pady=10)

# Start the main loop
root.mainloop()