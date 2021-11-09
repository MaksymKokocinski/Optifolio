import platform
print('Python version = ' + platform.python_version())
import yfinance as yf
print('yfinance version = ' + yf.__version__)
import datetime



def yfinancetest(tickersymbol):
    tickerdata = yf.Ticker(tickersymbol)
    tickerinfo = tickerdata.info
    investment = tickerinfo['shortName']

    today = datetime.datetime.today().isoformat()
    print('today =',today)
    
    tickerDF = tickerdata.history(period = '1d', start='2020-1-1', end=today[:10])
    pricelast = tickerDF['Close'].iloc[-1]
    #return(investment)
    print(investment + 'price last =' + str(pricelast))
    print(tickerDF)


yfinancetest('TSLA') #tesla
print('')
yfinancetest('CDRN.MX')