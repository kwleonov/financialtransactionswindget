# the utils module.
import datetime
import json
from json import JSONDecodeError

from src.external_api import convert_amount


def load_operations_json(filename: str) -> list[dict[str, any]]:
    """Loading list of financial transactions. filename - path to json file.
    Returns list of dict with financial transaction data."""

    transaction_data = []

    try:
        with open(filename, "r") as f:
            transaction_data = json.load(f)
            if type(transaction_data) is not list:
                return []

    except JSONDecodeError as e:
        print(f"JSON decode error: {e}")
    except FileNotFoundError as e:
        print(f"JSON decode error: {e}")

    return transaction_data


def get_transaction_amount(transaction_data: dict[str, any]) -> float:
    """accepts a transaction as input and returns the transaction amount
    in rubles, data type — float. If the transaction was in USD or EUR, an external API is
    accessed to obtain the current exchange rate and convert the transaction amount into
    rubles. To convert currency, use the convert_currency function in
    the external_api module."""

    amount_float = 0.0

    try:
        amount = transaction_data.get("operationAmount").get("amount")
        amount_float = float(amount)
        currency = transaction_data["operationAmount"]["currency"]["code"]

        if currency != "RUB":
            date_str = transaction_data["date"]
            date_time = datetime.datetime.fromisoformat(date_str)
            date = date_time.strftime("%Y-%m-%d")
            amount_float = convert_amount(amount, currency, date)
    except KeyError as e:
        print(f"KeyError: {e}")

    return amount_float
