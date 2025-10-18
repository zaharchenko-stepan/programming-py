import turtle
t=turtle.Turtle()
t.speed(0)
for i in ("black" , "red" , "green" , "blue"):
    t.color(i)
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.up()
    t.forward(200)
    t.down()

turtle.mainloop()