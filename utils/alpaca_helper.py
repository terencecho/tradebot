import alpaca_trade_api as tradeapi

from utils.constants import API_KEY, API_SECRET, APCA_API_BASE_URL


class AlpacaHelper:
    def __init__(self):
        self.alpaca = tradeapi.REST(API_KEY, API_SECRET, APCA_API_BASE_URL, 'v2')

    def get_alpaca(self):
        return self.alpaca

    # cancel any existing orders so they don't impact our buying power
    def clear_pending_trades(self):
        orders = self.alpaca.list_orders(status="open")
        for order in orders:
            self.alpaca.cancel_order(order.id)
