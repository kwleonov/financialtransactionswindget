# Module masks


def get_mask_card_number(card_number: str) -> str:
    """Function get_mask_card_number(card_number: str) -> str gets card
    number XXXXXXXXXXXXXXXX (12 digits) and return mask XXXX XX** **** XXXX,
    where X is digit."""

    invalid_format = "Invalid card number format"
    empty_card_number = "Get empty card number"
    card_number = card_number.replace(" ", "")

    if len(card_number) == 0:
        return empty_card_number

    if len(card_number) < 13:
        return invalid_format

    if not card_number.isdigit():
        return invalid_format

    # Divide firts digits into groups of 4 digits

    first_digits = card_number[:-12]
    first_digits_group = list()
    if len(first_digits) > 4:
        first_group_length = len(first_digits) % 4
        start_index = 0
        if first_group_length != 0:
            first_digits_group.append(first_digits[:first_group_length])
            start_index += first_group_length
        for i in range(start_index, len(first_digits), 4):
            first_digits_group.append(first_digits[i: i + 4])
    else:
        first_digits_group = [first_digits]

    first_digits_str = " ".join(first_digits_group)

    next_2_digits = card_number[-12:-10]
    last_4_digits = card_number[-4:]
    return f"{first_digits_str} {next_2_digits}** **** {last_4_digits}"


def get_mask_account(account_number: str) -> str:
    """Function get_mask_account(account_number: str) -> str gets account
    number XXXXXXXXXXXXXXXXXXXX (20 digits) and return mask **XXXX,
    where XXXX are 4 last digits."""

    account_number = account_number.replace(" ", "")
    account_number_length = len(account_number)

    if account_number_length < 20:
        return "Invalid account number length"

    if not account_number.isdigit():
        return "Invalid account number format"

    last_4_digits = account_number[-4:]
    return f"**{last_4_digits}"
