import time
import turtle
turtle.tracer(0)

t=turtle.Turtle("circle")
t.left(45)
t.up()

while True:
    t.forward(10)
    x=t.xcor()
    y=t.ycor()
    if x > 300 or x < -300:
        t.backward(10)
        t.right(90)
    if y > 250 or y < -250:
        t.backward(10)
        t.right(90)
    turtle.update()
    time.sleep(0.03)
