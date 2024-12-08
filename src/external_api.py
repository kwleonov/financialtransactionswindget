# The external_api module.

import os

import requests
from dotenv import load_dotenv


def convert_amount(amount: float, code: str, date: str) -> float:
    """converting currency from USD or EURO to RUB with
    Exchange Rates Data API: https://apilayer.com/exchangerates_data-api.
    Need create system environment variables:
    API_KEY, API_RESULT, API_URL with {{CURRENCY}}, {{AMOUNT}}, {{DATE}} for replace
    currency code, amount and date transaction."""

    load_dotenv()

    api_key = os.getenv('API_KEY')

    headers = {
        'apikey': f'{api_key}'
    }

    api_url = os.getenv('API_URL')
    api_url = api_url.replace('{{CURRENCY}}', code)
    api_url = api_url.replace('{{AMOUNT}}', str(amount))
    api_url = api_url.replace('{{DATE}}', date)

    response = requests.get(api_url, headers=headers)

    api_result_key = os.getenv('API_RESULT')
    result_json = response.json()
    result_amount: float = result_json[api_result_key]

    return result_amount
