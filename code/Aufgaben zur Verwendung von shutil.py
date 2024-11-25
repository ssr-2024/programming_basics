### Aufgaben zur Verwendung von shutil

### Du solltest  die wichtigsten Funktionen von shutil kennen und nun anwenden.

### Aufgabe 1: (Stell dir vor du musst deinen Laptop wechseln, weil dein Clubmate im Rucksack ausgelaufen ist und dein Laptop Bildschirm ist nun futsch) Erstelle einen ZIP-Ordner aus deinem persönlichen/geforkten Github Repository, welchen du lokal speicherst damit du die nach dem Abschluss des Programming Basics einen ZIP Ordner hast auf welchen du schnell zurückgreifen kannst. 
### Voraussetzungen: Gehe in zwei Schritten vor, 1. Clonen deines Repositorys (mit git); 2. Komprimieren des Repository in eine ZIP Datei (mit shutil)


### Aufgabe 2: (Da du nun shutil richtig gut im Griff hast, muss du gar nicht mehr auf die Markdowndatei zugreiffen und kannst die zweite Aufgabe auch so lösen) Wende shutil.copytree() an um alle Markdown Dateien (md) zu ignorieren. Die Funktion sollte dir eine Liste der Namen der Datein und Verzeichnisse zurückgeben, die du ignorieren kannst. Denke daran, dass du eine Kopie des Verzeichnisses machst und deine Markdown Dateien im Original Verzeichnis noch ungeändert vorhanden sind.
### Gib an wieviele Markdown Dokumente auf deinem persönlichen kopierten Repository vorhanden sind.

import shutil
import os
import subprocess

# 1. Klonen des Repositories
def clone_repository(repo_url, destination):
    subprocess.run(["git", "clone", repo_url, destination], check=True)
    print(f"Repository erfolgreich geklont: {destination}")

# 2. Erstellen eines ZIP-Archivs
def create_zip_archive(source_folder, archive_name):
    shutil.make_archive(archive_name, 'zip', source_folder)
    print(f"ZIP-Archiv erstellt: {archive_name}.zip")

# Kopieren des Repositories ohne Markdown-Dateien
def copy_repository_without_markdown(source_folder, destination_folder):
    ignored_files = []
    
    def ignore_markdown(folder, files):
        nonlocal ignored_files
        md_files = [file for file in files if file.endswith(".md")]
        ignored_files.extend([os.path.join(folder, file) for file in md_files])
        return md_files

    shutil.copytree(source_folder, destination_folder, ignore=ignore_markdown)
    print(f"Verzeichnis erfolgreich kopiert nach: {destination_folder}")
    return ignored_files

# Zählen der Markdown-Dateien
def count_markdown_files(source_folder):
    md_count = sum(
        1 for root, _, files in os.walk(source_folder)
        for file in files if file.endswith(".md")
    )
    return md_count

# Beispiel: Nutzung der Funktionen
repo_url = "https://github.com/dein-benutzername/dein-repository.git"  # Ersetze dies durch dein Repository
destination = "./geklontes_repository"
archive_name = "meine_programming_basics"

# Aufgabe 1: Repository klonen und ZIP-Archiv erstellen
clone_repository(repo_url, destination)
create_zip_archive(destination, archive_name)

# Aufgabe 2: Kopieren des Repository ohne Markdown-Dateien und Ausgabe der ignorierten Dateien
destination_copy = "./kopiertes_repository_ohne_markdown"
ignored_files = copy_repository_without_markdown(destination, destination_copy)
print(f"Ignorierte Markdown-Dateien: {ignored_files}")

# Anzahl der Markdown-Dateien im Original-Repository zählen
md_count = count_markdown_files(destination)
print(f"Anzahl der Markdown-Dateien im Original-Repository: {md_count}")
