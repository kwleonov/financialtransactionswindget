# the test_utils module

from typing import TypedDict
from unittest.mock import Mock, patch

import pytest

from src.utils import counter_category, get_transaction_amount, load_operations_json

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


@patch('builtins.open')
def test_load_operations_json(mock_file: Mock) -> None:
    """testing loading list of transaction data from json file."""

    json_data = '[{"id": 111, "state": "EXECUTED"}]'
    data = [{"id": 111, "state": "EXECUTED"}]
    mock_json = mock_file.return_value.__enter__.return_value
    mock_json.read.return_value = json_data
    assert load_operations_json("data/operations.json") == data
    mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")


@patch('builtins.open')
def test_exception_load_operations_json(mock_file: Mock) -> None:
    """testing loading incorrect json file."""

    json_data = '[{"id": 111, "state": "EXECUTED"]'
    mock_json = mock_file.return_value.__enter__.return_value
    mock_json.read.return_value = json_data
    assert load_operations_json("data/operations.json") == []


def test_load_not_exist_operations_json() -> None:
    """testing loading not exist json file."""

    assert load_operations_json("data/nonexist.json") == []


@patch('builtins.open')
def test_empty_load_operations_json(mock_file: Mock) -> None:
    """testing loading empty json file."""

    json_data = ''
    mock_json = mock_file.return_value.__enter__.return_value
    mock_json.read.return_value = json_data
    assert load_operations_json("data/operations.json") == []


@patch('builtins.open')
def test_not_list_load_operations_json(mock_file: Mock) -> None:
    """testing not list json file."""

    json_data = '{"id": 111, "state": "EXECUTED"}'
    mock_json = mock_file.return_value.__enter__.return_value
    mock_json.read.return_value = json_data
    assert load_operations_json("data/operations.json") == []


@pytest.mark.parametrize("transaction, amount", [
    (
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {
                        "name": "руб.",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
            },
            9999.0
    ),
    (
            {
                "id": 441945887,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589"
            },
            31957.58
    )
])
def test_get_transaction_amount(transaction: TransactionData, amount: float) -> None:
    """testing getting transaction amount."""

    with patch('requests.get') as mock_convert:
        mock_convert.return_value.json.return_value = {"result": 9999.0}
        assert get_transaction_amount(transaction) == amount


def test_counter_category(transactions: list[TransactionData]) -> None:
    """testing counter_category"""
    categories = ["Перевод"]
    data = {"Перевод": 5}
    assert counter_category(transactions, categories) == data
