# Python Notizen

Notizen zum Arbeitsauftrag:

Python (Anaconda) auch für Machine Learning und Data Science interessant!

``` help([object]) ``` für informationen über objekt(z.B. Variablentyp, Funktion, etc.)

## Datentypen




## Variablen

Die Funktion ``` type(var) ``` gibt Typ der Variable aus. 

Definieren verschiedener Variablentypen:
```py
x = 1     #integer definieren

y = 1.0   #float definieren

a = True  #boolean definieren (wobei True gleich 1, False gleich 0)

z1 = 'hello' #string definieren 
z2 = 'world'
z = z1 + ' ' + z2 #string zusammenfügen zu "hello world"

b = z1 x y #array definieren

print(z)   #gibt "hello world" in commandozeile aus

```
Beachte: Falls in String ```" "``` enthalten sein sollen, verwende ```' ' ``` zum Definieren, sonst auch mit ```" "``` möglich. 

## Einlesen von Tastatureingaben

```py
name = input('Enter your name:') #fragt nach Namen mit anschliessender Eingabe(bestätigen mit Enter), welche "name" zugewiesen wird
```
Die Funktion ```input()``` kann auch ohne Text verwendet werden

```py
x = int(input('Enter a number: ')) #fragt nach Nummer und wandelt String in Integer um 
```
Funktioniert auch mit Funktionen ```float(var)``` und ```str(var)```. Achtung: Bei nicht umwandelbarem Variablentyp, kann Laufzeitfehler auftreten!

**Rechner erstellen:**
```py
first_number = int(input('Type the first number: ')) ;\ #fragt zuerst nach erster Nummer
second_number = int(input('Type the second number: ')) ;\ #danach nach zweiter
print("The sum is: ", first_number + second_number) #Ausgabe der Summe
```
```;\``` lässt **Code Zeile für Zeile ausführen**


## Operatoren

Zur Verwendung von Operatoren braucht es folgende Stuktur: 
```py
<left side> <operator> <right side>
```

**Arithmetische Operatoren**
- ```+``` Additionsoperator
- ```-``` Subtraktionsoperator
- ```*``` Multiplikationsoperator
- ```/``` Divisionsoperator
- ```%``` Moduloperator
- ```//``` Floor-Divisionsoperator (teilt durch rechte Seite und rundet auf ganze Zahl ab)
- ```**``` Exponentenoperator

**Zuweisungsoperatoren**
- ```=``` für einfache Zuweisung
- ```+=``` für Addition um den Wert der rechten Seite
- ```-=``` für Subtraktion um den Wert der rechten Seite
- ```*=``` für Mulitiplikation um den Wert der rechten Seite
- ```/=``` für Division durch den Wert der rechten Seite

**Mathematische Operatoren**
- ```==``` Abfrage, ob gleich
- ```!=``` Abfrage, ob nicht gleich
- ```<``` Abfrage, ob kleiner als
- ```>``` Abfrage, ob grösser als
- ```<=``` Abfrage, ob kleiner gleich
- ```>=``` Abfrage, ob grösser gleich
--> vor allem für Abfragen ```while```, ```if```, etc.

**Boolsche Operatoren**
- ```and``` und
- ```or```  oder
- ```not``` nicht

## Datumsangaben

Importieren zuerst Modul ```date``` folgendermassen: 
```py
from datetime import date
```

Heutiges Datum abrufen: 
```py
Datum = date.today() #abrufen und zuweisen
print(Datum) #ausgeben
```
Wichtig: Falls ```Datum``` mit String ausgegegen werden soll, muss Variable mit ```str()``` konvertiert werden!

## if, elif und else
Anders als gewohnt von Java und C++ ist ```:``` entscheidend, keine Klammern ```{```, ```}```

```py
a = 27
b = 93
if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else: 
    print ("a is equal to b")
```
## Strings

Falls in String ```" "``` enthalten sein sollen, verwende ```' ' ``` zum Definieren, sonst auch mit ```" "``` möglich.

Falls in String ```'``` enthalten sein sollen, verwende ```""" """ ``` zum Definieren.

Falls String mehrzeiliger Text sein sollen, verwende ```""" """ ``` und Absätze oder ```\n```

**Splitten von Strings**
Verschiedene Möglichkeiten:
```py
print("temperatures and facts about the moon".title()) #.title() gibt mit grossem Anfangsbuchstaben zurück

temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures.split() #.split() gibt einzelne Wörter zurück
print(temperatures_list)

temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures.split('\n') #gibt einzelne Teile nach Zeilenwechsel zurück
print(temperatures_list)
```

**Suche nach Zeilenfolge in String**
```py
print("Moon" in "This text will describe facts about the Moon") #Ausgabe entweder True oder False

#Ausgabe der Position mit .find(" ") (-1 falls nicht gefunden)
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))

#Anzahl Vorkommen mit .count(" ")
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))
```

**Gross-/Kleinschreibung**

```py
print("The Moon And The Earth".lower()) # ganzen String in Kleinbuchstaben

print("The Moon And The Earth".upper()) # ganzen String in Grossbuchstaben
```

**Überprüfen von Inhalten**

Möglichkeiten
- ``` .isnumeric()```
- ``` .isdecimal()```
- ```.startswith(" ")```
- ```.endswith(" ")```

Beispiel: 
```py
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split(): #überprüfe für jedes item in aufgesplitem String(-Array), ob numerisch
    if item.isnumeric():
        print(item)
```
Achtung: -30 wird allerdings nicht als numerisch erkannt!

**Transformieren von Text**

- ```.lower()``` bietet sich zur Normaliserung eines Texts an
- ```.replace( )``` zum Ersetzen
- ```.join()``` zum Zusammensetzen

Beispiele: 
```py
print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C")) #Celsius wird mit C ersetzt

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts)) #gibt Sätze mit Leerzeichen dazwischen zurück
```

**Formatierung mit Prozentzeichen**

Mittels Platzhalter:
```py
# möglich(aber mit mehreren Variablen eher fehleranfällig):
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)

print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))
```
Mittels ```format()```-Methode:
```py
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))

mass_percentage = "1/6"
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))

#für bessere Lesbarkeit auch möglich:
mass_percentage = "1/6"
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(moon="Moon", mass=mass_percentage))

```

f-Zeichenfolgen: (am elegantesten)
```py
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")
```

## Mathematische Funktionen

- ```abs(x)``` Absolutbetrag von x 
- ```round(x)``` mathematisches Runden
- ```ceil(x)``` Aufrunden
- ```floor(x)``` Abrunden

Beachte: ```ceil``` und ```floor``` müssen zuerst importiert werden!
```py
from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)
```

## Listen 

**Erstellen von Listen:**
```py
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
```
**Zugriff auf Element** 
mittels ```planet[index]```, wobei erstes Element mit Index ```0``` und auch negativer Index möglich (z.B. ```-1``` letztes Element, ```-2``` zweitletztes usw.)

**Länge von Liste bestimmen**

```py
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")
```

**Hinzufügen eines Elements**

```py
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")
```

**Entfernen des letzten Elements**

```py
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")
```

**Finden des Index eines Elements**

```py
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")
```

**min und max in Listen**
Falls Liste aus Zahlen besteht möglich: 
```py
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 124054 # in Newtons, on Earth

print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "N")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "N")
```

**Bearbeiten von Listendaten**

Aufteilen:
```py
planets_after_earth = planets[3:8] # neue Liste mit Elementen 4 bis 9 aus alter liste planets
print(planets_after_earth)
```

Verknüpfen:
```py
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
```

Sortieren: 

```py
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
sorted_moons = regular_satellite_moons.sort() #Alphabetisch sortiert
inv_sorted_moons = regular_satellite_moons.sort(reverse=True) #Alphabetisch rückwärts sortiert
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
```
Achtung: ```.sort()``` ändert die aktuelle Liste!

## Schleifen

while-Schleifen:
```py
while <condition>:
    # code here
```

cooles Beispiel mit Listen: 
```py
# Create the variable for user input
user_input = ''
# Create the list to store the values
inputs = []

# The while loop
while user_input.lower() != 'done':
    # Check if there's a value in user_input
    if user_input:
        # Store the value in the list
        inputs.append(user_input)
    # Prompt for a new value
    user_input = input('Enter a new value, or done when done')
```


for-Schleifen: 

```py
for i in range(k): #für i von 0 bis k
    #code
```
```py
countdown = [4, 3, 2, 1, 0]
for number in countdown: #Variante mit Liste
    print(number)
print("Blast off!! 🚀")
```

Es können ```continue``` und ```break``` verwendet werden, um an Anfang zu springen oder Schleife zu beenden

## Wörterbücher

**Erstellen von Wörterbuch**
```py
planet = {
    'name': 'Earth',
    'moons': 1
}
```
**Zugriff auf Wörterbuchwerte**
```py
# planet['name'] is identical to using planet.get('name')
print(planet['name'])
```
Vorteil von ```.get(' ')``` ist, dass falls Wert nicht vorhanden ist, ein None ausgegeben wird und kein Key-Error!

**Ändern von Wörterbuchwerten**

```py
planet['name'] = 'Makemake'

# No output: name is now set to Makemake.
```

**Hinzufügen von Schlüsseln**

```py
planet['orbital period'] = 4333

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }
```

**Entfernen von Schlüsseln**

```py
planet.pop('orbital period')

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }
```

**Komplexe Datentypen**
Es ist möglich ein Wörterbuch im Wörterbuch zu erstellen:
```py
# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }

#Zugriff darauf:
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')
```

**Abrufen aller Schlüssel und Werte**
mittels ```keys``` alle Schlüssel

```py
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')
```

**Überprüfen, ob Schlüssel vorhanden**

```py
if 'december' in rainfall:
    #code
```

**Zugriff auf alle Werte**
mittels ```values```, ohne Ausgabe der Schlüssel, z.B.:
```py
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter.')
```

## Funktionen

**Definieren von Funktionen ohne expliziten Rückgabewert**
```py
def rocket_parts():
    print("payload, propellant, structure")
```

**Definieren von Funktionen mit expliziten Rückgabewert**
```py
def rocket_parts():
    return "payload, propellant, structure" #mit return
output = rocket_parts()
output
```

**Funktionen mit erforderlichen Argumenten**
z.B. ```any()```, benötigt Argumente, sonst wird Error ausgegeben:
```py
any([True, False, False])
```

**Funktionnen mit optionalen Argumenten**
z.B. ```str()```, benötigt nicht unbedingt Argument: 
```py
print(str()) #gibt einfach " " aus
```

**Erfordern von Argumenten**
```py
def days_to_complete(distance, speed): #hier mit mehreren Argumenten
    hours = distance/speed
    return hours/24
```

**Schlüsselwortargumente**
Bei Schlüsselwortargumenten kann ein "Standardwert vordefiniert werden. Dieser kann bei der Ausführung, muss aber nicht mehr (um-)definiert werden. 
```py
from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

arrival_time() #nimmt standardwert von hours
arrival_time(hours = 10) #verwendet anderen Wert für hours
```

Kombinieren von Argumenten ist natürlich problemlos möglich! Allerdings müssen zuerst Argumente und dann Schlüsselargumente definiert werden! 

**Variable Argumente**
Es besteht die Möglichkeit, Argumente zu verwenden, ohne diese und deren Anzahl im Vorhinein weiter zu definieren(auch 0 möglich): 
```py
def variable_length(*args):
    print(args)
```
Argumente werden hierbei als Tupel gespeichert 

**Variable Schlüsselwortargumente**
```py
def variable_length(**kwargs):
    print(kwargs)
```
Schlüsselwortargumente werden als Wörterbuch gespeichert

Frage, die sich mir stellt: Wie kann ich überprüfen, dass Variable in dem Format ist, wie ich sie gerne hätte?


## Fehlerbehandlung

**Try- und Except-Blöcke**

```py
try: #ausnahmeblock
     open('config.txt')
except FileNotFoundError: #falls Datei nicht gefunden wird, gebe Nachricht aus
     print("Couldn't find the config.txt file!") 
```

Die Blöcke können auch gruppiert werden: 
```py
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")
```

Ausserdem kann man nach Fehlermeldungsnummer unterscheiden: 
```py
try:
    open("config.txt")
except OSError as err:
     if err.errno == 2:
         print("Couldn't find the config.txt file!")
     elif err.errno == 13:
        print("Found config.txt but couldn't read it")
```

**Auslösen von Ausnahmen**

mittels ```raise```: 

```py
def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"
```

Beispiel für TypeError:
```py
def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypeError will be raised only if it isn't the right type 
            # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"
```

## Module
- in Python ganzes Programm als Modul interpretiert(d.h. bei Import wird auch Code ausgeführt, der nicht in Funktion enthalten ist)
- kann auf unterschiedliche Arten importiert (und danach abgerufen) werden:

```py
#importieren spezifischer funktionen
from ispw_functions import forward, right, found
#abrufen der funktionen
forward(200)
```
```py
#importieren aller funktionen
from ispw_functions import *
#abrufen der funktionen
forward(200)
```
```py
#importieren der Modulreferenz, as optional, dann Zugriff mit vollem Namen 
import ispw_functions as ispw
#abrufen der funktionen
ispw.forward(200)
```

Falls in Package (Ordner mit Modulen):

```py 
#importiere sqrt aus Modul algebra, welche in Package math_helpers liegt
from math_helpers.algebra import sqrt
#aufrufen der funktion
sqrt(100)
```
Beachte dabei, dass der Standort des Ordners wichtig ist!

- Package installieren: via Terminal mit `pip install package_name`

## Laufzeit ermitteln

mit `time`-Modul

## Numpy 

```py 
import numpy as np 

np_array_2d = np.array([[1,2,3],[4,5,6]])
```
Vorteil: 
- direkte Berechnungen mit arrays, nicht mehr über einzelne Indizes --> geringere Komplexität 
- bei unserem Beispiel Faktor 2000 schneller!

