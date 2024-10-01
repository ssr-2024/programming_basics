import turtle as t

def jump():
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.left(60)

t.forward(100)
jump() # our own jump function
t.forward(100)

t.exitonclick()