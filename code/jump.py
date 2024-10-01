import turtle as t

def jump(size):
    t.left(60)
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.left(60)

t.teleport(-300,0)
size=20
t.forward(50)
for jumps in range (5):
    jump(size)
    size=size+20
    t.forward(50)
exitonclick()