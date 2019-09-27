import turtle

def square(sidelength):
    for i in range(4):
        turtle.forward(sidelength)
        turtle.right(90)

turtle.shape("turtle")
turtle.color("red")
square(60)
turtle.speed(200)

for i in range(73):
    square(60)
    turtle.right(5)

turtle.penup()
turtle.color("green")
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.pendown()
square(60)
turtle.speed(50)

for i in range(73):
    square(60)
    turtle.right(5)


turtle.penup()
turtle.goto(100, 150)
turtle.right(90)
turtle.forward(250)
turtle.pendown()
turtle.color("blue")

square(60)
turtle.speed(50)

for i in range(73):
    square(60)
    turtle.right(5)

turtle.penup()
turtle.forward(100)
turtle.right(160)
turtle.forward(500)
turtle.pendown()
turtle.color("pink")

square(60)
turtle.speed(50)

for i in range(73):
    square(60)
    turtle.right(5)







turtle.exitonclick()
