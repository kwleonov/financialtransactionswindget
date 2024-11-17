# Module processing

from src.widget import get_date


def filter_by_state(processes: list[dict[str, int | str]], state: str = "EXECUTED") -> list[dict[str, int | str]]:
    """gets a list of dictionaries and optionally a value for the key the 'state' (by default 'EXECUTED').
    The function returns a new list of dictionaries containing only those dictionaries whose
    'state' key matches the specified value."""

    filtered_processes = list()
    for process in processes:
        if process["state"] == state:
            filtered_processes.append(process)

    return filtered_processes


def sort_by_date(processes: list[dict[str, int | str]], is_descending: bool = True) -> list[dict[str, int | str]]:
    """gets a list of dictionaries and an optional parameter specifying the sort order (by default, descending).
    The function should return a new list sorted by date."""

    correct_processes = list()
    for process in processes:
        date_time = str(process["date"])
        date = get_date(date_time)
        if date != "Incorrect date":
            correct_processes.append(process)

    sorted_processes = sorted(correct_processes, key=lambda k: k["date"], reverse=is_descending)

    return sorted_processes
