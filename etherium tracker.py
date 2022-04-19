from twilio.rest import Client
import ccxt
from forex_python.converter import CurrencyRates

client = Client("ACf3d95ca6b9794ca37f523d8229310e9f", "4b21e17d2644105d42fd366012b1d43b")

binance = ccxt.binance()
btc_ticker = binance.fetch_ticker('ETH/USDT')

c = CurrencyRates()
exchange_rate = c.get_rate('USD', 'GBP')

price = btc_ticker['bid']

print(f'price per coin is ${price}')
print(f'dollar to pound exchange rate is {exchange_rate}')
print(f'price in pounds is {price * exchange_rate}')