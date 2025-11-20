import turtle 

# Ordinary Spirals
wn = turtle.Screen()
wn.bgcolor("lightgreen")

shuja = turtle.Turtle()

distance = 50

for i in range(4):
  shuja.right(90)
  shuja.forward(distance)
  distance = distance +10
  
shuja.clear()               # clear turtle drawing

# Imprint Spiral
elon = turtle.Turtle()
elon.color("blue")
elon.shape("turtle")      # change the shape of turtle to look like an actual turtle

dist = 5
for i in range(16):
  elon.stamp()            # leave a stamp when moving forward instead of continuous
  elon.forward(dist)
  elon.right(24)
  dist = dist + 2

elon.clear()

# Circle of Turtle Shapes
adam = turtle.Turtle()
adam.color("green")
adam.shape("turtle")
adam.penup()              # Allow you to change position of turtle without moving it

for i in range(10):
  adam.forward(50)
  adam.stamp()
  adam.forward(-50)
  adam.right(36)

# line of turtle shapes
ali = turtle.Turtle()
ali.shape("turtle")
ali.color("blue")
ali.penup()                # pull the pen up no drawing when moving
for i in range(3):
  ali.stamp()
  ali.forward(50)
wn.exitonclick()           # exit the screem when it is clicked
  
