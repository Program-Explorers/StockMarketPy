import yfinance as yf
from flask import Flask, render_template, request, jsonify
import urllib.request
import json
import datanews

# from flask_compress import Compress

msft = yf.Ticker("MSFT")

# print(msft.info)


class stocks:
    def __int__(self, symbol, name, price):
        self.name = name
        self.symbol = symbol
        self.price = price

    def get_price(self):
        return self.symbol.info

    def get_dividends(self):
        return self.symbol.dividends

    def get_history(self, period):
        return self.symbol.history(period=period)

    def get_financials(self):
        return self.symbol.financials


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml', 'application/json', 'application/javascript']
# COMPRESS_LEVEL = 6
# COMPRESS_MIN_SIZE = 500
# Compress(app)
symbol = ''
stocksArray = urllib.request.urlopen(
    'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + symbol +'&apikey=demo').read()
stock = json.loads(stocksArray)


@app.route('/', methods=['POST', 'GET'])
def stockMain():
    return render_template("stocks.html")


@app.route('/news')
def news():
    datanews.api_key = '04loc6feus33veq8swg615d7w'
    response = datanews.headlines(q="stocks, stock market, bitcoin, etf, NYSE, NASDAQ, Dow Jones, "
                                  ,
                                  language=['en'], sortBy="relevance")
    articles = response['hits']
    article_data = {
        'article1_title': articles[0]['title'],
        'article1_content': articles[0]['content'],
        'article1_img': articles[0]['imageUrl'],
        'article1_url': articles[0]['url'],
        'article2_title': articles[1]['title'],
        'article2_content': articles[1]['content'],
        'article2_img': articles[1]['imageUrl'],
        'article2_url': articles[1]['url'],
        'article3_title': articles[2]['title'],
        'article3_content': articles[2]['content'],
        'article3_img': articles[2]['imageUrl'],
        'article3_url': articles[2]['url'],
        'article4_title': articles[3]['title'],
        'article4_content': articles[3]['content'],
        'article4_img': articles[3]['imageUrl'],
        'article4_url': articles[3]['url'],
        'article5_title': articles[4]['title'],
        'article5_content': articles[4]['content'],
        'article5_img': articles[4]['imageUrl'],
        'article5_url': articles[4]['url'],
    }
    print(response['numResults'])
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


if __name__ == '__main__':
    app.run(debug=True)
