# Plots
In Python ermöglicht die Verwendung von Plots eine grafische Darstellung von Daten. Dies hilft dabei, komplexe Datenmuster zu vereinfachen und anschaulich zu präsentieren. Auffällige Muster, die in den rohen Daten möglicherweise schwer erkennbar sind, lassen sich durch grafische Darstellungen schnell identifizieren. Plots sind daher ein effektives Mittel, um Daten in einer klareren und verständlicheren Form darzustellen.
## Figure
Die Figure in Plot-Modulen repräsentiert den gesamten Bereich, in dem die Plots angezeigt werden. Sie kann eine oder mehrere Plots nebeneinander platzieren. 
## Axes
Innerhalb einer Figure werden spezifische Diagrammbereiche definiert, die als Axes bezeichnet werden. Jedes dieser Axes lässt sich individuell anpassen und gestalten, wodurch der Nutzer die gesamte figure flexibel und nach seinen Wünschen anpassen kann.
### Subplots
Subplots ermöglichen es, mehrere Diagramme innerhalb einer figure nebeneinander anzuzeigen. Dies erleichtert beispielsweise den Vergleich zwischen zwei oder mehr Grafiken und macht es einfacher, Muster oder Trends übersichtlich darzustellen und schneller zu erkennen.
## Styles
Styles ermöglichen die Anpassung des Aussehen und die Formatierung von DataFrames, bevor sie angezeigt werden. Mit Hilfe von Pandas-Stilen können visuelle Elemente wie Farben, Schriftarten, Zellenhintergründe, Ränder und vieles mehr modifiziert werden, um die Daten ansprechender oder übersichtlicher darzustellen.
### Farbe
'Farbe' ermöglicht die Anpassung und das Hervorheben von visuellen Erscheinugsbilder von Daten. 'Farbe' kann verwendet werden, um bestimmte Zellen, Zeilen oder Spalten in einem DataFrame hervorzuheben, sodass sie leichter erkannt und interpretiert werden können. Dies kann besonders hilfreich sein, um Muster, Ausreißer oder Trends in den Daten schnell zu identifizieren.
### Marker
Farbe kann verwendet werden, um bestimmte Zellen, Zeilen oder Spalten in einem DataFrame hervorzuheben, sodass sie leichter erkannt und interpretiert werden können. Dies kann besonders hilfreich sein, um Muster, Ausreißer oder Trends in den Daten schnell zu identifizieren.Unter folgendem Link befindet sich eine Auflistung aller verwendbarer Marker (https://matplotlib.org/stable/api/markers_api.html).
## Legenden
Legenden sind ebenfalls ein wichtiger Bestandteil jeder grafischen Darstellung und tragen entscheidend zum Verständnis bei. Sie erklären die verschiedenen Elemente eines Plots und sorgen dafür, dass die dargestellten Daten von Personen, die nicht mit der Erstellung des Plots vertraut sind, richtig interpretiert werden können. Ohne eine Legende wäre es schwierig, die Bedeutung der einzelnen Darstellungen zu erkennen.
## Export
Um einen Plot erfolgreich zu exportieren, muss zunächst die Grösse festgelegt werden. Dies kann mit dem Befehl `ax.figure.set_size_inches()` stattfinden. Um die Auflösung in Inches oder Pixeln zu bestimmen, wird zusätzlich der Befehl `ax.figure.set_dpi()` genutzt. Die folgende Tabelle zeigt dies noch einmal anschaulich.
Fromate (png, svg)

| Eigenschaft | Beschreibung | Beispiel |
|:------------|:-------------|:---------|
| `dpi`       |      Pixel pro Inch        |  `ax.figure.set_dpi(1000)`   |
| `figsize`   |     Grösser der Abbildung in Inch         | `ax.figure.set_size_inches(2.3, 4.5)`       |
