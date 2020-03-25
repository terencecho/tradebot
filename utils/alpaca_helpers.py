import alpaca_trade_api as tradeapi

from utils.constants import API_KEY, API_SECRET, APCA_API_BASE_URL


def get_alpaca():
    return tradeapi.REST(API_KEY, API_SECRET, APCA_API_BASE_URL, 'v2')
