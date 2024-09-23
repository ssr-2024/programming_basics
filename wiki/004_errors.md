# Fehlermeldungen

Bekannte Fehlermeldungen:

- [NameError](#NameError)


## NameError
`NameError: name 'a' is not defined`
## Ursache
Aufruf einer Variable oder Funktion, die im aktuellen Skript nicht definiert ist.
## Mögliche Ursachen
- Variable/Funktion erst später im Skript definiert?
- Fehlender Import eines Python-Moduls, welches die Variable/Funktion definiert?
## Beispiel
```py
print(variable_not_defined_before)
```