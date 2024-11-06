import matplotlib.pyplot as plt

# Beispiel-Daten
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Erstellen des Histogramms mit einer benutzerdefinierten Farbe
plt.hist(data, bins=5, color='#2E8B57', edgecolor='black')

# Hinzufügen von Titeln und Beschriftungen
plt.title('Histogramm mit benutzerdefinierter Farbe')
plt.xlabel('Werte')
plt.ylabel('Häufigkeit')

# Anzeigen des Histogramms
plt.show()
