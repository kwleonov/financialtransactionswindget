# Module processing

import re
from typing import TypedDict

from src.widget import get_date

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


def filter_by_state(processes: list[TransactionData], state: str = "EXECUTED") -> list[TransactionData]:
    """gets a list of dictionaries and optionally a value for the key the 'state' (by default 'EXECUTED').
    The function returns a new list of dictionaries containing only those dictionaries whose
    'state' key matches the specified value."""

    filtered_processes = list()
    for process in processes:
        if "state" not in process:
            continue
        if process["state"] == state:
            filtered_processes.append(process)

    return filtered_processes


def sort_by_date(processes: list[TransactionData], is_descending: bool = True) -> list[TransactionData]:
    """gets a list of dictionaries and an optional parameter specifying the sort order (by default, descending).
    The function should return a new list sorted by date."""

    correct_processes = list()
    for process in processes:
        if "date" not in process:
            continue
        date_time = str(process["date"])
        date = get_date(date_time)
        if date != "Incorrect date":
            correct_processes.append(process)

    sorted_processes = sorted(correct_processes, key=lambda k: k["date"], reverse=is_descending)

    return sorted_processes


def filter_by_description(processes: list[TransactionData], word: str) -> list[TransactionData]:
    """gets a list of transactions filtered by 'description' with 'word'"""

    r = re.compile(word, re.IGNORECASE)
    filtered_transactions = filter(lambda x: r.search(x["description"]), processes)

    return list(filtered_transactions)
