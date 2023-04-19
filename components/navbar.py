import dash_bootstrap_components as dbc

# import own style (see /assets)
from assets.style import MAIN_COLORS

navbar = dbc.NavbarSimple(
	children=[
		dbc.NavItem(dbc.NavLink("Dashboard", href="/dashboard")),
	],
	brand="Stock Dashboard",
	brand_href="/",
	color=MAIN_COLORS["primary"],
	sticky='top',
	links_left=True,
	dark=True
)