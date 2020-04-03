#Import turtle
#Set initial number of squares
#Assign t to turtle
#Pendown
#Define square side size
#While statement is true
#Print "Input the number of squares"
#Except value error
#Print "please enter and integer"
#If number of square entered is greater the 3
#Draw number of squares entered
import turtle

num_squares = 3
t = turtle.Turtle()
t.pendown()
side = side_unit = 30

while True:
    try:
        num_squares = int(input('input the number of squares'))
    except ValueError:
        print("please enter an integer")
    if num_squares > 3:
        break

for sq in range(1, num_squares + 1):
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    t.forward(side)
    t.left(90)
    side = side_unit + 3 * sq  # increase the size of the side

    t.goto(0,0)                # return to base

turtle.done()
