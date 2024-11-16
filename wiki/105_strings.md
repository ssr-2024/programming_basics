# Strings
Das Eingeben von String-Variablen ist auf Python sehr einfach. Der Text, der als String gespeichert werden soll, wird entweder in einfache ('...') oder doppelte ("...") Anführungszeichen gesetzt. Allerdings kann das verwendete Anführungszeichen nicht innerhalb des Strings auftauchen, ohne einen Fehler zu verursachen. Dies lässt sich umgehen, indem man das jeweils andere Anführungszeichen verwendet oder einen Escape-Zeichen nutzt. 
Ein Escape-Zeichen besteht aus einem Backslash ( \ ), gefolgt von dem gewünschten Zeichen.
Im folgenden Beispiel wird der String nicht durch das zweite Anführungszeichen beendet, da es mit einem Backslash davor maskiert wurde.
```python

    dog_name = 'Elena\'s dog is called Jaxx'
```
## Gross- Kleinschreibung
Python unterscheidet zwischen der Gross- und Kleinschreibung. Der String 'Ralf' entspricht nicht 'ralf'.Wenn die Gross- oder Kleinschreibung keine Bedeutung hat, kann der gesamte String entweder in Klein- oder Grossbuchstaben umgewandelt werden.

## Formatierte Ausgabe `f'2 * 2 = {2 * 2}'`
Die formatierte Ausgabe in Python, die durch f-Strings ermöglicht wird, ist eine bequeme und lesbare Möglichkeit, Variablen oder Ausdrücke direkt in Strings einzufügen. Dies geschieht durch Voranstellen des Strings mit einem kleinen `f` und das Einschliessen der Variablen oder Ausdrücke in geschweifte Klammern `{}` innerhalb des Strings.

## Beispiele
```python
    name = 'Thierry'
    age = 57

    print('Hello my name is ' + name + ' and I am ' + str(age) + ' years old.')
```
Ausgabe:
```python
Hello my name is Thierry and I am 57 years old.
```


###
###
###
```python
    name = 'Thierry'
    age = 58

    print(f'Hello my name is {name} and on monday I will be  {age + 1} years old.')
```
Ausgabe:
```python
Hello my name is Thierry and on mondy I will be 58 years old.
```