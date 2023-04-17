# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dotenv import load_dotenv
import os
import requests
import json

# Get secrets
load_dotenv()
budget_uuid = os.environ.get('budget_uuid')
secret_token = os.environ.get('secret_token')

# Incorporate data
url = f'https://api.ynab.com/v1/budgets/{budget_uuid}/transactions?since_date=2023-01-01'
headers = {'Authorization': f'Bearer {secret_token}'}
# Get the data
resp_text = requests.get(url, headers=headers).text
resp_json = json.loads(resp_text)
transactions_json = resp_json['data']['transactions']
transactions = json.dumps(transactions_json)
df = pd.read_json(transactions)
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# Initialize the app - incorporate a Dash Bootstrap theme
external_stylesheets = [dbc.themes.FLATLY]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = dbc.Container([
	dbc.Row([
		html.Div('My First App with Data, Graph, and Controls', className="text-primary text-center fs-3")
	]),

	dbc.Row([
		dbc.RadioItems(options=[{"label": x, "value": x} for x in ['pop', 'lifeExp', 'gdpPercap']],
					   value='lifeExp',
					   inline=True,
					   id='radio-buttons-final')
	]),

	dbc.Row([
		dbc.Col([
			dash_table.DataTable(data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
		], width=6),

		dbc.Col([
			dcc.Graph(figure={}, id='my-first-graph-final')
		], width=6),
	]),

], fluid=True)

# Add controls to build the interaction
@callback(
	Output(component_id='my-first-graph-final', component_property='figure'),
	Input(component_id='radio-buttons-final', component_property='value')
)
def update_graph(col_chosen):
	fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
	return fig

# Run the app
if __name__ == '__main__':
	app.run_server(debug=True)
