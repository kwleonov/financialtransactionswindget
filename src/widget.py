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

    split_date = date_time[:10].split("-")
    year = split_date[0]
    month = split_date[1]
    day = split_date[2]
    return f"{day}.{month}.{year}"
