# Plots mit Matplotlib

Matplotlib ist eine Bibliothek zur Erstellung von 2D-Graphiken in Python. Sie bietet vielfältige Funktionen zur Visualisierung und Anpassung von Diagrammen.

### Installation
Falls Matplotlib noch nicht installiert ist, kann dies über die Kommandozeile erfolgen:
```python
pip install matplotlib
```

### Verwendung

Nach der Installation kann Matplotlib importiert werden:

```python
import matplotlib.pyplot as plt
```



## Figure

Eine Figure ist das gesamte Plot-Fenster, in dem ein oder mehrere Diagramme (Axes) angezeigt werden können.

Die Größe und Auflösung der Figure kann angepasst werden.

### Beispiel: Erstellen einer Figure mit festgelegter Größe

```python
fig = plt.figure(figsize=(8, 6))
print("Figure erstellt")
```

## Axes

Axes sind die einzelnen Diagrammbereiche innerhalb einer Figure.

In einer Figure können mehrere Axes (Diagramme) enthalten sein, um unterschiedliche Daten darzustellen.

### Beispiel: Erstellen eines Diagramms (Axes) mit Daten

```python
fig, ax = plt.subplots()  # Erstellt eine Figure und ein Axes-Objekt
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], label="Lineare Daten")
ax.set_title("Einfaches Diagramm")
ax.set_xlabel("X-Achse")
ax.set_ylabel("Y-Achse")
```


## Subplots

Subplots ermöglichen das Erstellen mehrerer Diagramme in einer Figure.

Dies ist nützlich, wenn verschiedene Datenreihen in einem gemeinsamen Plot-Fenster angezeigt werden sollen.

### Beispiel: Erstellen von zwei Subplots in einer Figure

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))  # Zwei Subplots nebeneinander
ax1.plot([1, 2, 3, 4], [1, 4, 9, 16], label="Quadratisch")
ax1.set_title("Quadratische Daten")
ax2.plot([1, 2, 3, 4], [1, 8, 27, 64], label="Kubisch", color="orange")
ax2.set_title("Kubische Daten")
```


## Styles

Matplotlib bietet eine Vielzahl von Stilen und Anpassungsmöglichkeiten für die Darstellung.

### Farbe

Die Farbe von Linien oder Balken kann mit dem `color`-Argument angepasst werden.

```python
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color="red")  # Setzt die Linie auf Rot
```

### Marker

Marker sind Symbole, die die Datenpunkte in einem Plot hervorheben.

```python
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], marker="o", linestyle="--")  # Kreisförmige Marker mit gestrichelter Linie
```


## Legenden

Legenden identifizieren die verschiedenen Datenreihen in einem Diagramm und werden mit `label` definiert.

`legend()` zeigt die Legende im Plot an.

```python
ax.legend()  # Zeigt die Legende an
ax1.legend()  # Zeigt die Legende im ersten Subplot an
ax2.legend()  # Zeigt die Legende im zweiten Subplot an
```


## Export

Plots können in verschiedene Formate exportiert werden, wie PNG und SVG.

Der Export kann mit `savefig()` durchgeführt werden und unterstützt verschiedene Anpassungsoptionen.

### Beispiel: Exportieren der Figure im PNG- und SVG-Format

```python
fig.savefig("plot.png", dpi=300, bbox_inches="tight")  # Exportiert die Figure als PNG mit 300 dpi
fig.savefig("plot.svg", bbox_inches="tight")           # Exportiert die Figure als SVG
```


## Eigenschaften für Export und Layout

 -----------------------------
 | Eigenschaft | Beschreibung                        | Beispiel            |
 |:------------|:-----------------------------------|:---------------------|
 | `dpi`       | Auflösung des exportierten Bildes   | `dpi=300`           |
 | `figsize`   | Größe der Figure in Zoll (Breite, Höhe) | `figsize=(8, 6)` |

### Beispiel zur Anpassung von DPI und Größe:

```python
fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
ax.plot([1, 2, 3], [1, 4, 9], color="purple")
ax.set_title("Diagramm mit benutzerdefinierten DPI und Größe")
```

# Diagramme anzeigen
```python

plt.show()
```

