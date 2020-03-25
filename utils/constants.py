from utils.yaml_helpers import get_secrets

API_KEY = get_secrets().get("api_key")
API_SECRET = get_secrets().get("api_secret")
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"
