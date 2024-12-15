# the table_utils module for reading tabular data from csv and excel files.

import csv
import logging
from os import makedirs

import pandas as pd

from src.utils import TransactionData

log_file = "logs/table_utils.log"
log_ok_str = "was executed without errors"
makedirs("logs", exist_ok=True)
logger = logging.getLogger(__name__)
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler = logging.FileHandler(log_file, mode="w")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_csv(filename: str) -> list[TransactionData]:
    """read_csv(filename) - filename is path to csv file, return list of transaction data from csv file.
    csv file must have fields:
    id: int, state: str, date: str, amount: float, currency_name: str, currency_code: str, from: str, to: str and
    description: str."""

    transaction_data: list[TransactionData] = list()

    try:
        with open(filename, encoding="utf-8") as csv_file:
            csv_data = csv.DictReader(csv_file, delimiter=";")
            for row in csv_data:
                id = int(row["id"])
                state = row["state"]
                date = row["date"]
                amount = str(row["amount"])
                currency_name = row["currency_name"]
                currency_code = row["currency_code"]
                from_val = row["from"]
                to_val = row["to"]
                description = row["description"]
                transaction: TransactionData = {
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
            logger.debug("the read_csv function was executed without errors.")
    except FileNotFoundError as e:
        logger.error(f"CSV file {filename} not found: {e}")
    except KeyError as e:
        logger.error(f"field name in csv data {filename} not exists: {e}")
    except csv.Error as e:
        logger.error(f"error parse {filename} csv data: {e}")

    return transaction_data


def read_excel(filename: str) -> list[TransactionData]:
    """read_excel(filename) - filename is path to excel file, return list of transaction data from excel file.
    excel file must have fields:
    id: float, state: str, date: str, amount: float, currency_name: str, currency_code: str, from: str, to: str and
    description: str."""

    transaction_data: list[TransactionData] = list()

    try:
        with open(filename, "rb") as excel_file:
            excel_data = pd.read_excel(excel_file)
            excel_dict = excel_data.to_dict("records")
            for row in excel_dict:
                id = int(row["id"])
                state = row["state"]
                date = row["date"]
                amount = str(row["amount"])
                currency_name = row["currency_name"]
                currency_code = row["currency_code"]
                from_val = row["from"]
                to_val = row["to"]
                description = row["description"]
                transaction: TransactionData = {
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
            logger.debug("the read_excel function was executed without errors.")
    except FileNotFoundError as e:
        logger.error(f"Excel file {filename} not found: {e}")
    except KeyError as e:
        logger.error(f"field name in Excel data {filename} not exists: {e}")
    except pd.errors.ParserError as e:
        logger.error(f"error parse {filename} excel data: {e}")

    return transaction_data
