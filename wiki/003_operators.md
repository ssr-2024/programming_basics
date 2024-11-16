# Operatoren
Operatoren in Python werden verwendet, um Operationen auf Variablen und Werten auszuführen. Sie ermöglichen Berechnungen, Vergleiche, logische Prüfungen, Zuweisungen und weiteres.

## Arithmetische Operatoren
| Operator | Beschreibung | Beispiel          |
|:---------|:-------------|:------------------|
| `+`      |    Addition          |         1 `+` 1 = 2       |
| `-`     |    Subtraktion           |          9 `-` 5 = 4      |
| `*`      |Multiplikation              |    5 `*` 3 =15             |
| `/`      | Division             |         54 `/` 9 = 6        |
| `//`     |     Division durch ganze Zahlen         |           13 `//` 5 = 2     |
| `**`     |  Potenzierung            |     4 `**` 3 = 64            |
| `%`      | Restwert             |           7 `%` 2 = 1      |


## Vergleichsoperatoren
| Operator | Beschreibung | Beispiel          |
|:---------|:-------------|:------------------|
| `<`      |       kleiner als        |                76 `<` 67 ergibt 'false' |
| `<=`     |  kleiner oder gleich            |          4 `<=` 4  ergibt 'true'       |
| `>`      |      grösser als        |           5 `>`2 ergibt 'true'        |
| `>=`     | grösser oder gleich             | 3 `>=` 4        ergibt 'false'         |
| `==`     |       gleicher Wert       |             3 `==`3 ergibt 'true'     |
| `!=`     |   ungleicher Wert           | 2 `!=` 2   ergibt 'false'              |

## Logische Operatoren
Logische Operatoren werden verwendet um logische Operationen durchzuführen
| Operator | Beschreibung | Beispiel          |
|:---------|:-------------|:------------------|
| `and`    |      Vergleichs-*und*        |    true **and** false  ergibt 'false'             |
| `or`     |         Vergleichs-*und*     | true **or** false ergibt 'true'                 |
| `not`    |         Vergleichs-*nicht*     | **not** false ergibt 'true'                 |

## Membership Operator
Dient zur Überprüfung um zu sehen ob ein Wert in einem weiteren Wert vorhanden ist.
| Operator | Beschreibung | Beispiel          |
|:---------|:-------------|:------------------|
| `in`     |    prüft ob im Wert beinhaltet           | 'z' in 'Bernie Sanders' ergibt 'false'                  |
| `not in` |  prüft ob im Wert  nicht beinhaltet            |   's' in 'Granit Xhaka' ergibt   'true'             |

## Identitätsoperator
Der Identitäsoperator wird verwendet, um zu prüfen, ob zwei Variablen auf dasselbe Objekt im Speicher verweisen und überprüft die Identität von Objekten, nicht deren Wert.
| Operator | Beschreibung | Beispiel          |
|:---------|:-------------|:------------------|
| `is`     |      Vergleicht Werte auf Gleichheit        |   'c' `is`   'k' wenn definiert wurde dass 'c' und 'k' denselben Wert besitzen ergibt 'true'             |
| `is not` |       Vergleicht Werte auf Differenzen       |    'c' `is not` 'k' wenn 'c' und'k' nicht den denselben Wert besitzen ergibt     'true'         |
