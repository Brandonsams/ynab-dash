from dash.dependencies import Input, Output
from app import app
from pages.dashboard.dashboard_model import yf_dataframe

# import components
from plots.line_plot import *


@app.callback(
	Output(component_id='div-vis', component_property='children'),
	Input(component_id='dropdown-choose-stock', component_property='value')
)
def update_vis(stock):
	df = yf_dataframe(stock=stock)
	fig = line_plot(df, stock)

	return fig