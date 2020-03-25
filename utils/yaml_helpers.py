import yaml

API_KEYS_YAML_FILE = '../configs/api_keys.yaml'
STOCKS_YAML_FILE = '../configs/stocks.yaml'


def get_secrets():
    with open(API_KEYS_YAML_FILE) as file:
        api_secrets = yaml.load(file, Loader=yaml.FullLoader)
        return api_secrets


def get_ticker_symbols_from_yaml(key):
    with open(STOCKS_YAML_FILE) as file:
        stocks = yaml.load(file, Loader=yaml.FullLoader)
        return stocks.get(key)
