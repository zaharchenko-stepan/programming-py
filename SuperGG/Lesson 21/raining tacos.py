import turtle
import random
import time

turtle.tracer(0)

t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()

for t in (t1,t2,t3,t4):
    t.hideturtle()
    t.up()
    x = random.randint(-250, 250)
    y = random.randint(200, 250)
    t.setpos(x, y)
    t.color("lightblue")
    t.right(90)

while True:
    for t in (t1,t2,t3,t4):
        t.clear()

        if t.ycor() < -250:
            x=random.randint(-250,250)
            y=random.randint(200,250)
            t.setpos(x, y)
        t.forward(10)
        t.dot(8)
        turtle.update()
        time.sleep(0.01)
