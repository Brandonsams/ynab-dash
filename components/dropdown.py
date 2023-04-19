from dash import dcc


def render_dropdown(dropdown_id: str, items=[''], clearable_option=False):
	dropdown = dcc.Dropdown(
		id=dropdown_id,
		clearable=clearable_option,
		options=[{'label': i, 'value': i} for i in items],
		value=items[0],
	)
	return dropdown