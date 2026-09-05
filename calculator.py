def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def divide( a,b):
    return a/b

num1 = float(input("enter first number :"))
operation = input("choose the operator (+,-,*,/) :")
num2 = float(input("enter second number :"))
if operation == "+" :
    result = add(num1,num2)
elif operation == "-" :
    result = sub(num1,num2)   
elif operation == "*" :
    result = multi(num1,num2) 
elif operation == "/":
    try :
        result = divide(num1,num2)
    except ZeroDivisionError :
        result = "Error ! cannot divide by zero"     
else:
    result = "invaild operatiton"    
print("Result", result)           
