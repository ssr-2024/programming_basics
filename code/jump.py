import turtle as t

def jump(jump_height=50):
    t.left(60)
    t.forward(jump_height)
    t.right(120)
    t.forward(jump_height)
    t.left(60)


for height in range(20,70,5):
    t.forward(10)
    jump(height)
    t.forward(10)

t.exitonclick()