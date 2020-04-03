# A program to add and multiply two numbers
# Wednesday, February 26, 2020
# CTI-110 P2HW1 - Basic Math
# Mady Sissoko
#

#Enter First number
firstnumber=int(input("Enter the first number: "))
#Enter Second number
secondnumber=int(input("Enter the second number: "))

# Add two numbers
sum = int(firstnumber) + int(secondnumber)

# Multiply two numbers
mul = int(firstnumber) * int(secondnumber)

# Display the sum of both numbers
print('sum of both numbers {0} and {1} is {2}'.format(firstnumber, secondnumber, sum))

# Display the multiplication of both numbers
print('product of both numbers {0} and {1} is {2}'.format(firstnumber, secondnumber, mul))
