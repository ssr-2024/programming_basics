# Plots
Ziel ist es Daten die man gesammelt und eventuell bearbeitet hat zu visualisieren.
## Figure
Graphisches Fenster in dem der Plot angezeigt wird.
## Axes

Objekt in dem die Daten abgebildet werden. 
![alt text](images/plots_overview.png)
- Titel: Titel des Plots
- ylabel: Beschriftung y-Achse
- xlabel: Beschriftung x-Achse
- axis: x- und y-Achse
### Subplots
Subplots ermöglichen es, mehrere Plots in einer einzigen Abbildung zu erstellen. Dies ist nützlich, um verschiedene Datensätze oder verschiedene Ansichten desselben Datensatzes nebeneinander darzustellen.

Beispiele:
```python
import matplotlib.pyplot as plt

# Erstellen von Subplots
fig, axs = plt.subplots(2, 2)

# Plot in der ersten Zeile, ersten Spalte
axs[0, 0].plot([1, 2, 3], [1, 4, 9])
axs[0, 0].set_title('Plot 1')

# Plot in der ersten Zeile, zweiten Spalte
axs[0, 1].plot([1, 2, 3], [1, 2, 3])
axs[0, 1].set_title('Plot 2')

# Plot in der zweiten Zeile, ersten Spalte
axs[1, 0].plot([1, 2, 3], [1, 0, 1])
axs[1, 0].set_title('Plot 3')

# Plot in der zweiten Zeile, zweiten Spalte
axs[1, 1].plot([1, 2, 3], [3, 2, 1])
axs[1, 1].set_title('Plot 4')

plt.tight_layout()
plt.show()
```

## Styles
Man kann den Style der Plots individuell anpassen.
### Farbe
Mit `color` kann die Farbe angepasst werden.
```Python
plt.plot([1, 2, 3], [4, 5, 6], color='red')
plt.show()
```
### Marker
Durch `Marker` können die Symbole durch die z.B. Datenpunkte gezeichnet werden angepasst werden

Beispiel:
```Python
plt.plot([1, 2, 3], [4, 5, 6], marker='o')
plt.show()
```


## Legenden
Legenden können genutzt werden, um verschiedene Datenreihen zu kennzeichen:
```Python
plt.plot([1, 2, 3], [4, 5, 6], label='Datenreihe 1')
plt.plot([1, 2, 3], [6, 5, 4], label='Datenreihe 2')
plt.legend()
plt.show()
```

## Export

Fromate (png, svg)

| Eigenschaft | Beschreibung | Beispiel |
|:------------|:-------------|:---------|
| `dpi`       |      Auflösung des Bildes        |     `plt.savefig('plot.png', dpi=300)`     |
| `figsize`   |    Grösse der Abbildung in Zoll          |   `plt.figure(figsize=(10, 5))`       |
