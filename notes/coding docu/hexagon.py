# importiere die turtle-library zum zeichnen

import turtle as t

# zeichne 6 mal eine 100 px lange linier und  rotiere um 60 grad um ein Hexagon zu zeichnen
for i in range(6):
    t.forward(100)
    t.right(60)

t.exitonclick()
