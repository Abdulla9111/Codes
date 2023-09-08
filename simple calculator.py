import math
a = int(input("Enter the value of a= "))
b = int(input("Enter the value of b= "))
n = input('enter the function: ')
if (n == '+'):
    print (a + b)
elif(n == '-'):
    print (a - b)
elif (n == '*'):
    print (a * b)
elif(n == '/'):
    print (a / b)
else:
    print('function error')