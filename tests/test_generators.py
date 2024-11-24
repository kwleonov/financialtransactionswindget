# Test for the generators module

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
