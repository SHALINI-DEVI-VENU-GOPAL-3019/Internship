from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("To-Do List")
root.geometry("400x450")

tasks = []

def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except:
        messagebox.showwarning("Warning", "Select a task to delete.")

def clear_tasks():
    listbox.delete(0, END)
    tasks.clear()

Label(root, text="TO-DO LIST", font=("Arial", 18, "bold")).pack(pady=10)

task_entry = Entry(root, width=35, font=("Arial", 12))
task_entry.pack(pady=10)

Button(root, text="Add Task", width=20, command=add_task).pack(pady=5)
Button(root, text="
