from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(processes: list[dict[str, int | str]]) -> None:
    """Testing the filtering of a list of dictionaries by a given state status."""

    out = filter_by_state(processes, state="CANCELED")
    for process in out:
        assert process["state"] == "CANCELED"

    out = filter_by_state(processes)
    for process in out:
        assert process["state"] == "EXECUTED"

    out = filter_by_state(processes, state="UNKNOWN")
    assert len(out) == 0


def test_sort_by_date(processes: list[dict[str, int | str]]) -> None:
    """Testing the sorting of the dictionary list by date in descending and ascending order."""

    out = sort_by_date(processes)
    assert len(out) == len(processes)

    for i in range(1, len(out)):
        assert str(out[i - 1]["date"]) >= str(out[i]["date"])

    out = sort_by_date(processes, False)
    for i in range(1, len(out)):
        assert str(out[i - 1]["date"]) <= str(out[i]["date"])


def test_sort_by_incorrect_data(incorrect_processes: list[dict[str, int | str]]) -> None:
    """Testing sort by incorrect date."""

    out = sort_by_date(incorrect_processes)
    assert len(out) == 0
