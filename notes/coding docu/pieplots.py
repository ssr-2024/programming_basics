# Zugang via: https://matplotlib.org/stable/plot_types/index.html
# Plot a pie chart

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery-nogrid') # plt.style.use = Funktion zum festlegen eines bestimmten Designs, hier ohne Gitter


# make data
x = [1, 2, 3, 4]
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x))) # plt.get_cmap = Funktion, die eine Farbpalette zurückgibt
# np.linspace ist eine Funktion von NumPy, die eine gleichmäßig verteilte Zahlenreihe erzeugt. Hier wird eine Zahlenreihe von 0.2 bis 0.7 mit einer Länge von len(x) erzeugt. Diese Zahlen repräsentieren Positionen in der Farbkarte.
# Die erzeugte Zahlenreihe wird als Eingabe für die Farbkarte 'Blues' verwendet. Dies bedeutet, dass für jede Zahl in der Zahlenreihe eine entsprechende Farbe aus der Farbkarte ausgewählt wird. Das Ergebnis ist eine Liste von Farben.

# plot
fig, ax = plt.subplots()
ax.pie(x, colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
