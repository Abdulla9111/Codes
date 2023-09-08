a = int(input("Enter the first Value: "))
c= input("Enter the operator: ")
b= int(input("Enter the Second value; "))
if (c == '+'):
    print("Ans of the given values after calculating is",a+b)
elif(c== '-'):
    print("Ans of the given values after calculating is",a-b)
elif(c== '*'):
    print("Ans of the given values after calculating is",a*b)
elif(c== '/'):
    print("Ans of the given values after calculating is",a/b)
elif(c== '%'):
    print("Ans of the given values after calculating is",a%b)
elif(c== '**'):
    print("Ans of the given values after calculating is",a**b)
elif(c== '//'):
    print("Ans of the given values after calculating is",a//b)
else:
    print("Unknown")
