import datetime
import time

from utils.alpaca_helpers import get_alpaca


def await_market_open():
    alpaca = get_alpaca()
    is_open = alpaca.get_clock().is_open
    while not is_open:
        clock = alpaca.get_clock()
        opening_time = clock.next_open.replace(tzinfo=datetime.timezone.utc).timestamp()
        curr_time = clock.timestamp.replace(tzinfo=datetime.timezone.utc).timestamp()
        time_to_open = int((opening_time - curr_time) / 60)
        print(str(time_to_open) + " minutes til market open.")
        time.sleep(60)
        is_open = alpaca.get_clock().is_open
