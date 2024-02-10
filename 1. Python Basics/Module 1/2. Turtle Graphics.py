import turtle           # Importing a turtle Libary
wn = turtle.Screen()    # Creating a Graphic Windows
wn.bgcolor("gray")

Nova = turtle.Turtle()  # Creating a Object name for Turtle
Nova.circle(75)
Nova.color("red")
Nova.forward(150)
Nova.left(90)
Nova.forward(75)
Nova.left(90)
Nova.forward(150)
Nova.left(90)
Nova.forward(75)

# We can use up() and down() Function with turtle to penup and pendown.
  
# Now lets create a square using for loop
nova = turtle.Turtle()
nova.shape("turtle")
nova.color("purple")
forw = 75
angle = 90
for _ in range(4):
    nova.stamp()
    nova.forward(forw)
    nova.left(angle)

wn.exitonclick()