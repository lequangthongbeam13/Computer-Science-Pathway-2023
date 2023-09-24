import tkinter as tk
from tkinter import ttk
import math

# function to perform basic calculations
def calculate():
    x = float(entry_x.get())
    y = float(entry_y.get())
    operation = operation_choice.get()

    if operation == '+':
        result = x + y
    elif operation == '-':
        result = x - y
    elif operation == '*':
        result = x * y
    elif operation == '/':
        if y == 0:
            result = 'Can not divided by 0'
        else: 
            result = x / y
    elif operation == '^':
        result = x ** 2
    elif operation == 'v':
        if x < 0:
            result = 'a negative number Square Root can not be calculated'
        else:
            result = math.sqrt(x)
    else:
        result = 'Invalid Operation'

    result_tab.config(text=f'Result: {result}')

# Creat UI window
UI = tk.Tk()
UI.title('Basic Calculator')

# show entry num1 window
x_tab = ttk.Label(UI, text='Num1: ')
x_tab.grid(row=1, column=0)

entry_x = ttk.Entry(UI)
entry_x.grid(row=1, column=1)

# show operation choice box
operation_choice = ttk.Combobox(UI, values=['+', '-', '*', '/', '^', 'v'])
operation_choice.set('+')
operation_choice.grid(row=1, column=2)

# show entry num2 window
y_tab = ttk.Label(UI, text='Num2: ')
y_tab.grid(row=1, column=4)

entry_y = ttk.Entry(UI)
entry_y.grid(row=1, column=5)

# show result 
result_tab = ttk.Label(UI, text='=')
result_tab.grid(row=2, column=0)

# show calculate button
calculate_button = ttk.Button(UI, text='Calculate', command=calculate)
calculate_button.grid(row=4, column=0, columnspan=6)

UI.mainloop()