# draw a square

import turtle as t

length = 60
angle = 90
t.fillcolor('red')
t.pensize(5)
t.begin_fill()
t.backward(length)
t.left(angle)
t.backward(length)
t.left(angle)
t.backward(length)
t.left(angle)
t.backward(length)
t.left(angle)
t.end_fill()
t.exitonclick()


