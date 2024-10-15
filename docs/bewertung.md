# Programming Basics

HS 2024

---

## Bewertung

Für das Seminar gibt es Testatübungen. Es wird empfohlen, die Übungen zeitnah zur Lektüre des Buches/des Lernpfades zu machen. Die Übungen werden automatisiert geprüft. Die gleichen Tests könnt ihr beim Lösen der Übungen lokal im "Testing"-Mode in VS-Code ausführen (Tipp: Fehlermeldungen genau ansehen - sie bieten oft Hilfe beim Lösen der Aufgaben!).

### Arbeitsaufträge (70%)

Die Bewertung der Arbeitsaufträge setzt sich aus den folgenden Punkten zusammen:

#### Dokumentation (35%)

Zu jedem im Unterricht besprochenen Thema ist unter `ssr2024/wiki` ein Markdown-Dokument vorbereitet. Zu jeder Überschrift sollen eigene Erklärungen, Beschreibungen, Beispiele und Notizen angefertigt werden.

Die Dokumentationen jedes Termins fliessen gleichmässig nach folgenden Kriterien in die Bewertung ein:

- Vollständigkeit
- Nachvollziehbarkeit
- Korrektheit
- treffende Beispiele
- Markdown Syntax richtig eingesetzt (Verwendung von Codeblöcken für Code, Links und Bilder richtig eingebunden, ...)

#### Commit-History (20%)

Die Commit-History zeigt auf wie an einem Projekt gearbeitet wird. Werden kleine, aber zusammengehörende Änderungen mit einem Commit und einer treffenden Nachricht zusammengefasst, lassen sich Änderungen gut nachvollziehen und ggf. einzelne Teile explizit rückgängig machen.

In die Bewertung fliessen ein:

- Wurden zusammengehörende Änderungen in einem Commit zusammengefasst?
- Commit-Messages
- Commit-Häufigkeit
- Commit-Konsistenz

<p style="page-break-after: always;"></p>

#### Dokumentation im Code (15%)

Die Code-Dokumentation hilft beim Lesen des Codes. Jede selbst geschriebene `Funktion` soll mit der gezeigten Konvention dokumentiert werden. Wo möglich sollen auch Type-Hints für die Funktionsparameter und den Rückgabewert hinzugefügt werden. Auch die einzelnen Module und Skripte sollen mit Kommentaren versehen werden und so nachvollziehbar werden.

```py
from typing import Union, List, Literal, Dict, Optional

def area(side_a: Union[int, float], side_b: Union[int, float]) -> Union[int, float]:
    """berechnet die Fläche eines Rechtecks

    Parameters
    ----------
    side_a : int, float
        eine Seite des Rechtecks
    side_b : int, float
        eine an 'side_a' anliegende Seite des Rechtecks

    Returns
    -------
    float, int
        Fläche des Rechtecks
    """
    return side_a * side_b
```

### Abschlussbericht (30%)

#### Teil 1: Selbständiges Erarbeiten und Dokumentieren eines Themengebietes

Die Dokumentation soll dabei folgende Teile aufweisen:

- Kurzbeschreibung der Thematik (maximal 5 Sätze, "Abstract")
- Aufzeigen der praktischen Relevanz (Wann ist die Funktionalität hilfreich? Bezug zur Datenauswertung herstellen.)
- Tutorial zur Thematik. Das Zielpublikum sind die Mitstudierenden aus dem Kurs "Programming Basics". Das Tutorial beschreibt die Syntax und die Funktionalität, inklusive erforderlicher und möglicher Argumente zum Aufrufen der Funktionen anhand von Code-Beispielen.
- Zwei selbst zusammengestellte Übungen zum Thema, die nach dem Studium des Tutorials gelöst werden können.

!Für den ersten Teil muss ein **Pull-Request** auf dem persönlichen (geforkten) `ssr2024` Repo geöffnet werden, der jegliche Commits des Abschlussberichts enthält.

#### Teil 2: Review und Lösen der Übungen von zwei anderen Abschlussberichten

Jede Person macht ein bis zwei Reviews der zugewiesenen Abschlussberichte (Tutorials) und bearbeitet in diesem Rahmen auch die jeweiligen Übungen. Beim Review sollen Verbesserungsvorschläge gemacht werden. Da die Berichte erst _nach_ dem Umsetzen der Vorschläge der Reviewer bewertet werden, _dürfen&sollen_ die Reviews konstruktiv und ruhig auch kritisch gemacht werden. Es ist bei Reviews auch okay, beispielsweise auf unübersichtliche Codeformatierungen hinzuweisen (Beispiwelsweise ist `a= 1+1` weniger übersichtlich als `a = 1 + 1` - das darf/soll auch angemerkt werden).

#### Beurteilungskriterien

##### Teil 1 (80%)

- Umfang (4000-7000 Zeichen)
- Nachvollziehbarkeit
- Vollständigkeit
- Korrektheit
- Treffende Beispiele
- Die gewählte Übung hilft der/dem LeserIn den Inhalt zu verarbeiten und besser zu verstehen

##### Teil 2 (20%)

- Gute Vorschläge zur Verbesserung des Tutorials gegeben
- Lösungsvorschlag zu den Übungen

#### Abgaben

**Teil 1**: 16.11.2024

**Teil 2**: (Reviewen): 30.11.2024

Definitive Abgabe **Teil 1** (Umsetzung der Reviews): 21.12.2024
