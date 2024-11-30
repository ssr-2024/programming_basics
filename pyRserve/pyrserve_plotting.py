# pyRserve Peer-Review Test Script
# Zuallererst: Installiere pyReserve mit `pip install pyRserve`; öffne RStudio und installiere das Package Rserve

# Plotten mit pyReserve über ggplot2

# Schritt 0: Importiere Packages
import pyRserve
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg # um Bild später zu laden

# Schritt 1: Mit Rserve verbinden
conn = pyRserve.connect()

# Schritt 2: Erstelle zufällige Daten, welche eine lineare Abhängigkeit beinhalten
x = np.random.rand(50)
y = 2 * x + np.random.normal(0, 0.1, 50)  # lineare Abhängigkeit mit etwas Rauschen darin 

# Schritt 3a: Erstelle Variablen in R und erstelle eine Funktion, um y umzucodieren (multipliziere dafür y mit -1).
# Variablen x und y in R einlesen
conn.r.x = x
conn.r.y = y


# Funktion erstellen für Umkodierung von y in R
conn.voidEval('conv <- function(y) { y*(-1) }')


# y umkodieren, d.h. Funktion auf y anwenden
conn.r.sapply(conn.r.y, conn.r.conv)

# Schritt 3b: Erstelle mit neuen Variablen x, y ein Dataframe in R
conn.eval('df <- data.frame(x, y)')


# Schritt 4: Verwende ggplot2 in R, um einen Scatterplot mit einer Trendlinie zu erstellen und speichere den Plot
# Tipp: Verwende String-Evaluation
r_code = """
library(ggplot2)
p <- ggplot(df, aes(x=x, y=y)) + 
    geom_point(color='blue') +
    geom_smooth(method='lm', color='red') +
    ggtitle("Scatter Plot with Trend Line")
    ggsave("scatter_plot.png", plot=p) 
"""
conn.eval(r_code)

# Schritt 5: Schliesse die Verbindung zum Server wieder
conn.close() 


# Schritt 6: Plot in Python einbinden
img = mpimg.imread("scatter_plot.png") # Bild in Python laden, in selbem Ordner

# Öffne den Plot in Python, Tipp: `imshow()`
plt.imshow(img)

