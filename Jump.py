import turtle as t

def jump(jump_height=50):
    t.left(60)
    t.forward(height)
    t.right(120)
    t.forward(height)
    t.left(60)

jump
for height in range (20,70,5):
    t.forward(10)
    jump(height)
    t.forward(10)



#die erste parable height hat nichts mit der zweiten zu tun, heisst die erste ist die Jumpheight, die zweite straightheight oder andere betitlung
t.exitonclick ()
