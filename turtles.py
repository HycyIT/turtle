import turtle

turtle.bgcolor('white')
t = turtle.Turtle()
t.color('green')
t.shape('turtle')
t.width(5)
t.speed(3)


"""def spirala():
    kat = 90
    bok = 200
    while bok > 0:
        t.forward(bok)
        t.right(kat)
        bok -= 5
"""


def bombka():
    for i in range(20):
        t.forward(100)
        t.backward(100)
        t.right(18)

    t.right(90)
    t.forward(100)
    t.right(270)
    t.circle(100)


bombka()

turtle.done()
