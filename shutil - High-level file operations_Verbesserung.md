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


## Ignorieren von bestimmten Dateien/Verzeichnissen beim Kopieren 
Mit shutil.copytree() kannst du bestimmte Dateien oder Verzeichnisse beim Kopieren ignorieren, indem du den ignore-Parameter verwendest. Der ignore-Parameter erwartet eine Funktion, die zwei Argumente annimmt: den Pfad zum Verzeichnis und eine Liste der darin enthaltenen Namen (Dateien und Unterverzeichnisse). Die Funktion sollte eine Liste der Namen der Dateien und Verzeichnisse zurückgeben, die du ignorieren möchtest.

## Backup und Archivierung
shutil unterstützt das Erstellen und Extrahieren von Archivdateien wie ZIP oder TAR, was für Backup- und Archivierungsprozesse von zentraler Bedeutung ist. Mit Funktionen wie shutil.make_archive() und shutil.unpack_archive() können ganze Verzeichnisse in ein kompaktes Archiv gepackt oder entpackt werden.

## Verwalten von Dateienystemen und Datenmigration
In großen Projekten oder bei der Arbeit mit mehreren Systemen müssen Daten zwischen verschiedenen Verzeichnissen oder sogar zwischen verschiedenen Servern verschoben werden. Mit Funktionen wie shutil.copy2() (die auch Metadaten wie Erstellungs- und Änderungszeit beibehält) können Entwickler sicherstellen, dass Daten korrekt migriert werden, ohne wichtige Informationen zu verlieren.


## Abänderung des Besitzers einer Datei
Die Funktion shutil.chown() wurde in Python 3.3 eingeführt und bietet eine einfache Möglichkeit, den Besitzer (Owner) und die Gruppe (Group) einer Datei zu ändern. Im Gegensatz zur os.chown()-Funktion, die nur die Benutzer- und Gruppen-IDs erwartet, kann shutil.chown() auch den Benutzernamen und Gruppennamen direkt akzeptieren.

### Warnung
Zum Ändern des Besitzers oder der Gruppe einer Datei benötigst du in der Regel Administratorrechte oder Root-Rechte, insbesondere wenn du den Besitzer auf einen anderen Benutzer änderst.

Auf Windows-Systemen funktioniert shutil.chown() nicht wie unter Unix-basierten Systemen. Windows verwaltet Dateibesitz und -berechtigungen anders, sodass du Windows-spezifische Methoden wie icacls oder die Windows-API verwenden musst, um den Besitzer zu ändern.

## Die vorgestellten Funktionen von shutil, deren Beschreibung sowie ein dazugehöriges Beispiel, sind in der untenstehenden Tabelle ersichtlich.

| Funktion               | Beschreibung                                  | Beispiel                                       |
|------------------------|----------------------------------------------|-----------------------------------------------|
| `shutil.move()`        | Verschieben von Log-Dateien in Archivverzeichnis.                          | `shutil.move('/path/to/logfile.log', '/path/to/archive/logfile.log')`           |
| `shutil.move()`        | Verschiebt oder benennt eine Datei/Ordner um.| `shutil.move('src/', 'dst/')`                 |
| `shutil.copytree()`      | Funktion um Datei zu ignorieren.    | `shutil.copytree(src, dst, ignore=ignore_patterns)`                 |
| `shutil.make_archive()`      | Erstellen eines Archives aus einem Verzeichnis.    | `shutil.make_archive('/path/to/backup', 'zip', '/path/to/work_dir')`                 |
| `shutil.unpack_archive()`      | Entpacken eines Archives.    | `shutil.unpack_archive('archive_name.zip', '/path/to/extract_to')`                 |
| `shutil.copy2()`      | Migration von Dateien zwischen verschiedenen Servern oder Systemen, wobei Metadaten beibehalten werden.    | `shutil.copy2('/path/to/source/file.txt', '/path/to/destination/file.txt')`                 |
| `shutil.copystat()`      | Metadaten einer Datei auf eine andere kopieren.    | `shutil.copystat(src, dst)`                 |
| `shutil.chown()`      | Besitzer (Owner) und die Gruppe (Group) einer Datei ändern.    | `shutil.chown(file_path, user='newuser', group='newgroup')`                 |


## Empfohlene Pakete für das benutzen von shutil
Diese weiteren Pakete erweisen sich als nützlich wenn es darum geht eine vollständige Lösung für das Arbeiten mit Dateien, Prozessen und Verzeichnissen zu finden. Wenn mit 'shutil' gearbeitet wird, sind diese anderen Module oft hilfreich, um zusätzliche Flexibilität und Funktionalität zu bieten.

### import os
Wird oft verwendet, um mit Dateipfaden und Betriebssystemfunktionen zu arbeiten, die nicht direkt von shutil abgedeckt werden (z.B. Pfadoperationen, Umgebungsvariablen).

### import subprocess
Ermöglicht das Ausführen und Interagieren mit externen Prozessen, was hilfreich ist, wenn mit Programmen oder Skripten gearbeitet wird, die nicht direkt in Python geschrieben sind.

### import glob
Wird verwendet, um Dateien mit bestimmten Mustern zu finden, was nützlich ist, wenn mit mehreren Dateien gearbeitet wird, die einer bestimmten Namenskonvention folgen.


### Weitere relevante Informationen zu shutil - High-level file operations sind auffindbar auf: https://docs.python.org/3/library/shutil.html#shutil.copytree 
