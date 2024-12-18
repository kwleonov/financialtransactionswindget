from typing import TypedDict

from src.generators import filter_by_currency
from src.processing import filter_by_description, filter_by_state, sort_by_date
from src.table_utils import read_csv, read_excel
from src.utils import load_operations_json
from src.widget import get_date, mask_account_card

Currency = TypedDict("Currency", {"name": str, "code": str})
OperationAmount = TypedDict("OperationAmount", {"amount": str, "currency": Currency})
TransactionData = TypedDict("TransactionData", {
    "id": int,
    "state": str,
    "date": str,
    "operationAmount": OperationAmount,
    "description": str,
    "from": str,
    "to": str,
})


def main() -> None:
    """The main function receives information about transactions from a user-specified file,
    filters them by the user-specified status, optionally sorts data by date, optionally shows only ruble transactions,
    optionally filters data by a specific word in the transaction description."""

    filename_json = "data/operations.json"
    filename_csv = "data/transactions.csv"
    filename_excel = "data/transactions_excel.xlsx"

    # Greeting

    print("""Программа: Привет! Добро пожаловать в программу работы
    банковскими транзакциями.""")

    transactions_data: list[TransactionData] = []

    # Getting transactions data

    is_select = False
    while not is_select:
        print("""Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла""")
        try:
            user_select = input("Пользователь: ")
        except Exception:
            user_select = "Oops"
        is_select = True

        if user_select == '1' or user_select.upper() == "JSON":
            transactions_data = load_operations_json(filename_json)
            print("Программа: Для обработки выбран JSON-файл.")
        elif user_select == '2' or user_select.upper() == "CSV":
            transactions_data = read_csv(filename_csv)
            print("Программа: Для обработки выбран csv-файл.")
        elif user_select == "3" or user_select.upper() == "EXCEL":
            transactions_data = read_excel(filename_excel)
            print("Программа: Для обработки выбран Excel-файл.")
        else:
            is_select = False
            print("Программа: Пожалуйста выберите 1 или 2 или 3.")

    # Filtering transactions data by state

    is_select = False
    while not is_select:
        print("""Программа: Введите статус, по которому необходимо выполнить фильтрацию.
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        try:
            user_select = input("Пользователь: ")
        except Exception:
            user_select = "Oops"
        is_select = True

        if user_select.upper() == "EXECUTED":
            transactions_data = filter_by_state(transactions_data, "EXECUTED")
            print("Программа: Операции отфильтрованы по статусу \"EXECUTED\"")
        elif user_select.upper() == "CANCELED":
            transactions_data = filter_by_state(transactions_data, "CANCELED")
            print("Программа: Операции отфильтрованы по статусу \"CANCELED\"")
        elif user_select.upper() == "PENDING":
            transactions_data = filter_by_state(transactions_data, "PENDING")
            print("Программа: Операции отфильтрованы по статусу \"PENDING\"")
        else:
            is_select = False
            print(f"Программа: Статус операции \"{user_select}\" недоступен.")

    # Sort by date

    print("Программа: Отсортировать операции по дате? Да/Нет")
    is_select = False
    is_sort_by_data = False

    while not is_select:
        try:
            user_select = input("Пользователь: ")
        except Exception:
            user_select = "Oops"
        is_select = True
        if user_select.upper() == "ДА":
            is_sort_by_data = True
        elif user_select.upper() == "НЕТ":
            continue
        else:
            is_select = False
            print("Программа: Пожалуйста выберите один из ответов: Да или Нет.")

    if is_sort_by_data:
        is_descending = False
        is_select = False
        print("Программа: Отсортировать по возрастанию или по убыванию?")
        while not is_select:
            try:
                user_select = input("Пользователь: ")
            except Exception:
                user_select = "Oops"
            is_select = True
            if user_select.lower() == "по возрастанию" or user_select.lower() == "возрастанию":
                continue
            elif user_select.lower() == "по убыванию" or user_select.lower() == "убыванию":
                is_descending = True
            else:
                is_select = False
                print("Программа: Пожалуйста выберите один из ответов: по возрастанию или по убыванию.")
        transactions_data = sort_by_date(transactions_data, is_descending)

    # filtering by Rub

    print("Программа: Выводить только рублевые транзакции? Да/Нет")
    is_select = False

    while not is_select:
        try:
            user_select = input("Пользователь: ")
        except Exception:
            user_select = "Oops"
        is_select = True
        if user_select.upper() == "ДА":
            transactions_data = list(filter_by_currency(transactions_data, "RUB"))
        elif user_select.upper() == "НЕТ":
            continue
        else:
            print("Программа: Пожалуйста выберите один из ответов: Да или Нет.")

    # Filtering by description

    print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    is_select = False

    while not is_select:
        try:
            user_select = input("Пользователь: ")
        except Exception:
            user_select = "Oops"
        is_select = True
        if user_select.upper() == "ДА":
            print("Программа: Пожалуйста введите по какому слову нужно отфильтровать список транзакций")
            is_select_word = False
            word = ""

            while not is_select_word:
                try:
                    word = input("Пользователь: ")
                    is_select_word = True
                except Exception:
                    is_select_word = False
                    print("Вовремя ввода произошла ошибка, пожалуйста повторите ввод")
            transactions_data = filter_by_description(transactions_data, word)
        elif user_select.upper() == "НЕТ":
            continue
        else:
            is_select = False
            print("Программа: Пожалуйста выберите один из ответов: Да или Нет.")

    # output of the final list of transactions

    if len(transactions_data) == 0:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Программа: Распечатываю итоговый список транзакций...")
        print("Программа:")
        print(f"Всего банковских операций в выборке: {len(transactions_data)}")
        for transaction in transactions_data:
            print()
            date = get_date(transaction["date"])
            description = transaction["description"]
            print(f"{date} {description}")
            from_ = ""
            if "from" in transaction:
                from_ = transaction["from"]
            to_ = transaction["to"]
            if from_ != from_ or from_ == "":
                print(f"{mask_account_card(to_)}")
            else:
                print(f"{mask_account_card(from_)} -> {mask_account_card(to_)}")
            amount = transaction["operationAmount"]["amount"]
            currency_name = transaction["operationAmount"]["currency"]["name"]
            print(f"Сумма: {amount} {currency_name}")


if __name__ == "__main__":
    main()
