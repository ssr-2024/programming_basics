#plot beispiele
#Subplots

import matplotlib.pyplot as plt
import numpy as np

# Beispiel-Daten
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Erstelle ein Figure-Objekt und Subplots
fig, axs = plt.subplots(2) # 2 Zeilen, 1 Spalte

# Erster Subplot
axs[0].plot(x, y1, 'r') # 'r' steht für rote Linie
axs[0].set_title('Sinusfunktion')
axs[0].set_ylabel('sin(x)')

# Zweiter Subplot
axs[1].plot(x, y2, 'b') # 'b' steht für blaue Linie
axs[1].set_title('Kosinusfunktion')
axs[1].set_ylabel('cos(x)')
axs[1].set_xlabel('x')

# Zeige die Plots an
plt.tight_layout() # Optimiert den Abstand zwischen den Subplots
plt.show()
