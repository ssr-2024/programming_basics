# Fragen im Buch 
![Buch](https://automatetheboringstuff.com/)
## Kapitel 1
1. `*`,`-`,`/`,`+` sind Operatoren
2. `spam` ist Variable, `'spam'` ist String
3. integer, float, string
4. ein Ausdruck ist Kombination von Werten und Operatoren, evaluieren schlussendlich zu einem Wert
5. Ausdruck kann zu einzelnem Wert evaluiert werden, bei Statement muss dies nicht unbedingt sein. 
6. `bacon` wird 20 zugewiesen, `bacon + 1` weist der Variable allerdings keinen neuen Wert zu, folglich  immernoch 20
7. beides zu `'spamspamspam'`
8. Variablen dürfen nicht mit Zahlen im Namen beginnen
9. `int()`,`float()`,`str()` um umzuwandeln
10. `99` ist kein string

## Kapitel 2
1. `True` und `False`, Grossbuchstabe essentiell
2. `and`, `or`, `not`
3.  |and|True|False|
    |----|-----|-----|
    |True|True|False|
    |False|False|False|

    |or|True|False|
    |----|-----|-----|
    |True|True|True|
    |False|True|False|

    |not||
    |----|-----|
    |True|False|
    |False|True|

4.  False
    False
    True
    False
    False
    True
5. `==`, `!=`,`>`,`<`,`>=`,`<=`
6. `==` vergleichend, `=` zuweisend
7. um Fluss eines Programms zu kontrollieren, evaluiert zu einem boolschen Wert
8. Innerhalb des if-Statements und `print('bacon')` und `print('ham')`
9.  ```py
    if spam == 1:
        print('Hello')
    elif spam == 2:
        print('Howdy')
    else:
        print('Greetings!')
    ```
10. CRTL+C
11. `break`, um aus Schleife auszubrechen, `continue`, um an Anfang zu springen
12. kein Unterschied
13. ```py
    for i in range(1, 11):
        print(i)
    
    i = 1
    while i <= 10:
        print(i)
        i = i + 1
    ```
14. mit `spam.bacon()`

## Kapitel 3 
1. um Code wiederzuverwenden, Komplexitätsverringerung
2. bei Aufruf der Funktion
3. `def`-Anweisung definiert eine Funktion
4. Eine Funktion besteht aus der `def`-Anweisung und dem Code in ihrer `def`-Klausel. Ein Funktionsaufruf ist das, was die Programmausführung in die Funktion bewegt, und der Funktionsaufruf wird Wert evaluiert
5. Es gibt einen globalen Gültigkeitsbereich, und ein lokaler Gültigkeitsbereich wird jedes Mal erstellt, wenn eine Funktion aufgerufen wird.
6. Wenn eine Funktion zurückkehrt, wird der lokale Gültigkeitsbereich zerstört, und alle darin enthaltenen Variablen werden vergessen.
7. Ein Rückgabewert ist der Wert, den ein Funktionsaufruf liefert. Wie jeder Wert kann ein Rückgabewert als Teil eines Ausdrucks verwendet werden.
8. Wenn es keine `return`-Anweisung für eine Funktion gibt, ist ihr Rückgabewert `None`.
9. Eine `global`-Anweisung zwingt eine Variable in einer Funktion, sich auf die globale Variable zu beziehen.
10. Der Datentyp von `None` ist `NoneType`.
11. Diese `import`-Anweisung importiert ein Modul namens `areallyourpetsnamederic`. 
12. Diese Funktion könnte mit `spam.bacon()` aufgerufen werden.
13. Platziere die Codezeile, die möglicherweise einen Fehler verursacht, in einem `try`-Block.
14. Der Code, der potenziell einen Fehler verursachen könnte, kommt in den `try`-Block. Der Code, der ausgeführt wird, wenn ein Fehler auftritt, kommt in den `except`-Block.

## Kapitel 4
1. Der leere Listenwert, der eine Liste ist, die keine Elemente enthält. Dies ist ähnlich wie `''` der leere Zeichenkettenwert ist.

2. `spam[2] = 'hello'` (Beachte, dass der dritte Wert in einer Liste an Index 2 liegt, da der erste Index 0 ist.)

3. `'d'` (Beachte, dass `'3' * 2` die Zeichenkette `'33'` ist, die an `int()` übergeben wird, bevor sie durch `11` geteilt wird. Dies ergibt letztendlich `3`. Ausdrücke können überall verwendet werden, wo Werte verwendet werden.)

4. `'d'` (Negative Indizes zählen vom Ende her.)

5. `['a', 'b']`

6. `1`

7. `[3.14, 'cat', 11, 'cat', True, 99]`

8. `[3.14, 11, 'cat', True]`

9. Der Operator für die Listenkonkatenation ist `+`, während der Operator für die Replikation `*` ist. (Das ist das Gleiche wie bei Zeichenketten.)

10. Während `append()` nur Werte am Ende einer Liste hinzufügt, kann `insert()` sie überall in der Liste einfügen.
11. Die `del`-Anweisung und die `remove()`-Listenmethode sind zwei Möglichkeiten, Werte aus einer Liste zu entfernen.

12. Sowohl Listen als auch Zeichenketten können an `len()` übergeben werden, haben Indizes und Slices, können in `for`-Schleifen verwendet, verkettet oder repliziert werden und können mit den Operatoren `in` und `not in` verwendet werden.

13. Listen sind veränderbar; sie können Werte hinzugefügt, entfernt oder geändert haben. Tupel sind unveränderlich; sie können überhaupt nicht geändert werden. Außerdem werden Tupel mit Klammern `( und )` geschrieben, während Listen eckige Klammern `[ und ]` verwenden.

14. `(42,)` (Das abschließende Komma ist obligatorisch.)

15. Die `tuple()`- und `list()`-Funktionen, jeweils.

16. Sie enthalten Referenzen auf Listenwerte.

17. Die `copy.copy()`-Funktion erstellt eine flache Kopie einer Liste, während die `copy.deepcopy()`-Funktion eine tiefe Kopie einer Liste erstellt. Das bedeutet, dass nur `copy.deepcopy()` alle Listen innerhalb der Liste dupliziert.

## Kapitel 5 
1. Zwei geschweifte Klammern: `{}`

2. `{'foo': 42}`

3. Die in einem Wörterbuch gespeicherten Elemente sind ungeordnet, während die Elemente in einer Liste geordnet sind.

4. Du erhältst einen `KeyError`-Fehler.

5. Es gibt keinen Unterschied. Der `in`-Operator überprüft, ob ein Wert als Schlüssel im Wörterbuch existiert.

6. `'cat' in spam` prüft, ob es einen Schlüssel `'cat'` im Wörterbuch gibt, während `'cat' in spam.values()` überprüft, ob es einen Wert `'cat'` für einen der Schlüssel in `spam` gibt.

7. `spam.setdefault('color', 'black')`

8. `pprint.pprint()`

## Kapitel 6
1. Escape-Zeichen repräsentieren Zeichen in Zeichenketten (`strings`), die ansonsten schwierig oder unmöglich in den Code einzugeben wären.

2. `\n` ist ein Zeilenumbruch; `\t` ist ein Tabulator.

3. Das Escape-Zeichen `\\` stellt ein Rückschrägstrich-Zeichen dar.

4. Das einfache Anführungszeichen in `Howl's` ist in Ordnung, da du doppelte Anführungszeichen für den Anfang und das Ende der Zeichenkette verwendet hast.

5. Mehrzeilige Zeichenketten (`multiline strings`) erlauben dir, Zeilenumbrüche in Zeichenketten zu verwenden, ohne das Escape-Zeichen `\n` zu nutzen.

6. Die Ausdrücke werten zu Folgendem aus:

   - `'e'`
   - `'Hello'`
   - `'Hello'`
   - `'lo, world!'`
   
7. Die Ausdrücke werten zu Folgendem aus:

   - `'HELLO'`
   - `True`
   - `'hello'`

8. Die Ausdrücke werten zu Folgendem aus:

   - `['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']`
   - `'There-can-be-only-one.'`

9. Die Methoden `rjust()`, `ljust()` und `center()` für Zeichenketten, jeweils.

10. Die Methoden `lstrip()` und `rstrip()` entfernen Leerzeichen am linken bzw. rechten Ende einer Zeichenkette.
