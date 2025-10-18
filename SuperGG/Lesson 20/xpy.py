import turtle
t=turtle.Turtle()
t.speed(6)

def hideturtle():
    t.hideturtle()

def showturtle():
    t.showturtle()

def wi5():
    t.width(5)

def w():
    t.forward(10)

def w5():
    t.width(10)

def s():
    t.backward(10)

def a():
    t.left(10)

def d():
    t.right(10)

def secret():
    for i in range(4):
        t.speed(0)
        t.width(3)
        t.forward(100)
        t.left(90)
        t.circle(100)
    t.speed(6)
    t.hideturtle()
    t.left(1440)
    t.showturtle()
    breaking_python()

def breaking_python():
    for i in range(999999999999999):
        t.forward(100)
        t.left(720)
        t.width(9999)
        t.circle(100)

def clear():
    t.clear()

def quader():
    t.speed(0)
    for i in range(200):
        t.forward(i)
        t.left(i)

turtle.onkeypress(w, 'w')
turtle.onkeypress(s, 's')
turtle.onkeypress(a, 'a')
turtle.onkeypress(d, 'd')
turtle.onkeypress(secret, 'm')
turtle.onkeypress(breaking_python, ' ')
turtle.onkeypress(clear, 'c')
turtle.onkeypress(wi5, '5')
turtle.onkeypress(hideturtle, 'h')
turtle.onkeypress(showturtle, 'b')
turtle.onkeypress(quader, 'q')
turtle.onkeypress(w5, '0')
turtle.listen()
turtle.mainloop()



