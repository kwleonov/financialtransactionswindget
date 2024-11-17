import pytest

from src.masks import get_mask_card_number


@pytest.mark.parametrize("card_number, mask", [
    ("1596837868705199", "1596 83** **** 5199"),
    ("7158300734726758", "7158 30** **** 6758"),
    ("6831982476737658", "6831 98** **** 7658"),
    ("8990922113665229", "8990 92** **** 5229"),
    ("5999414228426353", "5999 41** **** 6353"),
])
def test_get_mask_card_number(card_number: str, mask: str) -> None:
    """testing the correctness of masking a card number."""

    out = get_mask_card_number(card_number)
    assert out == mask
