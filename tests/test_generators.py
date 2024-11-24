# Test for the generators module

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions):
    """testing filtering transactions by currency."""

    transactions_by_USD = filter_by_currency(transactions, "USD")
    for transaction in transactions_by_USD:
        assert transaction["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_KGS_currency(transactions):
    """testing filtering by 'Kazakhstan some' have to return an empty list."""

    transactions_by_KGS = filter_by_currency(transactions, "KGS")
    list_transactions = list(transactions_by_KGS)
    assert len(list_transactions) == 0


@pytest.mark.parametrize("transaction_list, currency_code", [
    ([
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
     ], "RUB"),
    ([], "")
])
def test_filter_by_empty_currency_transactions(transaction_list, currency_code):
    """testing filtering by an empty transactions list or an empty currency."""

    transactions = list(filter_by_currency(transaction_list, currency_code))
    assert len(transactions) == 0


def test_transaction_descriptions(transactions):
    """testing getting transaction's description."""

    answers = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]

    get_transactions_description = transaction_descriptions(transactions)

    for answer in answers:
        description = next(get_transactions_description)
        assert description == answer


def test_by_empty_transaction_descriptions():
    """esting getting transaction's description with the empty transactions list."""

    get_transactions_description = transaction_descriptions([])
    descriptions = list(get_transactions_description)
    assert len(descriptions) == 0


@pytest.mark.parametrize(
    "start_number, stop_number, list_numbers",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
    ],
)
def test_card_number_generator(start_number, stop_number, list_numbers):
    """testing getting card numbers."""

    get_card_number = card_number_generator(start_number, stop_number)

    for number in list_numbers:
        card_number = next(get_card_number)
        assert number == card_number
