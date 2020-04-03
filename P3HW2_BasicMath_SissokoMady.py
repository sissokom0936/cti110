# CTI-110
# P3HW1 - BasicMath
# Mady Sissoko
# March 8, 2020
#
# This function adds two numbers 
def add(x, y):
   return x + y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y


print("MENU")
print("1.Add")
print("2.Multiply")
print("3.Subtract")
print("4.Exit")

# Take input from the user 
choice = input("Enter choice(1/2/3/4): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '3':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '4':
   print("the program will close.")
else:
   print("Error , an invalid choice was entered.")
