import turtle as t
import math

def pentagram_in_circle():
    # Rysowanie pentagramu
    t.color("black", "red")
    t.begin_fill()
    for _ in range(5):
        t.forward(300)
        t.right(144)
    t.end_fill()

    # Rysowanie okręgu wokół pentagramu
    t.penup()
    t.goto(0, 0)  # Powrót do środka ekranu
    t.pendown()
    t.circle(150)

    # Obrót pentagramu o 36 stopni, aby umieścić go wewnątrz koła
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.right(36)

# Wywołanie funkcji
pentagram_in_circle()

# Zakończenie programu po kliknięciu
t.hideturtle()
t.done()
