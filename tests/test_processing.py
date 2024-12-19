from typing import TypedDict

from src.processing import filter_by_description, filter_by_state, sort_by_date

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


def test_filter_by_state(processes: list[TransactionData]) -> None:
    """Testing the filtering of a list of dictionaries by a given state status."""

    out = filter_by_state(processes, state="CANCELED")
    for process in out:
        assert process["state"] == "CANCELED"

    out = filter_by_state(processes)
    for process in out:
        assert process["state"] == "EXECUTED"

    out = filter_by_state(processes, state="UNKNOWN")
    assert len(out) == 0


def test_sort_by_date(processes: list[TransactionData]) -> None:
    """Testing the sorting of the dictionary list by date in descending and ascending order."""

    out = sort_by_date(processes)
    assert len(out) == len(processes)

    for i in range(1, len(out)):
        assert str(out[i - 1]["date"]) >= str(out[i]["date"])

    out = sort_by_date(processes, False)
    for i in range(1, len(out)):
        assert str(out[i - 1]["date"]) <= str(out[i]["date"])


def test_sort_by_incorrect_data(incorrect_processes: list[TransactionData]) -> None:
    """Testing sort by incorrect date."""

    out = sort_by_date(incorrect_processes)
    assert len(out) == 0


def test_filter_by_description(transactions: list[TransactionData]) -> None:
    """testing filtering list of transactions by description with specific word"""

    filtered_transactions = filter_by_description(transactions, "Счет")

    assert len(filtered_transactions) > 0

    for transaction in filtered_transactions:
        description = transaction["description"].lower()
        assert description.find("счет")
