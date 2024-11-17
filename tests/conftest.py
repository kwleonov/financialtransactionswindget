import pytest


@pytest.fixture
def processes() -> list[dict[str, int | str]]:
    """fixture for the test_processing module"""

    test_data: list[dict[str, int | str]] = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    return test_data


@pytest.fixture
def incorrect_processes() -> list[dict[str, int | str]]:
    """fixture for the test_processing module"""

    test_data: list[dict[str, int | str]] = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-32T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-31T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-15-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2100-02-29T08:21:33.419441"},
    ]

    return test_data
