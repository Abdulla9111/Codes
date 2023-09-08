num1= int(input("Enter value of num1= "))
num2= int(input("Enter value of num2= "))
num3= int(input("Enter value of num3= "))
if(num1>num2):
    if(num1>num3):
        print("max num is =",num1)
    else:
        print("max num is =",num3)
else:
    if(num2>num3):
      print("max num is =",num2)
    else:
        print ("max num is =",num3)
