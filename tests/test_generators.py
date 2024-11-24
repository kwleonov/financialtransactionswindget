# Test for the generators module

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions):
    """testing filtering transactions by currency."""

    transactions_by_USD = filter_by_currency(transactions, "USD")
    for transaction in transactions_by_USD:
        assert transaction["operationAmount"]["currency"]["code"] == "USD"


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
