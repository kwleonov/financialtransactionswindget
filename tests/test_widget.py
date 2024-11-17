import pytest

from src.widget import get_date, mask_account_card


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


@pytest.mark.parametrize(
    "date_time, date",
    [
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2018-09-12T21:27:25.241689", "12.09.2018"),
        ("2018-10-14T08:21:33.419441", "14.10.2018"),
        ("2016-02-29T08:21:33.419441", "29.02.2016"),
    ],
)
def test_get_date(date_time: str, date: str) -> None:
    """Testing the correctness of the date conversion."""

    out = get_date(date_time)
    assert out == date


@pytest.mark.parametrize(
    "date_time",
    [
        (""),
        ("T21:27:25.241689"),
        ("2018-6-30"),
        ("6-30T21:27:25.241689"),
        ("2000-15-21"),
        ("2001-01-32"),
        ("22AA-01-01T21:27:25.241689"),
        ("2100-Fb-01T21:27:25.241689"),
        ("2100-02-AAT21:27:25.241689"),
        ("18-09-2012T21:27:25.241689"),
        ("2018-09-2012T21:27:25.241689"),
        ("2018-14-12T08:21:33.419441"),
        ("2018-11-31T08:21:33.419441"),
        ("2018-06-31T08:21:33.419441"),
        ("2100-02-29T08:21:33.419441"),
        ("2000-02-30T08:21:33.419441"),
    ],
)
def test_get_incorrect_date(date_time: str) -> None:
    """Testing get incorrect date."""

    out = get_date(date_time)
    assert out == "Incorrect date"
