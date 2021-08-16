import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
msft.info

# get historical market data
hist = msft.history(period="max")

#print(hist)


doge = yf.Ticker("DOGE-USD")
doge_hist = doge.history(period="max")



print(doge_hist) 
