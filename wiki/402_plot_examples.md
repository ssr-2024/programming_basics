# Plotten: Beispiele und Variationen

## Pie Plot
```py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

series = pd.Series(3 * np.random.rand(4), index=["a", "b", "c", "d"], name="Klubmitglieder")


series.plot.pie(
        labels=["Frauen", "Männer", "Jugendliche", "Kinder"],
        colors=["r", "g", "b", "c"],
        autopct="%.2f",
        fontsize=20,
        figsize=(6, 6),
        )
plt.savefig("./media/pieplot.png")
plt.show()
````
![pieplot](../media/plots/pie_plot.png)


## Box Plots
Einen Boxplot kann mit der Funktion `Series.plot.box()`, `DataFrame.plot.box()`, `DataFrame.boxplot()` oder mit `plt.boxplot()` erstellt werden.

```py
z.B. 
>> import matplotlib.pyplot as plt
>> import pandas as pd
>> import numpy as np
>> df = pd.DataFrame(np.random.rand(10, 5), columns=["A", "B", "C", "D", "E"])
>> plt.boxplot('A', data=df)
>> plt.show()
```
![boxplots.png](../media/plots/box_plot.png)

## Bar Plot
```py
# Libraries
import numpy as np
import matplotlib.pyplot as plt

# Make a random dataset:
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(bars))

# Create bars
plt.bar(y_pos, height)

# Create names on the x-axis
plt.xticks(y_pos, bars)

# Show graphic
plt.show()
```

![BarPlot](../media/plots/bar_plot.png)

## Histogramme 

Histogramm erstellen mit `DataFrame.plot.hist()` und `Series.plot.hist()`

```py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df4 = pd.DataFrame(
    {
        "a": np.random.randn(1000) + 1,
        "b": np.random.randn(1000),
        "c": np.random.randn(1000) - 1,
    },
    columns=["a", "b", "c"],
)

plt.figure();
df4.plot.hist(alpha=0.5);
```
Möglichkeit Histogramme zu stappeln & Bin-size anzupassen: 
```py
plt.figure()

df4.plot.hist(stacked=True, bins=20)
```
![histogram](../media/plots/histogram_plot.png)


## Area Plot

```py
#Library import
import numpy as np
import matplotlib.pyplot as plt

# Erstelle Daten für x & y
x = [1, 2, 3, 4, 5, 6]
y = [2, 7, 5, 7, 2, 9]

# Area plot
plt.fill_between(x, y)
plt.show()
```
### Umgesetztes Beispiel für Area Plot
<img src="../media/plots/area_plot.png" alt="Bild von Area Plot" title="Beispiel Area Plot" />

[Source und weitere Beispiele](https://www.python-graph-gallery.com/area-plot/)


## Density Plot

```py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
fig = plt.figure()
ax = fig.gca()


ax.set_xlabel("Value")
ax.set_ylabel("Density")
ax.set_title("Density")

ser = pd.Series(np.random.randn(1000))
ser.plot.kde()

ax.figure.savefig("../media/plots/density_plot.png")
# ax.figure.savefig("./plot_export.jpeg")

plt.show()
```
![density plot](../media/plots/density_plot.png)


## Scatter-Plot

Beispiel:
```py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame(np.random.rand(50, 4), columns=["a", "b", "c", "d"])

df["species"] = pd.Categorical(
    ["setosa"] * 20 + ["versicolor"] * 20 + ["virginica"] * 10
)


# 2 Kategorien
#df.plot.scatter(x="c", y="d", color="Green", label="Group 2", ax=ax)
#Unterteilung in Gruppen
df.plot.scatter(x="a", y="b", c="species", cmap="viridis", s=50)
# Punktegrösse zeigt es an
#df.plot.scatter(x="a", y="b", s=df["c"] * 200)
plt.show()`
```

![scatterplot](../media/plots/scatter_plot.png)
![Scatterplot2](../code/Scatterplot_example.png)

## 3D-Plot

Matplotlib erlaubt auch 3D-Plots, wahlweise mit einer Projektion auf verschiedene Flächen.
![Ein 3D-Plot mit Konturen](../media/plots/3d_plot.png)

Das Beispiel kann so erzeugt werden:

```py 
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

ax = plt.figure().add_subplot(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)

# Plot the 3D surface
ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)

# Plot projections of the contours for each dimension.  By choosing offsets
# that match the appropriate axes limits, the projected contours will sit on
# the 'walls' of the graph.
ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
ax.contour(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

ax.set(xlim=(-40, 40), ylim=(-40, 40), zlim=(-100, 100),
       xlabel='X', ylabel='Y', zlabel='Z')
ax.figure.savefig("../media/plots/3d_plot.png")
plt.show()
```
