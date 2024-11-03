from src.widget import get_date, mask_account_card


def main() -> None:
    test_data = [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
    ]

    for data_str in test_data:
        mask_str = mask_account_card(data_str)
        print(f"Input: {data_str}\nOutput: {mask_str}")

    date_time = "2024-03-11T02:26:18.671407"
    my_date = get_date(date_time)
    print(f"Input: {date_time}\nOutput: {my_date}")


if __name__ == "__main__":
    main()
