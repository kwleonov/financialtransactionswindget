# the test_utils module

from unittest.mock import patch

from src.utils import load_operations_json


@patch('builtins.open')
def test_load_operations_json(mock_file):
    """testing loading list of transaction data from json file."""

    json_data = '[{"id": 111, "state": "EXECUTED"}]'
    data = [{"id": 111, "state": "EXECUTED"}]
    mock_json = mock_file.return_value.__enter__.return_value
    mock_json.read.return_value = json_data
    assert load_operations_json("data/operations.json") == data
    mock_file.assert_called_once_with("data/operations.json", "r")


@patch('builtins.open')
def test_exception_load_operations_json(mock_file):
    """testing loading incorrect json file."""

    json_data = '[{"id": 111, "state": "EXECUTED"]'
    mock_json = mock_file.return_value.__enter__.return_value
    mock_json.read.return_value = json_data
    assert load_operations_json("data/operations.json") == []


def test_load_not_exist_operations_json():
    """testing loading not exist json file."""

    assert load_operations_json("data/nonexist.json") == []


@patch('builtins.open')
def test_empty_load_operations_json(mock_file):
    """testing loading incorrect json file."""

    json_data = ''
    mock_json = mock_file.return_value.__enter__.return_value
    mock_json.read.return_value = json_data
    assert load_operations_json("data/operations.json") == []


@patch('builtins.open')
def test_not_list_load_operations_json(mock_file):
    """testing not list json file."""

    json_data = '{"id": 111, "state": "EXECUTED"}'
    mock_json = mock_file.return_value.__enter__.return_value
    mock_json.read.return_value = json_data
    assert load_operations_json("data/operations.json") == []