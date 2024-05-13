#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#мы берем все токены, которые залистились в последнее время, не только щиткоины, которые рагаются через несколько часов, и берем выборку из 1.000 штук и  будем проверять гипотезы по типу стоило ли их покупать как только они вышли, т.е. при листинге и будет ли выгодно их покупать относительно их сегодняшней цены и вторую гипотезу будет ли профитно их покупать относительно их ath (all time high)
#здесь представлен код, с помошью которого мы будем выводить список тысячи последних токенов, которые листнулись на CoinMarketCap

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/new'
parameters = {
  'start':'1',
  'limit':'1000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'наша апишка',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  df = pd.DataFrame(data['data'])  # Предполагая, что данные находятся в ключе 'data'
  print(df)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
#сейчас разбираемся как получить информацию о начальной и максимальной цене
#то есть наши дальнейшие действия: через уже полученное api в таблицу выводим 1.000 последних токенов, разбираемся как получить лаунч цену и актуальную для проверки гипотезы №1, далее разбираемся над тем, как получить ath цену, дабы проверить гипотезу №2.

