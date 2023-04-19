import yfinance as yf


def get_yf_data(stock: str):
	 df = yf.download(tickers=stock, period='1d', interval='1m')
	 return df


def yf_dataframe(stock: str):
	return get_yf_data(stock)