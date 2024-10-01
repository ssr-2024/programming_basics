import turtle as t

def jump(angle = 60, height = 50):
    t.left(angle)
    t.forward(height)
    t.right(2*angle)
    t.forward(height)
    t.left(angle)

t.Screen().screensize(1000, 1000)
t.Screen().setworldcoordinates(0, -500, 1000, 500)
for i in range(10):  
    t.forward(50)
    jump(60,50+5*i)
    t.forward(50)

t.exitonclick()