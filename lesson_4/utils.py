import decimal
import requests
import datetime


def currency_rates(currency: str):
    """
    Функция принимает строку кода валюты и возвращает дату запроса и курс.

    :param currency: строка кода валюты, USD/EUR/...
    :return: возвращает кортеж (курс, дата)
    """
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    string_date: str = ''.join(response.headers.get('date').split()[1:4])
    request_date: datetime.date = datetime.datetime.strptime(string_date, '%d%b%Y').date()

    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    buffer = content[content.find(currency.upper()):]
    if buffer == '>':
        return f'None, {request_date.year}-{request_date.month}-{request_date.day}'

    string_fx_rate: str = buffer[buffer.find('<Value>') + 7:buffer.find('</Value>')]
    result: decimal.Decimal = decimal.Decimal(string_fx_rate.replace(',', '.'))

    return f'{result}, {request_date.year}-{request_date.month}-{request_date.day}'
