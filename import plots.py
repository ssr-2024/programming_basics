
import matplotlib.pyplot as plt

# Gegebene Werte
x = [1, 2, 3, 4, 5, 6]
y = [3, 5, 7, 9, 1, 2]

# Erstelle ein Figure-Objekt und Subplots
fig, axs = plt.subplots(2)  # 2 Zeilen, 1 Spalte

# Erster Subplot
axs[0].plot(x, y, 'g+-')  # 'g+-' steht für grüne Linie mit Datenpunkten als +
axs[0].set_title('Erster Subplot')
axs[0].set_ylabel('y-Werte')
axs [0].set_xlabel ('x-Werte')

# Zweiter Subplot (hier kannst du andere Daten oder den gleichen Plot verwenden)
axs[1].plot(x, y, 'b-o')  # 'b-o' steht für blaue Linie mit Punkten
axs[1].set_title('Zweiter Subplot')
axs[1].set_ylabel('y-Werte')
axs[1].set_xlabel('x-Werte')

# Zeige die Plots an
plt.tight_layout()  # Optimiert den Abstand zwischen den Subplots
plt.show()
