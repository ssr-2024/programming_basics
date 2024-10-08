# Modules and Packages

## Module
Module sind Files welche man importieren kann.
<br>
Zum Beispiel:
```Python
import turtle as t
```
Meist enthalten diese Files Funktionsdefinitionen, welche man dann im anderen File nutzen kann. Es können aber auch Funktionen aufgerufen werden, welche z.B. zum Setup von bestimmten Prozessen genutzt werden können.

## Packages

Packages sind Ordner mit Modulen. Diese können installiert werden mit pip install
<br>
Beispiel:
```cmd
pip install art
```
Dieses Package enthält verschiedene Funktionen welche zur Darstellung von Text nützlich sind.
<br>
Beispiel
```Python
from art import *
tprint("Test")
```
Gibt aus:
<br>
<img src="images\test.png">
