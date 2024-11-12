# Mögliche Lösungen zu den Aufgaben
## Plotten mit `pyRserve` über `ggplot2`
```py
# Schritt 0: Importiere Packages
import pyRserve
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg # um Bild später zu laden

# Schritt 1: Mit Rserve verbinden 
conn = pyRserve.connect()

# Schritt 2: Erstelle zufällige Daten, welche eine lineare Abhängigkeit beinhalten. Bspw y = 2*x + z.
x = np.random.rand(50)
y = 2 * x + np.random.normal(0, 0.1, 50)  # Lineare Abhängigkeit mit etwas Rauschen

# Schritt 3: Erstelle Variablen und Dataframe in R
conn.r.x = x
conn.r.y = y
conn.voidEval("data <- data.frame(x=x, y=y)") # Dataframe erstellen, ohne Ausgabe

# Schritt 4: Verwende ggplot2 in R, um einen Scatterplot mit einer Trendlinie zu erstellen und speichere Plot
r_code = """
library(ggplot2)
p <- ggplot(data, aes(x=x, y=y)) + 
    geom_point(color='blue') +
    geom_smooth(method='lm', color='red') +
    ggtitle("Scatter Plot with Trend Line")
    ggsave("scatter_plot.png", plot=p) 
"""
conn.eval(r_code)

# Schritt 5: Plot in Python einbinden
conn.close()  # Verbindung zu Server schliessen

# Plot in Python aufrufen und anzeigen
img = mpimg.imread("scatter_plot.png") # Bild in Python laden, in selbem Ordner
plt.imshow(img)
plt.axis('off')
plt.show()
```

## Berechnung einer ANOVA und anschliessenden Post-Hoc-t-Tests

```py
import pyRserve
import numpy as np
from itertools import combinations # später für Anzahl Kombinationen der t-Tests 

# Schritt 1: Mit Rserve verbinden
conn = pyRserve.connect()

# Schritt 2: Erstelle 3 Gruppen mit randomiserten Daten
group1 = np.random.normal(50, 5, 30)  # Gruppe 1: Mean=50, SD=5
group2 = np.random.normal(55, 5, 30)  # Gruppe 2: Mean=55, SD=5
group3 = np.random.normal(55, 5, 30)  # Gruppe 3: Mean=56, SD=5

# Schritt 3: Erstelle Variablen und Dataframe in R
conn.r.group1 = group1
conn.r.group2 = group2
conn.r.group3 = group3

r_code = """
df <- data.frame(
    value = c(group1, group2, group3),
    group = factor(rep(c('Group1', 'Group2', 'Group3'), each=30))
)
"""
conn.eval(r_code)

# Schritt 4: Führe ANOVA durch, extrahiere p-Wert und gebe ihn aus 
anova_result = conn.eval("summary(aov(value ~ group, data=df))")
anova_p_value = anova_result[0]['Pr(>F)'][0]
print(f"ANOVA p-value: {anova_p_value}")

# Schritt 5: Überprüfe, ob ANOVA signifikant war (p < 0.05)
alpha = 0.05
if anova_p_value < alpha:
    print("ANOVA ist signifikant. Durchführung von Post-Hoc-t-Tests mit Bonferroni-Korrektur.\n")
    
    # Definiere Dictionary für spätere Gruppenpaare für paarweise t-Tests
    groups = {'Gruppe1': group1, 'Gruppe2': group2, 'Gruppe3': group3}
    
    # Berechne paarweise t-Tests und wende Bonferroni-Korrektur an
    num_tests = 3  # drei Tests paarweise
    bonferroni_alpha = alpha / num_tests  # Bonferroni-Korrektur
    
    # Durchführung paarweiser t-Tests und Anwendung der Bonferroni-Korrektur mit anschliessender Resultat-Ausgabe
    for (g1, g2) in combinations(groups.keys(), 2): # Kombinationen der drei Gruppen
        
        # Berechne t-Tests und extrahiere p-Wert
        conn.r.a = groups[g1]
        conn.r.b = groups[g2]
        t_test_result = conn.eval("t.test(a,b)")
        p_value = t_test_result['p.value']
        
        # Wende Bonferroni-Korrektur auf p-Wert an
        corrected_p_value = p_value * num_tests
        corrected_p_value = min(corrected_p_value, 1)  # p-Wert kann nicht grösser 1 sein
        
        # Gebe jeweilige Resultate aus
        print(f"Paarweiser t-Test zwischen {g1} und {g2}:")
        print(f"Originaler p-Wert: {p_value}")
        print(f"Bonferroni-korrigierter p-Wert: {corrected_p_value}")
        
        if corrected_p_value < alpha:
            print(f"Resultat: Signifikanter Unterschied zwischen {g1} und {g2} nach Korrektur gefunden.\n")
        else:
            print(f"Resultat: Kein signifikanter Unterschied zwischen {g1} und {g2} nach Korrektur gefunden.\n")
else:
    print("ANOVA ist nicht signifikant. Keine weiteren Tests nötig.")

# Schliesse Verbindung mit Rserve
conn.close()

# Schliesse Verbindung zu Server ganz
conn.shutdown()

```
