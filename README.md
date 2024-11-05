# Financial Transactions Widget
## *(Виджет финансовых операций)*
Modules:
- **src/masks**
    - get_mask_card_number(card_number: str) -> str \- *gets card number XXXXXXXXXXXXXXXX (12 digits) and return mask XXXX XX\*\* \*\*\*\* XXXX, where X is digit.*
    - get_mask_account(account_number: str) -> str \- *gets account number XXXXXXXXXXXXXXXXXXXX (20 digits) and return mask \*\*XXXX, where XXXX are 4 last digits.*
- **src/widget**
  - mask_account_card(account_or_card_number: str) -> str \- *gets string of type and number card or bank account and return it with mask number.*
Example:
    - Visa Platinum 7000792289606361 -> Visa Platinum 7000 79** **** 6361
    - Счет 73654108430135874305 -> Счет **4305
  - get_date(date_time: str) -> str \- *gets date and time in format '2024-03-11T02:26:18.671407'
    and return date in format 'DD.MM.YYYY' ('11.03.2004')*
