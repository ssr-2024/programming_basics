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
        value='Switzerland',  # Standardmässig ausgewähltes Land
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
