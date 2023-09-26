import tkinter as tk
from tkinter import ttk
import math

# function to perform basic calculations
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def division(x,y):
    # concern about 0
    if y == 0:
       return 'can not divide by 0'
    return x / y

def square(x):
    return x ** 2

def squareroot(x):
    # concern about negative number
    if x<0:
       return 'can not squareroot of a negative number'
    return math.sqrt(x)

# Function to do the calculation
def calculate():
    x = entry_x.get()
    y = entry_y.get()
    operation = operation_choice.get()

    # to valid x
    if not x.strip():
        result_tab.config(text='It is not a valid number')
        return
    
    try:
        x = float(x)

        # calculation for '+','-','*','/'
        if operation in['+','-','*','/']:

            # to valid y
            if not y.strip():
                result_tab.config(text='It is not a valid number')
                return
            y = float(y)
            
            if operation == '+':
                result = add(x,y)

            elif operation == '-':
                result = subtract(x,y)

            elif operation == '*':
                result = multiply(x,y)

            elif operation == '/':
                result = division(x,y)

        # calculation for '^','v' and config y is empty
        elif operation in['^','v']:
            y = None

            if operation == '^':
                result = square(x)

            else:
                result = squareroot(x)

        else:
                result = 'Invalid Operation'

        result_tab.config(text=f'Result: {result}')

    except ValueError:
        result_tab.config(text='It is not a valid number')
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
