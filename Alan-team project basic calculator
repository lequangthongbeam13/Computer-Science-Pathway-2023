import math
# def function for basic calculator

def add(x,y):
    # function of addition
    return x + y
def subtract(x,y):
    # function of subtract
    return x - y
def multiply(x,y):
    # function of multiply
    return x * y
def division(x,y):
    # concern about 0
    if y == 0:
       return 'can not divide by 0'
    # function of division
    return x / y
def square(x):
    # function of square
    return x ** 2
def squareroot(x):
    # concern about negative number
    if x<0:
       return 'can not squareroot of a negative number'
    # function of squareroot
    return math.sqrt(x)

# Main loop included menu and calculations, while true means it will continue to run over and over 
while True:
    print ('Basic Calculator Menu: ')
    print ("1. Addition'+'")
    print ("2. subtract'-'")
    print ("3. Multiply'*'")
    print ("4. Division'/'")
    print ("5. Square'^2'")
    print ("6. Squareroot'vx'")
    print ('7. Exit')
   
   # choose operation
    choice = input('Please select each operation by number: ')
    
    # operate '1-4'
    if choice in ['1','2','3','4']:
       x = float(input('Enter first number: '))
       y = float(input('Enter second number: '))
    
       if choice == '1':
          result = add(x,y)
          operation = 'Addition'
       elif choice == '2':
            result = subtract(x,y)
            operation = 'subtract'
       elif choice == '3':
            result = multiply(x,y)
            operation = 'Mutiply'
       elif choice == '4':
            result = division(x,y)
            operation = 'Division'
       print(f'Rsult of {operation}: {result}')
    
    #'5','6'just need one number    
    elif choice in ['5','6']:
        x = float(input('Enter first number: '))
        y = None
        if choice == '5':
            result = square(x)
            operation = 'square'
        elif choice == '6':
            result = squareroot(x)
            operation = 'squareroot'
        print(f'Rsult of {operation}: {result}')
    # when choose '7'
    elif choice == '7':
       print("Bye Bye!")
       break

    else:
        print('Invalid input. Please try again')
        
