import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
    "account_card, mask",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(account_card: str, mask: str) -> None:
    """tests to verify that the function correctly recognizes and applies the desired type of
    masking, depending on the type of input data (card or account)."""

    out = mask_account_card(account_card)
    assert out == mask


@pytest.mark.parametrize(
    "account_card, mask",
    [
        ("Maestro 5", "Maestro Invalid card number format"),
        ("Счет 3538-3033-4744-4789-5560", "Счет Invalid account number format"),
        ("MasterCard ", "Incorrect data"),
        ("Счет 7365410843ABCD0135874305", "Счет Invalid account number format"),
        ("Visa Gold 89909221ABCD5229", "Visa Gold Invalid card number format"),
        ("Счет 3033474447895560", "Счет Invalid account number length"),
    ],
)
def test_mask_incorrect_account_card(account_card: str, mask: str) -> None:
    """Testing the function for processing incorrect input data and
    checking it\'s error tolerance."""

    out = mask_account_card(account_card)
    assert out == mask
