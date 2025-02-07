import tkinter as tk
from tkinter import messagebox

# Funksiýalary kesgitlemek
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Ýalňyşlyk", "0-a bölüp bolmaýar!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Ýalňyşlyk", "Funksiýa dogry däl!")
            return

        result_label.config(text=f"Netije: {result}")
    except ValueError:
        messagebox.showerror("Ýalňyşlyk", "Sany dogry giriziň!")

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result_label.config(text="Netije: ")

# Esasy penjire
window = tk.Tk()
window.title("Hasaplama Maşyny")
window.geometry("300x300")

# Sany girizmek üçin ýerler
tk.Label(window, text="1-nji sany giriziň:").pack()
entry1 = tk.Entry(window)
entry1.pack()

tk.Label(window, text="2-nji sany giriziň:").pack()
entry2 = tk.Entry(window)
entry2.pack()

# Funksiýany saýlamak
tk.Label(window, text="Funksiýany saýlaň:").pack()
operation_var = tk.StringVar(value="+")
operations_frame = tk.Frame(window)
operations_frame.pack()
for op in ["+", "-", "*", "/"]:
    tk.Radiobutton(operations_frame, text=op, variable=operation_var, value=op).pack(side=tk.LEFT)

# Netije üçin ýer
result_label = tk.Label(window, text="Netije: ", font=("Arial", 12))
result_label.pack(pady=10)

# Düwmeler
tk.Button(window, text="Hasapla", command=calculate).pack(pady=5)
tk.Button(window, text="Arassala", command=clear).pack(pady=5)

# Penjiräni görkezmek
window.mainloop()