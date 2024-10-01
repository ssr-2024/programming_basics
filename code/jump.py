import turtle as t

<<<<<<< HEAD
# define jump function
def jump(jump_height=50):
    t.left(60)
    t.forward(jump_height)
    t.right(120)
    t.forward(jump_height)
    t.left(60)


for height in range(20,70,5):
    t.forward(5)
    jump(height) # our own jump function
    t.forward(5)
=======
def jump():
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.left(60)

t.forward(100)
jump() # our own jump function
t.forward(100)
>>>>>>> 17f618643b4c8acbd1a800d6b09345df46c383b6

t.exitonclick()