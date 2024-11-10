# Module processing


def filter_by_state(processes: list, state: str = "EXECUTED") -> list:
    """gets a list of dictionaries and optionally a value for the key the 'state' (by default 'EXECUTED').
    The function returns a new list of dictionaries containing only those dictionaries whose
    'state' key matches the specified value."""

    filtered_processes = list()
    for process in processes:
        if process["state"] == state:
            filtered_processes.append(process)

    return filtered_processes


def sort_by_date(processes: list, is_descending: bool = True) -> list:
    """gets a list of dictionaries and an optional parameter specifying the sort order (by default, descending).
    The function should return a new list sorted by date."""

    sorted_processes = sorted(processes, key=lambda k: k["date"], reverse=is_descending)

    return sorted_processes
