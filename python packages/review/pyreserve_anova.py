# Schritt 0: Importiere Packages
import pyRserve
import numpy as np
from itertools import combinations # später für Anzahl Kombinationen der t-Tests 

# Schritt 1: Mit Rserve verbinden
conn = pyRserve.connect()

# Schritt 2: Erstelle 3 Gruppen mit randomiserten Daten
group1 = np.random.normal(50, 5, 30)  # Gruppe 1: Mean=50, SD=5
group2 = np.random.normal(55, 5, 30)  # Gruppe 2: Mean=55, SD=5
group3 = np.random.normal(50, 5, 30)  # Gruppe 3: Mean=55, SD=5

# Schritt 3: Erstelle Variablen und Dataframe in R, beachte dabei, dass die Gruppenzugehörigkeit als Faktoren definiert werden sollten
# 3a: Variablen in R einlesen
conn.r.group1 = group1
conn.r.group2 = group2
conn.r.group3 = group3

# 3b: Dataframe erstellen
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

# Ausführliche Erklärung der Notation [0]['Pr(>F)'][0]
'''
Die Notation [0]['Pr(>F)'][0] wird verwendet, um durch die verschachtelte Struktur des ANOVA-Ergebnisses in R zu navigieren und den p-Wert zu extrahieren. Hier ist eine Aufschlüsselung, was jeder Teil macht:
anova_result[0]: Greift auf das erste Element des ANOVA-Ergebnisses zu, das typischerweise eine Liste enthält, die die ANOVA-Tabelle beinhaltet.
['Pr(>F)']: Greift auf die Spalte mit dem Namen 'Pr(>F)' in der ANOVA-Tabelle zu, die die p-Werte für die F-Tests enthält.
[0]: Greift auf den ersten p-Wert in der Spalte 'Pr(>F)' zu, der dem p-Wert für den gesamten F-Test der ANOVA entspricht.
Diese Notation ermöglicht es, den p-Wert aus der verschachtelten Struktur des ANOVA-Ergebnisses zu extrahieren und in Python zu verwenden.'''

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
        t_test_result = conn.eval("t.test(a, b)")
        p_value = t_test_result['p.value']
        
        # Wende Bonferroni-Korrektur auf p-Wert an
        corrected_p_value = p_value * num_tests
        corrected_p_value = min(corrected_p_value, 1)  # p-Wert kann nicht grösser 1 sein
        
        # Gebe jeweilige Resultate aus
        print(f"t-Test paarweise zwischen {g1} und {g2}:")
        print(f"p-Wert im Original: {p_value}")
        print(f"p-Wert korrigiert nach Bonferroni: {corrected_p_value}")
else:
    print("ANOVA ist nicht signifikant. Keine weiteren Tests nötig.")

# Schliesse Verbindung zu Server ganz
conn.shutdown()

# Ergebnis:
'''
ANOVA p-value: 1.2118032434983213e-06
ANOVA ist signifikant. Durchführung von Post-Hoc-t-Tests mit Bonferroni-Korrektur.

t-Test paarweise zwischen Gruppe1 und Gruppe2:
p-Wert im Original: 2.9068038746156957e-06
p-Wert korrigiert nach Bonferroni: 8.720411623847086e-06
t-Test paarweise zwischen Gruppe1 und Gruppe3:
p-Wert im Original: 0.35216033184600715
p-Wert korrigiert nach Bonferroni: 1
t-Test paarweise zwischen Gruppe2 und Gruppe3:
p-Wert im Original: 6.307551100083978e-05
p-Wert korrigiert nach Bonferroni: 0.0001892265330025193
'''