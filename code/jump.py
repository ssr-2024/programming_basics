from turtle import forward, left, right, exitonclick

def jump(angle, height):
    left(angle)
    forward(height)
    right(2*angle)
    forward(height)
    left(angle)

forward(100)
jump(60,50)
forward(100)
exitonclick()
