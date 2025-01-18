# Programming_Basics Package Vorstellung: Plotly

## Kurzbeschreibung (Abstract)
Plotly ist eine interaktive Visualisierungsbibliothek in Python,
die es ermöglicht, statische und dynamische Grafiken für die Datenanalyse und Präsentation zu erstellen. In Plotly wird eine Vielzahl von verschiedenen Diagrammen unterstützt, darunter Linien-, Balken-, Scatter- und Kartenplots. Plotly ist besonders nützlich für die Visualisierung grosser Datensätze, da es detaillierte und interaktive Diagramme ohne viel Codeaufwand erzeugt.

## Praktische Relevanz
Plotly ist ein vielseitiges Tool für die visuelle Datenanalyse und -präsentation, 
das besonders in Bereichen mit grossen oder komplexen Datensätzen wertvoll ist. 
Es bietet interaktive Funktionen wie Zoomen, Hervorheben von Datenpunkten und das Ein-
und Ausblenden von Datenreihen, dadurch können wir tiefere Einblicke in die Daten gewinnen,
ohne den Code selbst anpassen zu müssen. Diese Interaktivität ist vor allem in Explorationsphasen
von Vorteil, in denen Hypothesen überprüft oder beispielsweise Ausreisser in den Daten identifiziert 
werden sollen.


Der Hauptunterschied zwischen Plotly und Matplotlib, mit dem ebenfalls verschiedene Datenvisualisierungen gemacht 
werden können liegt in der Interaktivität dieser Visualisierungen. Plotly bietet eine dynamische Schnittstelle, 
die in vielen Umgebungen genutzt werden kann. 
Besonders für das Reporting und die Präsentation von Analyseergebnissen an ein breiteres Publikum 
eignet sich Plotly gut, da interaktive Visualisierungen oft intuitiver zu verstehen sind und das Benutzerengagement erhöhen.

Mit diesen Eigenschaften bietet Plotly nützliche Funktionen in diversen Bereichen der Wissenschaft, 
Finanzen und Ingenieurwesen, wo solche detaillierte und anpassbare Grafiken von grossem Nutzen sind. 


## Einführung

Plotly ist bekannt für seine einfache Handhabung und die Möglichkeit, interaktive Visualisierungen mit wenigen Zeilen Code zu erstellen. 

### Installation 
Um Plotly zu installieren, nutzen wir den gewohnten Befehl:
```py
pip install plotly
```

### Standard Diagramme mit plotly.express

In diesem Abschnitt werden die grundlegenden Diagrammtypen und Funktionen von plotly.express vorgestellt.

#### 1. Liniendiagramm (px.line)
Verwendet für zeitliche Trends und Entwicklungen.

```python
import plotly.express as px
df = px.data.gapminder()
fig = px.line(df, x="year", y="gdpPercap", color="continent", title="BIP pro Kopf über die Jahre")
fig.show()
```
Argumente:

- x, y: Spalten für die x- und y-Achse (erforderlich)
- color: Gruppierung nach Kategorien (z. B. continent)
- line_group: Gruppiert Linien nach einer anderen Spalte
- title: Titel des Diagramms

#### 2. Balkendiagramm (px.bar)
Verwendet für Vergleiche zwischen Kategorien.

```py
fig = px.bar(df, x="continent", y="pop", color="continent", title="Bevölkerung nach Kontinent")
fig.show()
```
Argumente:

- x, y: Spalten für die x- und y-Achse (erforderlich)
- color: Gruppierung nach Kategorien
- title: Titel des Diagramms

#### 3. Tortendiagramm (px.pie)
Verwendet für die prozentuale Darstellung von Kategorien.

```py
fig = px.pie(df[df['year'] == 2007], values='pop', names='continent', title="Bevölkerungsanteil 2007")
fig.show()
```

Argumente:

- values: Werte, die im Diagramm dargestellt werden (erforderlich)
- names: Kategoriennamen
- color_discrete_sequence: Farben für die Kategorien


#### 4. Scatterplot (px.scatter)
Verwendet für die Beziehung zwischen zwei Variablen.

```py
fig = px.scatter(df, x="gdpPercap", y="lifeExp", color="continent", hover_name="country",
                 title="Lebenserwartung vs. BIP pro Kopf")
fig.show()
```

Argumente:

- x, y: Spalten für die x- und y-Achse (erforderlich)
- color: Gruppierung nach Kategorien
- hover_name: Spalte für zusätzliche Informationen beim Hover
- size: Grösse der Punkte basierend auf einer numerischen Spalte

#### 5. Histogramm (px.histogram)
Verwendet zur Darstellung der Verteilung einer Variable.

```py
fig = px.histogram(df, x="lifeExp", nbins=20, title="Verteilung der Lebenserwartung")
fig.show()
```

Argumente:

- x: Spalte für die x-Achse (erforderlich)
- nbins: Anzahl der Bins (Intervalle) im Histogramm
- color: Gruppierung nach Kategorien


**Wichtig!**
Plotly-Diagramme werden standardmässig im Browser dargestellt, weil Plotly interaktive HTML- und JavaScript-basierte Visualisierungen erzeugt. Dies ermöglicht die Nutzung von Funktionen wie Zoomen, Hovern, Klicken und andere interaktive Elemente, die direkt im Browser optimal unterstützt werden.

### Interaktives Dashboard mit Dash und plotly

Ein interaktives Dashboard ist eine visuelle Oberfläche, die es ermöglicht, Daten dynamisch zu filtern und verschiedene Ansichten anzuzeigen. Dash ist ein Framework von Plotly, das sich besonders gut eignet, um solche interaktiven Dashboards zu erstellen und in Python zu verwenden. 

Weil das Erstellen, bzw. auch das Vorstellen dieser interkativen Dashboards den Rahmen dieser kleinen Arbeit sprengen würde, ich es persönlich aber trotzdem unheimlich interessant finde, wird hier ein Code-Beispiel, das von ChatGPT erstellt wurde vorgestellt. Anhand von diesem Beispiel bekommen wir einen guten Eindruck, was mit Dash und Plotly möglich wäre, wenn man die nötige Zeit und Effort dafür aufwendet. 

Es kann entweder der Code unten kopiert werden oder die Datei 'plotly_dashboard.py' ausgeführt werden, um das Beispiel anzusehen. Sofern alles klappt, wir die Anwendung über den lokalen Server ausgeführt und kann in einem Webbrowser angezeigt werden, meist unter http://127.0.0.1:8050.

Dieses interaktive Dashboard wurde mithilfe von Dash und Plotly entwickelt und bietet eine übersichtliche Visualisierung der Entwicklung des Bruttoinlandsprodukts (BIP) pro Kopf für verschiedene Länder über die Zeit.


```py
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Beispiel-Datensatz laden
df = px.data.gapminder()

# Erstellen der Dash-Anwendung
app = dash.Dash(__name__)

# Layout der Anwendung
app.layout = html.Div([
    html.H1("Interaktives Dashboard: BIP pro Kopf nach Land"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df['country'].unique()],
        value='Germany',  # Standardmässig ausgewähltes Land
        style={'width': '50%'}
    ),
    dcc.Graph(id='line-graph')
])

# Callback zur Aktualisierung des Diagramms basierend auf der Auswahl im Dropdown
@app.callback(
    Output('line-graph', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_graph(selected_country):
    filtered_df = df[df['country'] == selected_country]
    fig = px.line(filtered_df, x='year', y='gdpPercap', 
                  title=f'BIP pro Kopf in {selected_country} über die Jahre',
                  labels={'gdpPercap': 'BIP pro Kopf', 'year': 'Jahr'})
    fig.update_layout(transition_duration=500)
    return fig

# Starten der Dash-Anwendung
if __name__ == '__main__':
    app.run_server(debug=True)
```

Wie erwähnt wird aus Zeit und Platz gründen nicht weiter auf dieses Beispiel eingegangen. Ich fand es bei der Recherche aber zu cool, um es ganz weg zu lassen ;)

## Übungsaufgaben

### Aufgabe 1: Tortendiagramm erstellen

Erstelle ein Tortendiagramm zur Darstellung der Marktanteile verschiedener Smartphone-Marken.
Die Smartphone-Marken haben die folgenden (fiktiven) Marktanteile:
- Apple - 49%
- Samsung - 26%
- Huawei 13%
- Sony 5%
- Nokia 4%
- Andere 3%

Die Lösungen können weiter unten angesehen werden.


### Aufgabe 2: Liniendiagramm erstellen

Ein Museum hat die Besucherzahlen für jeden Monat eines Jahres erfasst. Die Daten sind wie folgt:

Monate: Januar bis Dezember
Besucherzahlen: [450, 500, 600, 700, 750, 800, 850, 820, 780, 730, 620, 550]

Erstelle ein interaktives Liniendiagramm mit Plotly, das die Besucherentwicklung im Jahresverlauf darstellt. Füge passende Achsentitel und einen Diagrammtitel hinzu.

Die Lösungen können weiter unten angesehen werden.


Die Aufgaben mit den Lösungen sind ebenfalls als Python File (package_plotly_uebungsaufgaben.py) abgelegt und können dort nachgeschaut werden.