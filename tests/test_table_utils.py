# the test_table_utils module.

from unittest.mock import Mock, patch

from src.table_utils import read_csv


@patch("csv.DictReader")
def test_read_csv(mock_csv: Mock) -> None:
    """testing the read_csv function for get transaction data"""

    csv_data = [{"id": 111, "state": "EXECUTED", "date": "2024-12-15",
                 "amount": 111, "currency_name": "Ruble", "currency_code": "RUB",
                 "description": "test", "from": "Master Card", "to": "Visa"}]
    data = [{"id": 111, "state": "EXECUTED", "date": "2024-12-15",
             "operationAmount": {"amount": "111", "currency": {"name": "Ruble", "code": "RUB"}},
             "description": "test", "from": "Master Card", "to": "Visa"}]
    mock_csv.return_value = csv_data
    assert read_csv("data/transactions.csv") == data
