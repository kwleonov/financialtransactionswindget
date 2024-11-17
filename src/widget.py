# Module widget

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_or_card_number: str) -> str:
    """Get string of type and number card or bank account and return it with mask number
    Example:
        Visa Platinum 7000792289606361 -> Visa Platinum 7000 79** **** 6361
        Счет 73654108430135874305      -> Счет **4305"""

    split_number = account_or_card_number.split()
    if len(split_number) < 2:
        return "Incorrect data"

    type_number = " ".join(split_number[:-1])
    number = split_number[-1]
    mask_number = ""

    if type_number == "Счет":
        mask_number = get_mask_account(number)
    else:
        mask_number = get_mask_card_number(number)

    return f"{type_number} {mask_number}"


def get_date(date_time: str) -> str:
    """Get date and time in format '2024-03-11T02:26:18.671407'
    and return date in format 'DD.MM.YYYY' ('11.03.2004')"""

    incorrect_date = "Incorrect date"

    if len(date_time) < 10:
        return incorrect_date

    split_date_time = date_time.split("T")
    if len(split_date_time) != 2:
        return incorrect_date

    split_date = split_date_time[0].split("-")
    if len(split_date) < 3:
        return incorrect_date

    year = split_date[0]
    if len(year) < 4 or not year.isdigit():
        return incorrect_date

    month = split_date[1]
    if len(month) > 2 or not month.isdigit():
        return incorrect_date
    if int(month) > 12:
        return incorrect_date

    day = split_date[2]
    if len(day) > 2 or not day.isdigit():
        return incorrect_date
    if int(day) > 31:
        return incorrect_date
    if int(month) in [4, 6, 9, 11] and int(day) > 30:
        return incorrect_date
    if int(month) == 2:
        is_leap_year = False
        if int(year) % 4 == 0:
            is_leap_year = True
        if int(year) % 100 == 0:
            is_leap_year = False
        if int(year) % 400 == 0:
            is_leap_year = True
        if is_leap_year and int(day) > 29:
            return incorrect_date
        if not is_leap_year and int(day) > 28:
            return incorrect_date

    return f"{day}.{month}.{year}"
