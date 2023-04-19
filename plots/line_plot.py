from dash import dcc
import plotly.express as px


def line_plot(df, stock:str):
	fig = px.line(df, x=df.index, y=df['Adj Close'])
	fig.update_layout(title=str(stock))

	return dcc.Graph(figure=fig)