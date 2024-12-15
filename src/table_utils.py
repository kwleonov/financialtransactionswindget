# the table_utils module for reading tabular data from csv and excel files.

import csv
import pandas as pd

from src.utils import TransactionData
from tests.conftest import transactions


def read_csv(filename: str) -> list[TransactionData]:
    """read_csv(filename) - filename is path to csv file, return list of transaction data from csv file.
    csv file must have fields:
    id: int, state: str, date: str, amount: float, currency_name: str, currency_code: str, from: str, to: str and
    description: str."""

    transaction_data: list[TransactionData] = list()

    try:
        with open(filename) as csv_file:
            csv_data = csv.DictReader(csv_file)
            for row in csv_data:
                id = row["id"]
                state = row["state"]
                date = row["date"]
                amount = row["amount"]
                currency_name = row["currency_name"]
                currency_code = row["currency_code"]
                from_val = row["from"]
                to_val = row["to"]
                description = row["description"]
                transaction = {
                    "id": id,
                    "state": state,
                    "date": date,
                    "operationAmount": {
                        "amount": amount,
                        "currency": {
                            "name": currency_name,
                            "code": currency_code,
                        }
                    },
                    "description": description,
                    "from": from_val,
                    "to": to_val,
                }
                transaction_data.append(transaction)
    except FileNotFoundError as e:
        pass
    except KeyError as e:
        pass
    except csv.Error as e:
        pass

    return transaction_data


def read_excel(filename: str) -> list[TransactionData]:
    """read_excel(filename) - filename is path to excel file, return list of transaction data from excel file.
    excel file must have fields:
    id: int, state: str, date: str, amount: float, currency_name: str, currency_code: str, from: str, to: str and
    description: str."""

    transaction_data: list[TransactionData] = list()

    try:
        pass
    except FileNotFoundError as e:
        pass
    except KeyError as e:
        pass
    except pd. as e:
        pass

    return transaction_data
