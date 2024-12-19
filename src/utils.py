# the utils module.

import datetime
import json
import logging
from collections import Counter
from json import JSONDecodeError
from os import makedirs
from typing import TypedDict

from src.external_api import convert_amount
from src.processing import filter_by_description

Currency = TypedDict("Currency", {"name": str, "code": str})
OperationAmount = TypedDict("OperationAmount", {"amount": str, "currency": Currency})
TransactionData = TypedDict("TransactionData", {
    "id": int,
    "state": str,
    "date": str,
    "operationAmount": OperationAmount,
    "description": str,
    "from": str,
    "to": str,
})

log_file = "logs/utils.log"
log_ok_str = "was executed without errors"
makedirs("logs", exist_ok=True)
logger = logging.getLogger(__name__)
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler = logging.FileHandler(log_file, mode="w")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_operations_json(filename: str) -> list[TransactionData]:
    """Loading list of financial transactions. filename - path to json file.
    Returns list of dict with financial transaction data."""

    transaction_data = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            transaction_data = json.load(f)
            if type(transaction_data) is not list:
                logger.error("the load_operations_json - didn't get a list of transactions")
                return []
            logger.debug(f"the load_operations_json {log_ok_str}")

    except JSONDecodeError as e:
        logger.error(f"the load_operations_json - JSON decode error: {e}")
    except FileNotFoundError as e:
        logger.error(f"the load_operations_json - JSON file not found: {e}")

    return transaction_data


def get_transaction_amount(transaction_data: TransactionData) -> float:
    """accepts a transaction as input and returns the transaction amount
    in rubles, data type — float. If the transaction was in USD or EUR, an external API is
    accessed to obtain the current exchange rate and convert the transaction amount into
    rubles. To convert currency, use the convert_currency function in
    the external_api module."""

    amount_float = 0.0

    try:
        amount = transaction_data["operationAmount"]["amount"]
        amount_float = float(amount)
        currency = transaction_data["operationAmount"]["currency"]["code"]

        if currency != "RUB":
            date_str = transaction_data["date"]
            date_time = datetime.datetime.fromisoformat(date_str)
            date = date_time.strftime("%Y-%m-%d")
            amount_float = convert_amount(amount_float, currency, date)

        logger.debug(f"the get_transaction_amount {log_ok_str}")

    except KeyError as e:
        logger.error(f"the get_transaction_amount - KeyError: {e}")

    return amount_float


def counter_category(transactions_data: list[TransactionData], categories: list[str]) -> dict[str, int]:
    """gets list of transactions and list of categories, return dict where keys are categories and values are
    number of operations for each category."""

    categories_count: Counter[str] = Counter()

    for category in categories:
        transactions = filter_by_description(transactions_data, category)
        for i in range(len(transactions)):
            categories_count.update([category])

    return dict(categories_count)
