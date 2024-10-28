# Operatoren

In Python sind Operatoren Symbole, die bestimmte Operationen an Variablen und Werten durchführen.

## Arithmetische Operatoren
Arithmetische Operatoren werden verwendet, um mathematische Operationen durchzuführen.

| Operator | Beschreibung                  | Beispiel             |
|:---------|:------------------------------|:---------------------|
| `+`      | Addition                      | `2 + 3  # Ausgabe: 5`|
| `-`      | Subtraktion                   | `5 - 2  # Ausgabe: 3`|
| `*`      | Multiplikation                | `2 * 3  # Ausgabe: 6`|
| `/`      | Division                      | `10 / 2 # Ausgabe: 5.0`|
| `//`     | Ganzzahl-Division             | `10 // 3 # Ausgabe: 3`|
| `**`     | Potenzierung                  | `2 ** 3  # Ausgabe: 8`|
| `%`      | Modulo (Rest der Division)    | `10 % 3  # Ausgabe: 1`|

## Vergleichsoperatoren

Vergleichsoperatoren vergleichen zwei Werte und geben einen Wahrheitswert (`True` oder `False`) zurück.

| Operator | Beschreibung                  | Beispiel            |
|:---------|:------------------------------|:--------------------|
| `<`      | Kleiner als                   | `2 < 3  # Ausgabe: True`|
| `<=`     | Kleiner oder gleich            | `3 <= 3 # Ausgabe: True`|
| `>`      | Größer als                    | `5 > 2  # Ausgabe: True`|
| `>=`     | Größer oder gleich             | `5 >= 6 # Ausgabe: False`|
| `==`     | Gleich                         | `2 == 2 # Ausgabe: True`|
| `!=`     | Ungleich                       | `2 != 3 # Ausgabe: True`|

## Logische Operatoren
Logische Operatoren werden verwendet, um logische Ausdrücke zu verknüpfen.

| Operator | Beschreibung                  | Beispiel              |
|:---------|:------------------------------|:----------------------|
| `and`    | Logisches UND                  | `(2 < 3) and (4 > 1)  # Ausgabe: True`|
| `or`     | Logisches ODER                 | `(2 > 3) or (4 > 1)   # Ausgabe: True`|
| `not`    | Logische Negation              | `not (2 > 3)          # Ausgabe: True`|

## Membership Operatoren
Membership-Operatoren prüfen, ob ein Element in einer Sequenz vorhanden ist.

| Operator | Beschreibung                  | Beispiel                   |
|:---------|:------------------------------|:---------------------------|
| `in`     | Prüft, ob ein Element enthalten ist | `3 in [1, 2, 3]  # Ausgabe: True`|
| `not in` | Prüft, ob ein Element nicht enthalten ist | `4 not in [1, 2, 3] # Ausgabe: True`|

## Identitätsoperatoren
Identitätsoperatoren prüfen, ob zwei Objekte identisch sind (auf die gleiche Speicheradresse verweisen).

| Operator | Beschreibung                  | Beispiel                     |
|:---------|:------------------------------|:-----------------------------|
| `is`     | Prüft, ob zwei Objekte identisch sind | `a is b  # Ausgabe: True, wenn a und b auf dasselbe Objekt verweisen`|
| `is not` | Prüft, ob zwei Objekte nicht identisch sind | `a is not b  # Ausgabe: True, wenn a und b unterschiedliche Objekte sind`|
