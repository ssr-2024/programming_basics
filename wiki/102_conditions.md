# Bedingungen

In Python können Bedingungen genutzt werden, um Entscheidungen im Code zu treffen. Bedingungen sind Ausdrücke, die zu einem `True` oder `False` Ergebnis führen, wodurch der Code entscheidet, welchen Weg er nehmen soll.

- **Ausdrücke für Bedingungen**: Bedingungen können durch Vergleichsoperatoren (`==`, `!=`, `>`, `<`, `>=`, `<=`) und logische Operatoren (`and`, `or`, `not`) definiert werden.
- **Datentyp des Ergebnisses**: Das Resultat einer Bedingung ist klassischerweise vom Typ `bool`, was entweder `True` oder `False` bedeutet.

Weitere Informationen zu logischen Operatoren findest du hier: [Logische Operatoren](003_operatoren.md#logische-operatoren)

## Wenn-Dann (`if`)

Ein *Wenn-Dann* Szenario wird durch eine `if`-Anweisung dargestellt. Diese Anweisung überprüft, ob eine Bedingung erfüllt ist (`True`). Wenn dies der Fall ist, wird der Codeblock ausgeführt.

### UML-Diagramm für eine *Wenn-Dann* Bedingung:

```Mermaid
flowchart TD
    Start[Start] --> Condition{Bedingung erfüllt?}
    Condition -- Ja --> Action[Aktion ausführen]
    Condition -- Nein --> End[Ende]
```


### Python-Umsetzung:
```python
x = 10

if x > 5:
    print("x ist größer als 5")
```

## Wenn-Dann-Sonst (`if else`)

Ein *Wenn-Dann-Sonst* Szenario wird durch `if` und `else` dargestellt. Wenn die Bedingung `True` ist, wird der `if`-Block ausgeführt, ansonsten der `else`-Block.

### UML-Diagramm für eine *Wenn-Dann-Sonst* Bedingung:

```Mermaid
flowchart TD
    Start[Start] --> Condition{Bedingung erfüllt?}
    Condition -- Ja --> Action1[Aktion 1 ausführen]
    Condition -- Nein --> Action2[Aktion 2 ausführen]
    Action1 --> End[Ende]
    Action2 --> End
```

### Python-Umsetzung:
```python
x = 3

if x > 5:
    print("x ist größer als 5")
else:
    print("x ist kleiner oder gleich 5")
```

## Geschachtelte Wenn-Dann-Sonst Überprüfungen (`if elif ... else`)

Ein *Geschachteltes Wenn-Dann-Sonst* Szenario wird durch `if`, `elif` und `else` dargestellt. Es erlaubt mehrere Bedingungen, die nacheinander überprüft werden. Sobald eine Bedingung `True` ist, wird der zugehörige Block ausgeführt, und die restlichen Bedingungen werden ignoriert.

### UML-Diagramm für eine geschachtelte *Wenn-Dann-Sonst* Bedingung:
``` Mermaid
flowchart TD
    Start[Start] --> Condition1{Bedingung 1 erfüllt?}
    Condition1 -- Ja --> Action1[Aktion 1 ausführen]
    Condition1 -- Nein --> Condition2{Bedingung 2 erfüllt?}
    Condition2 -- Ja --> Action2[Aktion 2 ausführen]
    Condition2 -- Nein --> Action3[Aktion 3 ausführen]
    Action1 --> End[Ende]
    Action2 --> End
    Action3 --> End
```

### Python-Umsetzung:

``` python
x = 7

if x > 10:
    print("x ist größer als 10")
elif x > 5:
    print("x ist größer als 5 aber kleiner oder gleich 10")
else:
    print("x ist kleiner oder gleich 5")
```

