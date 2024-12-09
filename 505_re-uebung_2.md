# Übung 3: Validierung und Ersetzung in einem Traumbericht

In dieser Übung wirst du die Funktionen `re.match()` und `re.sub()` verwenden, um den Inhalt eines Traumberichts zu validieren und bestimmte Begriffe zu ersetzen.

## Aufgabe

Du erhältst einen Traumbericht, und deine Aufgabe ist es, Folgendes zu tun:

1. **Überprüfe mit `re.match()`**, ob der Traumbericht mit einem Datum im Format `YYYY-MM-DD` beginnt. Falls ja, fahre mit den weiteren Aufgaben fort. Wenn nicht, gib eine Fehlermeldung aus, die besagt, dass das Format ungültig ist.
2. **Ersetze mit `re.sub()`**:
   - Alle Zahlen durch das Wort „Zahl“, um sensible Daten unkenntlich zu machen.
   - Alle Namen (z. B. „Alex“, „Lena“) durch das Wort „Name“, um die Anonymität zu wahren.

**Traumbericht:**

2023-11-11

Ich war mit Alex, der 25 Jahre alt ist, und Lena auf einem schönen Hügel. Die Sonne schien, und wir fühlten uns sehr glücklich. Überall waren Blumen, und wir konnten weit in die Landschaft schauen. Dann kamen wir zu einem kleinen See, wo wir eine Runde schwammen. Der See war 50 Meter breit und 2 Meter tief. Es war so friedlich, und wir lachten viel. Als es Abend wurde, saßen wir noch am Ufer und schauten zu, wie die Sterne aufgingen.


## Hinweise

- Verwende `re.match()` für die Validierung des Datumsformats am Anfang des Textes.
- Nutze `re.sub()` für die Ersetzungen:
  - Ersetze alle Zahlen (`\d+`) durch das Wort „Zahl“.
  - Ersetze alle Namen (z. B. Wörter mit Großbuchstaben am Anfang, die keine Satzanfänge sind) durch „Name“.

## Erwartete Ausgabe

**Nach erfolgreicher Umsetzung deines Codes könnte die Ausgabe wie folgt aussehen**:

Gültiges Datum: 2023-11-11

Neuer Traumbericht: Zahl-Zahl-Zahl

Traumbericht: Ich war mit Name, der Zahl Jahre alt ist, und Name auf einem schönen Hügel. Die Sonne schien, und wir fühlten uns sehr glücklich. Überall waren Blumen, und wir konnten weit in die Landschaft schauen. Dann kamen wir zu einem kleinen See, wo wir eine Runde schwammen. Der See war Zahl Meter breit und Zahl Meter tief. Es war so friedlich, und wir lachten viel. Als es Abend wurde, saßen wir noch am Ufer und schauten zu, wie die Sterne aufgingen.

**Wenn das Datum ungültig ist, sollte die Ausgabe folgendermaßen aussehen**:

Fehler: Ungültiges Datumsformat. Der Bericht muss mit einem Datum im Format YYYY-MM-DD beginnen.

# Lösung

```python
import re

# Beispieltext des Traumberichts
dream_report = """
2023-11-11

Traumbericht: Ich war mit Alex, der 25 Jahre alt ist, und Lena auf einem schönen Hügel. Die Sonne schien, und wir fühlten uns sehr glücklich. Überall waren Blumen, und wir konnten weit in die Landschaft schauen. Dann kamen wir zu einem kleinen See, wo wir eine Runde schwammen. Der See war 50 Meter breit und 2 Meter tief. Es war so friedlich, und wir lachten viel. Als es Abend wurde, saßen wir noch am Ufer und schauten zu, wie die Sterne aufgingen.
"""

# 1. Überprüfung des Datumsformats am Anfang des Berichts
# `^` stellt sicher, dass das Datum am Anfang steht
if re.match(r"^\d{4}-\d{2}-\d{2}", dream_report):
    # Extraktion des Datums, falls gültig
    date = re.match(r"^\d{4}-\d{2}-\d{2}", dream_report).group(0)
    print(f"Gültiges Datum: {date}")
else:
    # Fehlermeldung bei ungültigem Datumsformat
    print("Fehler: Ungültiges Datumsformat. Der Bericht muss mit einem Datum im Format YYYY-MM-DD beginnen.")
    exit()

# 2. Ersetzen von Zahlen, Namen und Vorbereitung für die neue Ausgabe

# Ersetzen aller Zahlen durch das Wort "Zahl"
# `\d+` findet eine oder mehrere Ziffern
updated_report = re.sub(r"\d+", "Zahl", dream_report)

# Ersetzen aller Namen durch das Wort "Name"
# `[A-Z][a-z]+` sucht nach Wörtern, die mit einem Großbuchstaben beginnen, gefolgt von Kleinbuchstaben
# Diese Regel geht davon aus, dass Namen immer mit einem Großbuchstaben anfangen und keine Satzanfänge sind
updated_report = re.sub(r"\b[A-Z][a-z]+\b", "Name", updated_report)

# Ausgabe des neuen, anonymisierten Traumberichts
print("\nNeuer Traumbericht:")
print(updated_report)
```
