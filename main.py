import yfinance as yf
from flask import Flask, render_template, request, jsonify
import pandas as pd
# from flask_compress import Compress

# class stocks:
#     def __init__(self, symbol, name):
#         self.name = name
#         self.symbol = symbol
#
#         self.ticker = yf.Ticker(symbol)
#
#     def get_price(self):
#         return self.ticker.info
#
#     def get_dividends(self):
#         return self.ticker.dividends
#
#     def get_history(self, period):
#         return self.ticker.history(period=period)
#
#     def get_financials(self):
#         return self.ticker.financials


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml', 'application/json', 'application/javascript']
# COMPRESS_LEVEL = 6
# COMPRESS_MIN_SIZE = 500
# Compress(app)


@app.route('/', methods=['POST', 'GET'])
def stockMain():
    return render_template("stocks.html")
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