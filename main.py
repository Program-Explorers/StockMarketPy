import yfinance as yf
from flask import Flask, render_template, request, jsonify
import urllib.request
import json
import datanews
from pandas_datareader import data
from fuzzywuzzy import process

import matplotlib.pyplot as plt
import pandas as pd
# from flask_compress import Compress


def get_company(company):
    with open('data_stocks') as json_file:
        list_of_stocks = json.load(json_file)
        return process.extractOne(company, list_of_stocks)[0]


tickers = ['AAPL', 'MSFT', '^GSPC']
start_date = '2020-01-01'
end_date = '2020-12-31'
panel_data = data.DataReader('INPX', 'yahoo', start_date, end_date)

# yf.Ticker("MSFT").info['shortName']
# panel_data.to_frame()


class stocks:
    def __init__(self, symbol, name, price):
        self.name = name
        self.symbol = symbol
        self.price = price

        self.Ticker = yf.Ticker(symbol)

    def get_price(self):
        return self.price

    def get_dividends(self):
        return self.Ticker.dividends

    def get_history(self, period):
        return self.Ticker.history(period=period)

    def get_financials(self):
        return self.Ticker.financials

    def get_quaterly_financials(self):
        return self.Ticker.quarterly_financials

    def get_actions(self):
        return self.Ticker.actions

    def get_splits(self):
        return self.Ticker.splits

    def get_major_holders(self):
        return self.Ticker.major_holders


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml', 'application/json', 'application/javascript']
# COMPRESS_LEVEL = 6
# COMPRESS_MIN_SIZE = 500
# Compress(app)


@app.route('/', methods=['POST', 'GET'])
def stockMain():
    # get text from search bar
    if request.method == 'POST':
        searched = request.form['stock']
        company1 = get_company(searched).title()
        symbol1 = get_company(company1).upper()

    else:
        company1 = "Microsoft"
        symbol1 = 'MSFT'

    stock1_api_info = json.loads(urllib.request.urlopen("".join(['https://www.alphavantage.co/query?function=GLOBAL_'
                                                                 'QUOTE&symbol=', symbol1, '&apikey=demo'])).read())

    stock1 = stocks(symbol1, company1, round(int(stock1_api_info['Global Quote']['05. price']), 2))

    return render_template("stocks.html", stock1=stock1)


@app.route('/news')
def news():
    datanews.api_key = '04loc6feus33veq8swg615d7w'
    response = datanews.headlines(q="stocks, stock market, bitcoin, etf, NYSE, NASDAQ, Dow Jones, "
                                  ,
                                  language=['en'], sortBy="relevance")
    articles = response['hits']
    print(response)
    article_data = {}
    for i in range(1, 11):
        x = str(i)
        article_data['article'+x+'_title'] = articles[i-1]['title']
        article_data['article' + x + '_content'] = articles[i - 1]['content']
        article_data['article' + x + '_img'] = articles[i - 1]['imageUrl']
        article_data['article' + x + '_url'] = articles[i - 1]['url']

    return render_template("news.html", article_data=article_data)
# get stock info
# print(msft.info)
#
# # get historical market data
# hist = msft.history(period="max")
#
# # show actions (dividends, splits)
# print(msft.actions)
#
# # show dividends
# print(msft.dividends)
#
# # show splits
# print(msft.splits)
#
# # show financials
# print(msft.financials)
# print(msft.quarterly_financials)
#
# # show major holders
# print(msft.major_holders)
#
# # show institutional holders
# print(msft.institutional_holders)
#
# # show balance sheet
# print(msft.balance_sheet)
# print(msft.quarterly_balance_sheet)
#
# # show cashflow
# print(msft.cashflow)
# print(msft.quarterly_cashflow)
#
# # show earnings
# print(msft.earnings)
# print(msft.quarterly_earnings)
#
# # show sustainability
# print(msft.sustainability)
#
# # show analysts recommendations
# print(msft.recommendations)
#
# # show next event (earnings, etc)
# print(msft.calendar)
#
# # show ISIN code - *experimental*
# # ISIN = International Securities Identification Number
# print(msft.isin)
#
# # show options expirations
# print(msft.options)
#
# # get option chain for specific expiration
# # opt = msft.option_chain('2020-12-24')
# # print(opt)

# LINK: https://aroussi.com/post/python-yahoo-finance


if __name__ == '__main__':
    app.run(debug=True)
