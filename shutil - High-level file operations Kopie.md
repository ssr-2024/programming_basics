# shutil - High-level file operations

Die ‘shutil’-Bibliothek in Python bietet eine Sammlung nützlicher Funktionen zur Verwaltung von Dateien und Verzeichnissen.
Sie ermöglicht das Kopieren, Verschieben, Umbenennen und Löschen von Dateien sowie das Rekursive Bearbeiten ganzer Verzeichnisbäume.
Wichtige Funktionen wie ‘shutil.copy()’, ‘shutil.move()’ und ‘shutil.rmtree()’ vereinfachen die Arbeit mit Dateisystemen, indem sie eine einfache Schnittstelle für häufige Aufgaben bieten.
Darüber hinaus unterstützt ‘shutil’ auch das Erstellen von Archivdateien (z.B. ZIP oder TAR) und das Extrahieren von Archiven.
Diese Funktionen machen ‘shutil’ zu einem vielseitigen Werkzeug, das Entwicklern hilft, mit Datei- und Ordnersystemen auf effiziente Weise zu interagieren.

## Warnung
Auch die höherwertigen Datei-Kopierfunktionen (shutil.copy(), shutil.copy2()) können nicht alle Dateimetadaten kopieren.
Auf POSIX-Plattformen bedeutet das, dass der Dateibesitzer und die Gruppe verloren gehen, ebenso wie ACLs (Access Control Lists). 
Auf macOS werden die Ressourcengabel und andere Metadaten nicht verwendet. 
Das bedeutet, dass Ressourcen verloren gehen und Dateityp- sowie Ersteller-Codes nicht korrekt sind. 
Auf Windows werden Dateibesitzer, ACLs und alternative Datenströme nicht kopiert.

## Praktische Relevanz
Die praktische Relevanz der shutil-Bibliothek in Python liegt in ihrer Fähigkeit, eine Vielzahl von Dateisystemoperationen einfach und effizient durchzuführen. Insbesondere für Aufgaben, die häufig in Skripten zur Automatisierung von Systemadministration, Datenverwaltung oder Backup-Prozessen auftauchen, bietet shutil eine leistungsstarke und benutzerfreundliche Schnittstelle. Hier sind einige konkrete Anwendungsbeispiele und Szenarien, in denen shutil eine wesentliche Rolle spielt:

## Automatisierung von Dateioperationen
In vielen Automatisierungsskripten müssen Dateien und Verzeichnisse regelmässig kopiert, verschoben oder gelöscht werden. Die Funktionen von shutil, wie shutil.copy(), shutil.move() und shutil.rmtree(), erleichtern diese Operationen erheblich, da sie einfache Methoden bereitstellen, um diese Aufgaben ohne manuelle Eingriffe durchzuführen.

### Beispiel:
Ein Skript, das automatisch log-Dateien von einem Server in ein Archivverzeichnis verschiebt und gleichzeitig die alten Dateien löscht, um Speicherplatz zu sparen.

```
    import shutil
    
    # Verschieben von Log-Dateien in das Archiv-Verzeichnis
    shutil.move('/path/to/logfile.log', '/path/to/archive/logfile.log')

    # Löschen eines Verzeichnisses (mit Inhalt)   
    shutil.rmtree('/path/to/old_logs')
```

Am obigen Beispiel wurde mittels dem source path zur Datei zurückgegriffen, mittels eingabe des file name kann ebenfalls auf die erwünschte Datei zurückgegriffen werden.
Die Destination einer zweiten Datei kann ebenfalls mittels path 

## Ignorieren von bestimmten Dateien/Verzeichnissen beim Kopieren 
Mit shutil.copytree() kannst du bestimmte Dateien oder Verzeichnisse beim Kopieren ignorieren, indem du den ignore-Parameter verwendest. Der ignore-Parameter erwartet eine Funktion, die zwei Argumente annimmt: den Pfad zum Verzeichnis und eine Liste der darin enthaltenen Namen (Dateien und Unterverzeichnisse). Die Funktion sollte eine Liste der Namen der Dateien und Verzeichnisse zurückgeben, die du ignorieren möchtest.

### Beispiel:
Nehmen wir an, du möchtest alle .txt- und .log-Dateien aus einem Verzeichnis ausschließen, wenn du es mit shutil.copytree() kopierst. Du könntest eine Funktion definieren, die diese Dateitypen ignoriert.

```
    import shutil
    import os

    # Funktion, um bestimmte Dateien zu ignorieren
    def ignore_patterns(src, names):

    # Rückgabe einer Liste der Dateien, die ignoriert werden sollen
    return [name for name in names if name.endswith('.txt') or name.endswith('.log')]

    # Quelle und Zielverzeichnis
    src = '/path/to/source_dir'
    dst = '/path/to/destination_dir'

    # Kopiere das Verzeichnis, aber ignoriere .txt und .log Dateien
    shutil.copytree(src, dst, ignore=ignore_patterns)
```

### Alternatives Beispiel:
Du kannst auch reguläre Ausdrücke verwenden, um eine flexiblere Ignorierlogik zu implementieren. Dies ist besonders nützlich, wenn du eine Vielzahl von Dateimustern oder komplexe Bedingungen hast.

```
    import shutil
    import re

    # Funktion, die mithilfe eines regulären Ausdrucks Dateien ignoriert
    def ignore_regex(src, names):

        # Hier wird nach Dateien gesucht, die mit '.txt' oder '.log' enden
        return [name for name in names if re.search(r'\.txt$|\.log$', name)]

    src = '/path/to/source_dir'
    dst = '/path/to/destination_dir'

    # Kopiere das Verzeichnis und ignoriere alle .txt und .log Dateien
    shutil.copytree(src, dst, ignore=ignore_regex)
```


## Backup und Archivierung
shutil unterstützt das Erstellen und Extrahieren von Archivdateien wie ZIP oder TAR, was für Backup- und Archivierungsprozesse von zentraler Bedeutung ist. Mit Funktionen wie shutil.make_archive() und shutil.unpack_archive() können ganze Verzeichnisse in ein kompaktes Archiv gepackt oder entpackt werden.

### Beispiel:
Regelmässige Backups eines Arbeitsverzeichnisses in eine ZIP-Datei.

```    
    import shutil

    # Erstellen eines ZIP-Archivs aus einem Verzeichnis
    shutil.make_archive('/path/to/backup', 'zip', '/path/to/work_dir')
```

### Alternatives Beispiel:
Aus den erstellten Archiven können auch wieder Dateien herausgezogen werden, heisst ein Archiv entpackt werden.

```
    import shutil

    # Entpacken eines ZIP-Archivs
    shutil.unpack_archive('archive_name.zip', '/path/to/extract_to')
```

## Verwalten von Dateienystemen und Datenmigration
In großen Projekten oder bei der Arbeit mit mehreren Systemen müssen Daten zwischen verschiedenen Verzeichnissen oder sogar zwischen verschiedenen Servern verschoben werden. Mit Funktionen wie shutil.copy2() (die auch Metadaten wie Erstellungs- und Änderungszeit beibehält) können Entwickler sicherstellen, dass Daten korrekt migriert werden, ohne wichtige Informationen zu verlieren.

### Beispiel:
Migration von Dateien zwischen verschiedenen Servern oder Systemen, wobei Metadaten beibehalten werden.

```
    import shutil

    # Kopieren einer Datei inklusive Metadaten
    shutil.copy2('/path/to/source/file.txt', '/path/to/destination/file.txt')
```

### Alternatives Beispiel:
Die Funktion shutil.copystat() in Python wird verwendet, um die Metadaten einer Datei auf eine andere zu kopieren. Diese Metadaten umfassen verschiedene Dateiattribute wie Zugriffszeit, Modifikationszeit und Berechtigungen (Permissions), aber nicht den Inhalt der Datei selbst.

```
    import shutil

    # Pfade zur Quell- und Ziel-Datei
    src = 'source.txt'
    dst = 'destination.txt'

    # Kopiere die Metadaten von source.txt nach destination.txt
    shutil.copystat(src, dst)
```

## Abänderung des Besitzers einer Datei
Die Funktion shutil.chown() wurde in Python 3.3 eingeführt und bietet eine einfache Möglichkeit, den Besitzer (Owner) und die Gruppe (Group) einer Datei zu ändern. Im Gegensatz zur os.chown()-Funktion, die nur die Benutzer- und Gruppen-IDs erwartet, kann shutil.chown() auch den Benutzernamen und Gruppennamen direkt akzeptieren.

```
    import shutil

    # Pfad zur Datei
    file_path = 'path/to/your/file.txt'

    # Ändere den Besitzer und die Gruppe der Datei
    shutil.chown(file_path, user='newuser', group='newgroup')

    print(f"Besitzer und Gruppe von {file_path} wurden geändert.")
```

## Warnung
Zum Ändern des Besitzers oder der Gruppe einer Datei benötigst du in der Regel Administratorrechte oder Root-Rechte, insbesondere wenn du den Besitzer auf einen anderen Benutzer änderst.

Auf Windows-Systemen funktioniert shutil.chown() nicht wie unter Unix-basierten Systemen. Windows verwaltet Dateibesitz und -berechtigungen anders, sodass du Windows-spezifische Methoden wie icacls oder die Windows-API verwenden musst, um den Besitzer zu ändern.


## Empfohlene Pakete für das benutzen von shutil
Diese weiteren Pakete erweisen sich als nützlich wenn es darum geht eine vollständige Lösung für das Arbeiten mit Dateien, Prozessen und Verzeichnissen zu finden. Wenn mit 'shutil' gearbeitet wird, sind diese anderen Module oft hilfreich, um zusätzliche Flexibilität und Funktionalität zu bieten.

### import os
Wird oft verwendet, um mit Dateipfaden und Betriebssystemfunktionen zu arbeiten, die nicht direkt von shutil abgedeckt werden (z.B. Pfadoperationen, Umgebungsvariablen).

### import subprocess
Ermöglicht das Ausführen und Interagieren mit externen Prozessen, was hilfreich ist, wenn mit Programmen oder Skripten gearbeitet wird, die nicht direkt in Python geschrieben sind.

### import glob
Wird verwendet, um Dateien mit bestimmten Mustern zu finden, was nützlich ist, wenn mit mehreren Dateien gearbeitet wird, die einer bestimmten Namenskonvention folgen.


### Weitere relevante Informationen zu shutil - High-level file operations sind auffindbar auf: https://docs.python.org/3/library/shutil.html#shutil.copytree 
