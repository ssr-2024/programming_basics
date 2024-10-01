# create a function that draws a zig-zag line, then continues forward

import turtle as t

def jump() :
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.left(60)

t.forward(100)
jump()
t.forward(100)

t.exitonclick