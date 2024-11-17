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