#Function for each operation
def add (num1, num2):
    return num1 + num2

def subtract (num1,num2):
    return num1-num2

def multiply (num1,num2):
    return num1*num2

def divide (num1,num2):
    return num1/num2

# Input from user
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
operation = input("Choose Opearion: a,s,d,m: ")


if operation == "a":
    print(number_1, "+", number_2, "=", add(number_1,number_2))
    
elif operation == "s":
    print(number_1, "-", number_2, "=", subtract(number_1,number_2))

elif operation == "m":
    print(number_1, "*", number_2, "=", multiply(number_1,number_2))

elif operation == "d":
    print(number_1, "/", number_2, "=", divide(number_1,number_2))
