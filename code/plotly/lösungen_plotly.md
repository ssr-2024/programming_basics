**Lösung Aufgabe 1**
```py
import plotly.express as px


marken = ["Apple", "Samsung", "Huawei", "Sony", "Nokia", "Andere"]
marktanteile = [49, 26, 13, 5, 4,3]


fig = px.pie(names=marken, values=marktanteile, title="Marktanteile verschiedener Smartphone-Marken")
fig.show()
```


**Lösung Aufgabe 2**
```py
import plotly.express as px

monate = ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"]
besucherzahlen = [450, 500, 600, 700, 750, 800, 850, 820, 780, 730, 620, 550]

fig = px.line(x=monate, y=besucherzahlen, title="Monatliche Besucherzahlen des Museums")
fig.update_layout(xaxis_title="Monat", yaxis_title="Anzahl der Besucher")
fig.show()
```