import turtle

wn = turtle.Screen()
shuja = turtle.Turtle()

# Drawing Sun 
shuja.color("yellow")
shuja.fillcolor("yellow")
shuja.begin_fill()
shuja.circle(50)
shuja.end_fill()

# Bringing turtle to center right circumference of Sun
shuja.left(90)
shuja.forward(50)
shuja.right(90)
shuja.forward(50)

# List we will use to draw planets using for loop in order
radius = [4,7,8,6,20,16,12,14]
colors = ["gray","yellow","blue","red","orange","gold","cyan","dark blue"]
forward_distances = [40, 40, 40, 60, 60, 60, 60,60]

# Drawing Planets
for i in range(0,8):
  # For
  shuja.penup()
  
  shuja.forward(forward_distances[i])
  shuja.pendown()
  shuja.color(colors[i])
  shuja.fillcolor(colors[i])
  shuja.begin_fill()
  shuja.circle(radius[i])
  shuja.end_fill()
  
wn.exitonclick()