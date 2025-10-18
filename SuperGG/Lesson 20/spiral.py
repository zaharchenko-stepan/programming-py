import turtle
t = turtle.Turtle()
t.hideturtle()
for i in range(1000):
    t.forward(i)
    t.left(90)
turtle.mainloop()