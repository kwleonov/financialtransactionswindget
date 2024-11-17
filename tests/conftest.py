import pytest


@pytest.fixture
def card_numbers() -> dict[str, list[str]]:
    """list of card numbers"""

    card_numbers = [
        "Maestro 1596837868705199",
        "MasterCard 7158300734726758",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
    ]

    masks = [
        "XXXX XX78 6870 XXXX",
        "XXXX XX07 3472 XXXX",
        "XXXX XX24 7673 XXXX",
        "XXXX XX21 1366 XXXX",
        "XXXX XX42 2842 XXXX",
    ]

    test_data: dict[str, list[str]] = {"card_number": card_numbers, "mask": masks}

    return test_data
