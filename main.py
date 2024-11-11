from src.processing import filter_by_state, sort_by_date
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

    test_process_data: list[dict[str, int | str]] = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    print(filter_by_state(test_process_data))
    print(filter_by_state(test_process_data, state="CANCELED"))

    print(sort_by_date(test_process_data))
    print(sort_by_date(test_process_data, is_descending=False))


if __name__ == "__main__":
    main()
