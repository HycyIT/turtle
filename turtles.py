import turtle

turtle.bgcolor('white')
t = turtle.Turtle()
t.shape('turtle')
t.color("black", "yellow")
t.width(3)
t.speed(0)


"""def spirala():
    kat = 90
    bok = 200
    while bok > 0:
        t.forward(bok)
        t.right(kat)
        bok -= 5
"""


"""def bombka():
    for i in range(20):
        t.forward(100)
        t.backward(100)
        t.right(18)

    t.right(90)
    t.forward(100)
    t.right(270)
    t.circle(100)


bombka()
"""
"""
t.left(40)
t.forward(60)
t.circle(30, 200)
t.left(240)
t.circle(30, 200)
t.forward(60)
"""

"""
def trojkat():
    for i in range(3):
        t.right(120)
        t.forward(100)


for i in range(3):
    t.right(60)
    t.begin_fill()
    trojkat()
    t.color("black", "yellow")
    t.end_fill()
    t.right(60)
    t.begin_fill()
    trojkat()
    t.color("black", "green")
    t.end_fill()

t.speed(2)
t.forward(100)
t.begin_fill()
t.pencolor("white")
t.forward(20)
t.left(90)
t.pencolor("black")
t.end_fill()
t.circle(120)
t.end_fill()
t.hideturtle()
"""

"""
def pentagram():
    t.color("black", "red")
    t.begin_fill()
    for i in range(5):
        t.forward(300)
        t.right(144)
    t.right(108)
    t.circle(157)
    t.end_fill()


pentagram()
"""


def fuction():
    for i in range(30):
        t.forward(200)
        t.left(110)


fuction()
turtle.done()
