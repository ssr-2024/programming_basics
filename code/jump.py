#importiere aus turtle
from turtle import forward, right, exitonclick

def jump(angle:float , height:float):
    """funktion, um Zacken zu generieren,
    mit entsprechendem Winkel und Länge anpassbar
    """
    right(-angle)
    forward(height)
    right(2*angle) #=180-2*(90-angle)
    forward(height)
    right(-angle)
 
#generiere 5 Zacken, welche grösser werden
for i in range(50,100,10):
    forward(10)
    jump(80,i)

exitonclick()