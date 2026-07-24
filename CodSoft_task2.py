from tkinter import *
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operator.get()

        if op == "+":
            result.set(num1 + num2)
        elif op == "-":
            result.set(num1 - num2)
        elif op == "*":
            result.set(num1 * num2)
        elif op == "/":
            if num2 != 0:
                result.set(num1 / num2)
            else:
                messagebox.showerror("Error", "Division by zero!")
    except:
        messagebox.showerror("Error", "Enter valid numbers!")

root = Tk()
root.title("Calculator")
root.geometry("350x350")

Label(root, text="CALCULATOR", font=("Arial", 18, "bold")).pack(pady=10)

Label(root, text="First Number").pack()
entry1 = Entry(root)
entry1.pack()

Label(root, text="Second Number").pack()
entry2 = Entry(root)
entry2.pack()

operator = StringVar()
operator.set("+")

Label(root, text="Select Operation").pack()

OptionMenu(root, operator, "+", "-", "*", "/").pack()

result = StringVar()

Button(root, text="Calculate", command=calculate, width=20).pack(pady=10)

Label(root, text="Result:", font=("Arial", 12)).pack()
Entry(root, textvariable=result, state="readonly").pack()

root.mainloop()
