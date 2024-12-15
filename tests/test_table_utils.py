# the test_table_utils module.

from unittest.mock import Mock, patch

import pandas as pd

from src.table_utils import read_csv, read_excel


@patch("csv.DictReader")
def test_read_csv(mock_csv: Mock) -> None:
    """testing the read_csv function for get transaction data."""

    csv_data = [{"id": 111, "state": "EXECUTED", "date": "2024-12-15",
                 "amount": 111, "currency_name": "Ruble", "currency_code": "RUB",
                 "description": "test", "from": "Master Card", "to": "Visa"}]
    data = [{"id": 111, "state": "EXECUTED", "date": "2024-12-15",
             "operationAmount": {"amount": "111", "currency": {"name": "Ruble", "code": "RUB"}},
             "description": "test", "from": "Master Card", "to": "Visa"}]
    mock_csv.return_value = csv_data
    assert read_csv("data/transactions.csv") == data


def test_not_exist_csv() -> None:
    """testing open not exist file for exception."""

    assert read_csv("data/notexist.csv") == []


@patch("csv.DictReader")
def test_invalid_csv(mock_csv: Mock) -> None:
    """testing get invalid csv data."""

    mock_csv.return_value = [{"ids": 111}]
    assert read_csv("data/transactions.csv") == []


@patch("pandas.read_excel")
def test_read_excel(mock_excel: Mock) -> None:
    """testing the read_excel function for get transaction data."""

    excel_data = pd.DataFrame({"id": [111.0], "state": ["EXECUTED"], "date": ["2024-12-15"],
                               "amount": [111.0], "currency_name": ["Ruble"], "currency_code": ["RUB"],
                               "description": ["test"], "from": ["Master Card"], "to": ["Visa"]})
    data = [{"id": 111, "state": "EXECUTED", "date": "2024-12-15",
             "operationAmount": {"amount": "111.0", "currency": {"name": "Ruble", "code": "RUB"}},
             "description": "test", "from": "Master Card", "to": "Visa"}]
    mock_excel.return_value = excel_data
    assert read_excel("data/transactions_excel.xlsx") == data


def test_not_exist_excel() -> None:
    """testing open not exist file for exception."""

    assert read_excel("data/notexist.xlsx") == []


@patch("pandas.read_excel")
def test_invalid_excel(mock_csv: Mock) -> None:
    """testing get invalid excel data."""

    mock_csv.return_value = pd.DataFrame({"ids": [111.0]})
    assert read_excel("data/transactions_excel.xlsx") == []
