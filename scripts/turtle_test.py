import turtle               # import turtle library
wn = turtle.Screen()        # create a graphics window ,an instance of Screen class
wn = wn.bgcolor("lightgreen") #

tess = turtle.Turtle()
tess.pensize(10)
tess.forward(120)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)

tess.right(120)
tess.left(120)

alex = turtle.Turtle()     # create a turtle named alex, an instance of Turtle class
alex.color("hotpink")
alex.forward(50)           # method that tell alex to move forward by 150 unit
alex.left(90)              # method that tell alex to turn left by 90 degree, method
alex.forward(50)
alex.left(90)  
alex.forward(50)  
alex.left(90)
alex.forward(50)

tess.clear()
alex.clear()

alex.penup()
alex.goto(123,50)             # move the turtle to an absolute position
alex.pendown()
alex.right(90)
alex.forward(100)

wn.exitonclick()