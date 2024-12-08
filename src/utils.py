# the utils module.
import json
from json import JSONDecodeError


def load_operations_json(filename: str) -> list[dict[str, any]]:
    """Loading list of financial transactions. filename - path to json file.
    Returns list of dict with financial transaction data."""

    transaction_data = []

    with open(filename, "r") as f:
        try:
            transaction_data = json.load(f)
        except JSONDecodeError:
            pass
        except TypeError:
            pass
        except ValueError:
            pass

    return transaction_data


def get_transaction_amount(transaction_data: dict[str, any]) -> float:
    """accepts a transaction as input and returns the transaction amount
    in rubles, data type — float. If the transaction was in USD or EUR, an external API is
    accessed to obtain the current exchange rate and convert the transaction amount into
    rubles. To convert currency, use the convert_currency function in
    the external_api module."""

    amount = transaction_data["operationAmount"]["amount"]
    currency = transaction_data["operationAmount"]["currency"]["code"]

    amount_float = 0.0
    if currency != "RUB":
        amount = convert_currency(amount, code)
    else:
        amount = float(amount)

    return amount_float