# Module masks


def get_mask_card_number(card_number: str) -> str:
    """Function get_mask_card_number(card_number: str) -> str gets card
    number XXXXXXXXXXXXXXXX (12 digits) and return mask XXXX XX** **** XXXX,
    where X is digit."""

    first_4_digits = card_number[:4]
    next_2_digits = card_number[4:6]
    last_4_digits = card_number[-4:]
    return f"{first_4_digits} {next_2_digits}** **** {last_4_digits}"


def get_mask_account(account_number: str) -> str:
    """Function get_mask_account(account_number: str) -> str gets account
    number XXXXXXXXXXXXXXXXXXXX (20 digits) and return mask **XXXX,
    where XXXX are 4 last digits."""

    last_4_digits = account_number[-4:]
    return f"**{last_4_digits}"
