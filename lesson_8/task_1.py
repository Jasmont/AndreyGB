import re
PATTERN = re.compile(r'[@.]')


def email_parse(email: str):
    """
    Функция принемает строку почтового ящика и возвращает словарь с именем и доменом

    :param email: строка почтового ящика
    :return: словарь с именем и доменом
    """
    list_of_items = re.split(PATTERN, email)
    if len(list_of_items) < 3:
        raise ValueError(f'wrong email: {email}')
    return {'username': list_of_items[0],
            'domain': list_of_items[1]}


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    print(email_parse('someone@geekbrainsru'))
