""""
Aufgabe 1: Tortendiagramm erstellen

Erstelle ein Tortendiagramm zur Darstellung der Marktanteile verschiedener Smartphone-Marken.
Die Smartphone-Marken haben die folgenden (fiktiven) Marktanteile:
- Apple - 49%
- Samsung - 26%
- Huawei 13%
- Sony 5%
- Nokia 4%
- Andere 3%
"""
import plotly.express as px
smartphone_brands = ["Apple", "Samsung", "Huawei", "Sony", "Nokia", "Andere"]
market_shares = [49, 26, 13, 5, 4, 3]

fig = px.pie(values=market_shares,
              names=smartphone_brands,
              title="Market Share of Smartphone Brands")
fig.show()

#Lösung Aufgabe 1

import plotly.express as px




marken = ["Apple", "Samsung", "Huawei", "Sony", "Nokia", "Andere"]
marktanteile = [49, 26, 13, 5, 4,3]


fig = px.pie(names=marken, values=marktanteile, title="Marktanteile verschiedener Smartphone-Marken")
fig.show()


"""
Aufgabe 2: Liniendiagramm erstellen

Ein Museum hat die Besucherzahlen für jeden Monat eines Jahres erfasst. Die Daten sind wie folgt:

Monate: Januar bis Dezember
Besucherzahlen: [450, 500, 600, 700, 750, 800, 850, 820, 780, 730, 620, 550]

Erstelle ein interaktives Liniendiagramm mit Plotly, das die Besucherentwicklung im Jahresverlauf darstellt. Füge passende Achsentitel und einen Diagrammtitel hinzu.
"""
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
visitors = [450, 500, 600, 700, 750, 800, 850, 820, 780, 730, 620, 550]

fig = px.line(x=months,
                y=visitors,
                title="Monthly Visitors of the Museum")

fig.update_layout(xaxis_title="Month",
                    yaxis_title="Number of Visitors")
fig.show()

#Lösung Aufgabe 2

import plotly.express as px

monate = ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"]
besucherzahlen = [450, 500, 600, 700, 750, 800, 850, 820, 780, 730, 620, 550]

fig = px.line(x=monate,
                y=besucherzahlen,
                title="Monatliche Besucherzahlen des Museums")
fig.update_layout(xaxis_title="Monat",
                  yaxis_title="Anzahl der Besucher")
fig.show()
