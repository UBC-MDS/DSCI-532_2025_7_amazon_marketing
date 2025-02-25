import altair as alt
import dash_bootstrap_components as dbc
import dash_vega_components as dvc
from dash import Dash
from vega_datasets import data


# Initiatlize the app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

cars = data.cars()
chart = alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    tooltip='Origin'
).interactive()

# Layout
app.layout = dbc.Container([
    # Note that you need to pass the chart as a dictionary via `to_dict()`
    dvc.Vega(spec=chart.to_dict()),
])

# Layout
app.layout = dbc.Container([
    dcc.Checklist(id='show_chart', options=[' Show chart']),
    dvc.Vega(id='scatter', spec={})
])

# Server side callbacks/reactivity
@callback(
    Output('scatter', 'spec'),
    Input('show_chart', 'value')
)
def create_chart(show_chart):
    if show_chart:
        return chart.to_dict()
    else:
        return {}
    
# Run the app/dashboard
if __name__ == '__main__':
    app.run(debug=True)
