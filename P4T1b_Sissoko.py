#Import turtle
#Create play ground for turtle
#Create turtle and assing to an object
#Set pen size
#set pen color
#Draw first initial
#Raise turtle pen up
#Move turtle forward
#Put pen down
#Draw second intial

import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
mady = turtle.Turtle()    # Create a turtle, assign to mady
mady.pensize(5)
mady.pencolor("brown")

mady.left(90)
mady.forward (100)
mady.left(45)
mady.back(50)
mady.right(90)
mady.forward(50)
mady.left(45)
mady.back(100)

mady.right(90)
mady.penup()
mady.forward(50)

mady.pendown()
mady.forward (100)
mady.left(90)
mady.forward(50)
mady.left(90)
mady.forward(100)
mady.right(90)
mady.forward(50)
mady.right(90)
mady.forward(100)


# end commands
wn.mainloop()             # Wait for user to close window
