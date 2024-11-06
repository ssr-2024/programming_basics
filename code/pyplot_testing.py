import numpy as np
import matplotlib.pyplot as plt
'''

fig = plt.figure()            # erstelle figure
ax = fig.gca()                 # get current axes (gca)
ax.plot([9, 1, 1, 1, 7], 'r-', label='Plot 1')    # -  für durchgezogene Linie in Rot
ax.plot([2, 2, 2, 6, 2], 'g--', label='Plot 2')   # -- für gestrichelte Linie in Grün
ax.plot([3, 3, 3, 3, 3], 'b+-', label='Plot 3')   # +  Datenpunkte als Pluszeichen in Blau
ax.plot([4, 2, 4, 4, 8], 'yo--', label='Plot 4')  # o  Datenpunkte als Kreise in Gelb mit gestrichelter Linie
ax.grid()                         # add background grid
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Primary Plot')
ax.set_xticks(np.arange(0, 10, 0.2))

ax.set_xlim(-3, 15)            # x-Achse von -3 bis 15
ax.set_ylim(0, 5)              # y-Achse von 0 bis 5
ax.autoscale()                 # Zurücksetzen auf automatische Skalierung

ax.legend(loc='lower center', ncol=2)  # bis zu 2 Labels in einer Zeile

ax.figure.set_size_inches(6.3, 3.54)  # Größe in Zoll (1 cm / 2.54 = 1 Zoll)
ax.figure.set_dpi(100)               # Punkte pro Zoll (dpi); Größe * dpi = Pixel

ax.figure.savefig("plot_export.png")   # Export als Portable Network Graphic (PNG)
ax.figure.savefig("plot_export.svg")   # Export als Scalable Vector Graphic (SVG)


plt.show()
'''

import matplotlib.pyplot as plt
import numpy as np

# Daten für den Area Plot
x = np.linspace(0, 10, 100)
y1 = np.sin(x) + 1.5
y2 = np.cos(x) + 1

# Erstellung der Figur und der Achsen
fig, ax = plt.subplots()
ax.fill_between(x, y1, color="skyblue", alpha=0.4, label="sin(x) + 1")
ax.fill_between(x, y2, color="sandybrown", alpha=0.4, label="cos(x) + 1")

# Einstellung der Größe und DPI für den Export
ax.figure.set_size_inches(6.3, 3.54)
ax.figure.set_dpi(100)

# Achsenbeschriftungen und Titel
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Area Plot von sin(x) + 1 und cos(x) + 1')
ax.legend(loc='upper right')

# Hintergrundgitter aktivieren
ax.grid()


plt.show()
