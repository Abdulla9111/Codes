num1=int(input("enter value of num1"))
num2=int(input("enter value of num2"))
num3=int(input("enter value of num3"))
if (num1 > num2 and num1 > num3):
    print("maximum number among three numbers is", num1)
elif (num2 > num1 and num2 > num3):
    print("maximum number among three numbers is", num2)
else :
    print("maximum number is",num3)

