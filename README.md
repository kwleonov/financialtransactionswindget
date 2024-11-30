# Financial Transactions Widget
## *(Виджет финансовых операций)*
Modules:
- **src/masks**
    - get_mask_card_number(card_number: str) -> str - *gets card number XXXXXXXXXXXXXXXX (12 digits) and
  return mask XXXX XX\*\* \*\*\*\* XXXX, where X is digit.*
    - get_mask_account(account_number: str) -> str - *gets account number XXXXXXXXXXXXXXXXXXXX (20 digits) and
  return mask \*\*XXXX, where XXXX are 4 last digits.*
- **src/widget**
  - mask_account_card(account_or_card_number: str) -> str - *gets string of type and number card or bank account and
  return it with mask number.*  
  Example:
    - Visa Platinum 7000792289606361 -> Visa Platinum 7000 79** **** 6361
    - Счет 73654108430135874305 -> Счет **4305
  - get_date(date_time: str) -> str \- *gets date and time in format '2024-03-11T02:26:18.671407'
    and return date in format 'DD.MM.YYYY' ('11.03.2004')*
- **src/processing**
  - filter_by_state(processes: list[dict[str, int | str]], state: str="EXECUTED") -> list[dict[str, int | str]] -
  *gets a list of dictionaries and optionally a value for the key the 'state' (by default 'EXECUTED').  
  The function returns a new list of dictionaries containing only those dictionaries whose 'state' key matches
  the specified value.*
  - sort_by_date(processes: list[dict[str, int | str]], is_descending: bool=True) -> list[dict[str, int | str]] -
  *gets a list of dictionaries and an optional parameter specifying the sort order (by default, descending).  
  The function should return a new list sorted by date.*
- **src/generators**
  - filter_by_currency(transactions, currency_code) - *The function get a list of dictionaries representing 
  transactions as input. The function should return an iterator that alternately issues transactions where 
  the transaction currency corresponds to the specified one (for example, USD).*
  - transaction_descriptions(transactions): - *The generator, which takes a list of dictionaries with transactions and 
  returns a description of each operation in turn.*
  - card_number_generator(start_number, stop_number) - The generator, which issues bank card numbers in the format 
  XXXX XXXX XXXX XXXX, where X is the digit of the card number.  
  The generator can generate card numbers in the specified range from 0000 0000 0000 0001 to 9999 9999 9999 9999.  
  The generator must take initial and final values to generate a range of numbers.
- **src/decorators**
  - log(filename) - *a decorator for logging the execution of the wrapped function. Logging includes:*
    - *The name of the function and the result of the successful operation.*
    - *The name of the function, the type of error that occurred, and the input parameters if the execution of 
    the function resulted in an error.*
- **tests/test_masks**
  - test_get_mask_card_number() - *testing the correctness of masking a card number.*
  - test_get_mask_non_standard_card_number() - *checking the operation of the function on various input formats of
  card numbers, including boundary cases and non-standard number lengths.*
  - test_get_mask_empty_card_number() - *checking that the function correctly processes input lines where
  the card number is missing.*
  - test_get_mask_account() - *testing the correctness of masking an account number.*
  - test_get_mask_different_account_format() - *checking the operation of the function on various input formats of
  account numbers.*
  - test_get_mask_small_account_length() - *checking that the function correctly processes input data where
  the account number is less than the expected length.*
- **tests/test_widget**
  - test_mask_account_card() - *Tests to verify that the function correctly recognizes and applies the desired type of
  masking, depending on the type of input data (card or account).*
  - test_mask_incorrect_account_card() - *Testing the function for processing incorrect input data and
  checking it\'s error tolerance.*
  - test_get_date() - *Testing the correctness of the date conversion.*
  - test_get_incorrect_date() - *Testing get incorrect date.*
- **teats/test_processing**
  - test_filter_by_state() - *Testing the filtering of a list of dictionaries by a given state status.*
  - test_sort_by_date() - *Testing the sorting of the dictionary list by date in descending and ascending order.*
  - test_sort_by_incorrect_data - *Testing sort by incorrect date.*
- **tests/test_generators**
  - test_filter_by_currency() - *testing filtering transactions by currency.*
  - test_filter_by_KGS_currency() - *testing filtering by 'Kazakhstan some' have to return an empty list.*
  - test_filter_by_empty_currency_transactions() - *testing filtering by an empty transactions list or 
  an empty currency.*
  - test_transaction_descriptions() - *testing getting transaction's description.*
  - test_by_empty_transaction_descriptions() - *testing getting transaction's description with 
  the empty transactions list.*
  - test_card_number_generator() - *testing getting card numbers.*
  - test_card_number_format() - *testing correcting card number format.*
  - test_bad_card_number_range() - *testing for an incorrect range of card numbers.*
- **tests/test_decorators**
  - test_log() - *the test of logging the execution of the wrapped function, the call of which ended without errors.*
  - test_log_error() - *the test for the log decorator when an error is called as a result of executing 
  the wrapped function.*