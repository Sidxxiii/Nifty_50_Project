import yfinance as yf

nifty = yf.download("^NSEI", start="2026-04-01", end="2026-09-12")

nifty.to_csv("data/nifty_raw.csv")

print(nifty.head())
