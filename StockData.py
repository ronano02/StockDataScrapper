import requests
import time
from bs4 import BeautifulSoup

class Stonk:
    def __init__(self, ticker, link, buyin, currency):
        self.ticker = ticker
        self.link = link
        self.buyin = buyin
        self.currency = currency

tesla = Stonk('TSLA', 'https://au.finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch', None, 'USD')
nvidia = Stonk('NVDA', 'https://au.finance.yahoo.com/quote/NVDA?p=NVDA&.tsrc=fin-srch', None, 'USD')
ark = Stonk('ARKK', 'https://au.finance.yahoo.com/quote/ARKK?p=ARKK&.tsrc=fin-srch', None, 'USD')
bitcoin = Stonk('BTC', 'https://au.finance.yahoo.com/quote/BTC-AUD?p=BTC-AUD&.tsrc=fin-srch', None, 'AUD')
ethereum = Stonk('ETH', 'https://au.finance.yahoo.com/quote/ETH-AUD?p=ETH-AUD&.tsrc=fin-srch', None, 'AUD')
ripple = Stonk('XRP', 'https://au.finance.yahoo.com/quote/XRP-AUD?p=XRP-AUD&.tsrc=fin-srch', None, 'AUD')
vechain = Stonk('VET', 'https://au.finance.yahoo.com/quote/VET-AUD?p=VET-AUD&.tsrc=fin-srch', None, 'AUD')
doge = Stonk('DOGE', 'https://au.finance.yahoo.com/quote/DOGE-AUD?p=DOGE-AUD&.tsrc=fin-srch', None, 'AUD')

stocks = [tesla, nvidia, ark]
crypto = [bitcoin, ethereum, ripple, vechain, doge]

def stonkData(list):
    for stock in list:
        link = requests.get(stock.link)
        soup = BeautifulSoup(link.text, 'lxml')
        price = soup.find(class_='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)').text
        try:
            change = soup.find(class_='Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)').text
        except:
            change = soup.find(class_= 'Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)').text
        print(stock.ticker)
        print(str(price) + f' ({stock.currency})')
        print(change)
        if stock.buyin != None:
            print('Bought in at:' + str(stock.buyin))
        print()

exit = 0

while exit == 0:
    print('-' * 100)
    print('\nS T O N K S\n')
    stonkData(stocks)
    print('\nC R Y P T O\n')
    stonkData(crypto)
    print('-' * 100)
    time.sleep(60)
