# the generators module


def filter_by_currency(transactions, currency_code):
    """The filter_by_currency function, which get a list of dictionaries representing transactions as input.
    The function should return an iterator that alternately issues transactions where
    the transaction currency corresponds to the specified one (for example, USD)."""

    transactions_by_code = filter(lambda x: x["operationAmount"]["currency"]["code"] == currency_code, transactions)
    return transactions_by_code


def transaction_descriptions(transactions):
    """The generator transaction_descriptions, which takes a list of dictionaries with transactions and
    returns a description of each operation in turn."""

    for transaction in transactions:
        yield transaction["description"]


def card_number_generator():
    pass
