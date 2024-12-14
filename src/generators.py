# the generators module

from collections.abc import Generator, Iterable

from src.utils import TransactionData


def filter_by_currency(transactions: list[TransactionData], currency_code: str) -> Iterable[TransactionData]:
    """The filter_by_currency function, which get a list of dictionaries representing transactions as input.
    The function should return an iterator that alternately issues transactions where
    the transaction currency corresponds to the specified one (for example, USD)."""

    transactions_by_code = filter(lambda x: x["operationAmount"]["currency"]["code"] == currency_code, transactions)
    return transactions_by_code


def transaction_descriptions(transactions: list[TransactionData]) -> Generator[str]:
    """The generator transaction_descriptions, which takes a list of dictionaries with transactions and
    returns a description of each operation in turn."""

    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start_number: int, stop_number: int) -> Generator[str]:
    """The generator, which issues bank card numbers in the format
    XXXX XXXX XXXX XXXX, where X is the digit of the card number.
    The generator can generate card numbers in the specified range from 0000 0000 0000 0001 to 9999 9999 9999 9999.
    The generator must take initial and final values to generate a range of numbers."""

    finish_number = 9999_9999_9999_9999

    if start_number > finish_number:
        return
    if start_number < 1:
        start_number = 1
    if stop_number > finish_number:
        stop_number = finish_number

    for number in range(start_number, stop_number + 1):
        str_number = str(number)
        str_number = str_number.rjust(16, "0")

        groups = []
        for i in range(0, 16, 4):
            groups.append(str_number[i: i + 4])

        card_number = " ".join(groups)

        yield card_number
