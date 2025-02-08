import turtle as t

for i in range(4):
    if i%2:
        t.forward(100)
    else:
        t.forward(50)
    t.right(90)

t.exitonclick()