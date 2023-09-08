n=int(input("Enter the value of n"))
a = (n % 1)
b = (n % n)
if(a == 0 and b == 0):
  print("n is prime number")
else:
  print("n is not prime number")
