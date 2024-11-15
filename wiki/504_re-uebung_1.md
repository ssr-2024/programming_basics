# Übung 1: Analyse eines Traumberichts

In dieser Übung wirst du mithilfe von regulären Ausdrücken wichtige Informationen aus einem Traumbericht extrahieren. Verwende die Kenntnisse über das `re`-Modul und die grundlegenden Regex-Funktionen, um die Aufgabe zu lösen.

## Aufgabe

Nutze den folgenden Traumbericht, um die angegebenen Informationen zu extrahieren. Schreibe ein Python-Skript, das folgende Informationen aus dem Bericht herausfiltert:

1. **Datum** des Traums
2. **Emotionen** im Traum
3. **Hauptthemen** des Traums
4. **Orte**, die im Traum vorkommen

**Traumbericht:**

Datum: 2023-11-07

"Ich fand mich in einem alten, verlassenen Haus wieder. Die Wände waren mit alten Gemälden bedeckt, die alle leicht gruselig aussahen. Während ich durch die dunklen Flure ging, hörte ich ein leises Flüstern hinter mir. Plötzlich stand mein alter Schulfreund Jonas vor mir und zeigte auf eine Tür, die halb geöffnet war. Als ich durch die Tür trat, befand ich mich plötzlich in einem weiten Feld unter einem klaren Sternenhimmel. Ich fühlte mich frei, aber auch ein wenig ängstlich. Ich sah ein seltsames Licht am Horizont und begann darauf zuzulaufen, bis ich auf ein tiefes Tal stieß, das ich nicht überqueren konnte. Dann wachte ich auf."

Emotionen: Furcht, Neugier, Freiheit

Hauptthemen: Vergangenheit, Freundschaft, Unbekanntes

Orte: Altes Haus, Flur, Feld, Tal


## Hinweise

- Nutze reguläre Ausdrücke, um die gewünschten Informationen zu finden und zu extrahieren.
- Die erstellung von Dictionaries mit Regex-Mustern benötigt  viel Erfahrung. Bei zu viel Frustration nutze Hilfsmittel wie ChatGTP oder die Musterlösung im Lösungs Abschnitt. 
- Verwende die Funktionen `re.search()`, `re.findall()` oder ähnliche, um gezielt nach den einzelnen Informationen zu suchen.
- Denke daran, die Ergebnisse strukturiert auszugeben.

## Beispiel für die Ausgabe

Nach erfolgreicher Umsetzung deines Codes könnte die Ausgabe so aussehen:

Datum: 2023-11-07 Emotionen: ['Furcht', 'Neugier', 'Freiheit'] Hauptthemen: ['Vergangenheit', 'Freundschaft', 'Unbekanntes'] Orte: ['Altes Haus', 'Flur', 'Feld', 'Tal']

# Lösung

```python

import re

# Traumbericht
dream_report = """
Datum: 2023-11-07

Traumbericht:  
Ich fand mich in einem alten, verlassenen Haus wieder. Die Wände waren mit alten Gemälden bedeckt, die alle leicht gruselig aussahen. Während ich durch die dunklen Flure ging, hörte ich ein leises Flüstern hinter mir. Plötzlich stand mein alter Schulfreund Jonas vor mir und zeigte auf eine Tür, die halb geöffnet war. Als ich durch die Tür trat, befand ich mich plötzlich in einem weiten Feld unter einem klaren Sternenhimmel. Ich fühlte mich frei, aber auch ein wenig ängstlich. Ich sah ein seltsames Licht am Horizont und begann darauf zuzulaufen, bis ich auf ein tiefes Tal stieß, das ich nicht überqueren konnte. Dann wachte ich auf.

Emotionen: Furcht, Neugier, Freiheit

Hauptthemen: Vergangenheit, Freundschaft, Unbekanntes

Orte: Altes Haus, Flur, Feld, Tal
"""

# Dictionary mit Regex-Mustern zur Erkennung der Informationen
patterns = {
    "date": r"Datum:\s+(\d{4}-\d{2}-\d{2})",  # Datum im Format YYYY-MM-DD

    "emotions": r"Emotionen:\s+([A-Za-zäöüÄÖÜß,\s]+)",  # Liste der Emotionen durch Kommas getrennt

    "themes": r"Hauptthemen:\s+([A-Za-zäöüÄÖÜß,\s]+)",  # Liste der Hauptthemen durch Kommas getrennt

    "places": r"Orte:\s+([A-Za-zäöüÄÖÜß,\s]+)"  # Liste der Orte durch Kommas getrennt
}

# Dictionary für die extrahierten Daten, die am Ende ausgegeben werden
data = {}

# Schleife durch das Dictionary mit Regex-Mustern
for key, pattern in patterns.items():
    # Suche das Muster im Traumbericht und speichere das Ergebnis in 'match'
    match = re.search(pattern, dream_report)
    if match:
        # .group(1) gibt die erste erfasste Gruppe im Muster zurück
        # split(",") teilt die gefundene Zeichenkette anhand von Kommas in eine Liste auf
        # .strip() entfernt überflüssige Leerzeichen
        data[key] = [item.strip() for item in match.group(1).split(',')]

# Ausgabe der extrahierten Daten in einem strukturierten Format
print("Extrahierte Traumberichtsdaten:")
for key, value in data.items():
    # key.capitalize() formatiert die Ausgabe, um den Schlüssel groß zu schreiben (z. B. "Date" statt "date")
    print(f"{key.capitalize()}: {value}")
```