
# creeati un patrat care se deseneaza de 100 de ori

import turtle




turtle.title("Patrat de 100 de ori")
t = turtle.Turtle()

def forma(grade, r, g, b, rm, gm, bm):
    turtle.colormode(255)
    t.pensize(4)

    for i in range(100):
        t.color(r,g,b)
        r = r + rm
        g = g + gm
        b = b + bm
        t.forward(i * 5 + 10)
        t.left(grade)
    turtle.mainloop()


