import turtle
t=turtle.Turtle()
t.speed(10)
for i in range(4):
    t.forward(100)
    t.left(90)
    t.circle(100)
t.hideturtle()
turtle.mainloop()