import turtle as h
h.fillcolor('yellow')
h.begin_fill()
for i in range(4):
    h.forward(90)
    h.left(90)
h.end_fill()

h.left(90)
h.forward(90)

h.fillcolor('red')
h.begin_fill()
h.right(45)
h.forward(65)
h.right(90)
h.forward(65)
h.end_fill()

h.exitonclick()