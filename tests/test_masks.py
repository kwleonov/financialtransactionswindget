import pytest

from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "card_number, mask",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("8990922113665229", "8990 92** **** 5229"),
        ("5999414228426353", "5999 41** **** 6353"),
    ],
)
def test_get_mask_card_number(card_number: str, mask: str) -> None:
    """testing the correctness of masking a card number."""

    out = get_mask_card_number(card_number)
    assert out == mask


@pytest.mark.parametrize(
    "card_number, mask",
    [
        ("1596837868705199123", "159 6837 86** **** 9123"),
        ("7158300734726", "7 15** **** 4726"),
        ("5999 4142 2842 6353", "5999 41** **** 6353"),
        ("6831982476", "Invalid card number format"),
        ("899092211", "Invalid card number format"),
        ("5", "Invalid card number format"),
        ("89909221ABCD5229", "Invalid card number format"),
    ],
)
def test_get_mask_non_standard_card_number(card_number: str, mask: str) -> None:
    """checking the operation of the function on various input formats of card numbers,
    including boundary cases and non-standard number lengths."""

    out = get_mask_card_number(card_number)
    assert out == mask


def test_get_mask_empty_card_number() -> None:
    """checking that the function correctly processes input lines where the card number is missing."""

    out = get_mask_card_number("")
    assert out == "Get empty card number"
