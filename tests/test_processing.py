from src.processing import filter_by_state


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
