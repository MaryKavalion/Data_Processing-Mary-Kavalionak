from dash import Dash, html, dcc, callback, Output, Input
import plotly_express as px
import pandas as pd

df = px.data.gapminder()

app = Dash(__name__)

my_H1 = html.H1(children = "My dash app.", style = ({"font-family": "wingdings"}))
my_H2 = html.H2(id = "my-H2", children = "More info...")
my_dropdown = dcc.Dropdown(id = "my-dropdown", options = df["year"].unique(), value = 2007, style = {"width": "300px"})
my_graph = dcc.Graph(id = "my-graph", figure = {})
my_button = html.Button("Click here!")

app.layout = html.Div(children = [my_H1, my_H2, my_dropdown, my_graph, my_button])

@callback(
        Output(my_H2, component_property = "children"),
        Output(my_graph, component_property = "figure"),
        Input(my_dropdown, component_property="value")
)
def select_year(year):
    text = f"Life expectancy for {year}"
    return text, px.strip(df.query("year == @year"), x = "lifeExp", color = "continent" )

@callback(
    Output(my_H1, "children"),
    Input(my_button, "n_clicks")
)
def button_clicked(n):
    return f"Button clicked {n} times."

app.run(debug=True)

# <div>
#   <h1> My dash app </h1>
#   <h2> More info... </h2>
        # <div>
#        ...
        # </div>
# </div>