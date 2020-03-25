import datetime
import time


class TimeHelper:
    def __init__(self, alpaca):
        self.alpaca = alpaca

    # waits for market to open
    def await_market_open(self):
        is_open = self.alpaca.get_clock().is_open
        while not is_open:
            clock = self.alpaca.get_clock()
            opening_time = clock.next_open.replace(tzinfo=datetime.timezone.utc).timestamp()
            curr_time = clock.timestamp.replace(tzinfo=datetime.timezone.utc).timestamp()
            time_to_open = int((opening_time - curr_time) / 60)
            print(str(time_to_open) + " minutes til market open.")
            time.sleep(60)
            is_open = self.alpaca.get_clock().is_open
