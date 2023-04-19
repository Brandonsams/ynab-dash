import dash_bootstrap_components as dbc
from dash import html

# import components
from components.dropdown import render_dropdown
from components.navbar import navbar


def render_dashboard():
    return html.Div([
        navbar,
        html.Div(
                    [
                        html.Br(),
                        dbc.Container(
                            fluid=True,
                            children=[
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            width=2,
                                            children=dbc.Card(
                                                [
                                                    dbc.CardHeader("Stocks"),
                                                    dbc.CardBody(
                                                        [
                                                            render_dropdown(
                                                                dropdown_id="dropdown-choose-stock", items=['TSLA', 'AAPL', 'SQ', 'PLTR'])
                                                        ]
                                                    )
                                                ],
                                                style={'height': "84vh"},
                                            )
                                        ),
                                        dbc.Col(
                                            width=10,
                                            children=dbc.Card(
                                                [
                                                    dbc.CardHeader(
                                                        "Visualisation"),
                                                    dbc.CardBody(
                                                        [
                                                            render_dropdown(
                                                                dropdown_id='dropdown-vis', items=['Line Plot']),
                                                            html.Div(
                                                                id='div-vis')
                                                        ]
                                                    )
                                                ],
                                                style={'height': '84vh'}
                                            )
                                        )
                                    ]
                                )
                            ]
                        ),
                    ]
                    )
    ])
