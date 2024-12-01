
import regex as re

dream_report = """
Datum: 07-11-2023


Traumbericht:  
Ich fand mich in einem alten, verlassenen Haus wieder. Die Wände waren mit alten Gemälden bedeckt, die alle leicht gruselig aussahen. Während ich durch die dunklen Flure ging, hörte ich ein leises Flüstern hinter mir. Plötzlich stand mein alter Schulfreund Jonas vor mir und zeigte auf eine Tür, die halb geöffnet war. Als ich durch die Tür trat, befand ich mich plötzlich in einem weiten Feld unter einem klaren Sternenhimmel. Ich fühlte mich frei, aber auch ein wenig ängstlich. Ich sah ein seltsames Licht am Horizont und begann darauf zuzulaufen, bis ich auf ein tiefes Tal stieß, das ich nicht überqueren konnte. Dann wachte ich auf.

Emotionen: Furcht, Neugier, Freiheit

Hauptthemen: Vergangenheit, Freundschaft, Unbekanntes

Orte: Altes Haus, Flur, Feld, Tal
"""
# Dictionary zur Erkennung der notwenidgen Informationen
patterns = {
    "date": r"Datum:\s+(\d{2}-\d{2}-\d{4})",

    "emotions": r"Emotionen:\s+([A-Za-zäöüÄÖÜß,\s]+)",

    "themes": r"Hauptthemen:\s+([A-Za-zäöüÄÖÜß,\s]+)", 

    "places": r"Orte:\s+([A-Za-zäöüÄÖÜß,\s]+)"  
}    
#Erstellen eines Dictionary
data = {}

# Suche nach Mustern im Dictionary
for key, pattern in patterns.items():
    match = re.search(pattern, dream_report)
    if match:
        # .group(1) Angabe darüber welche Grupe behandelt wird
        # split(";") Trennzeichen für Kette
        # .strip() unnötige Leerschläge werden eliminiert
        data[key] = [item.strip() for item in match.group(1).split(',')]

# Ausgabe der extrahierten Daten in einem strukturierten Format
print("Extrahierte Traumberichtsdaten:")
for key, value in data.items():
    # key.capitalize() Grossschreibung bei Ausgabe der Wörter
    print(f"{key.capitalize()}: {value}")


