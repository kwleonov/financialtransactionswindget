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

    result_amount = 0.0

    load_dotenv()

    api_key = os.getenv('API_KEY')
    if api_key is None:
        return result_amount

    headers = {
        'apikey': f'{api_key}'
    }

    api_url = os.getenv('API_URL')
    if api_url is None:
        return result_amount

    api_url_value = str(api_url)
    api_url_value = api_url_value.replace('{{CURRENCY}}', code)
    api_url_value = api_url_value.replace('{{AMOUNT}}', str(amount))
    api_url_value = api_url_value.replace('{{DATE}}', date)

    response = requests.get(api_url_value, headers=headers)
    result_json = response.json()

    api_result_key = os.getenv('API_RESULT')
    if api_result_key is None:
        return result_amount

    result_amount = result_json[api_result_key]

    return result_amount
