from typing import Dict, List
import random

en_ru_dictionary: Dict[str, str] = {
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",
    "ten": "десять"
}


def num_translate(string_number: str):
    """
    Функция переводит строковое представление чисел от 0-10 в русский язык.

    :param string_number: строковый литерал числа от 0-10;
    :return: возвращает пустую строку если не передается ничего или нет в словаре, иначе возвращает перевод.
    """
    return \
        None if string_number is None or string_number not in en_ru_dictionary.keys() \
            else en_ru_dictionary[string_number]


def num_translate_adv(string_number: str):
    """
    Усложненная функция. Функция переводит строковое представление чисел от 0-10 в русский язык c учетом регистра.

    :param string_number: строковый литерал числа от 0-10;
    :return: возвращает пустую строку если не передается ничего или нет в словаре, иначе возвращает перевод.
    """

    is_capital: bool = string_number[0].isupper()

    return \
        None if string_number is None or string_number.lower() not in en_ru_dictionary.keys() \
            else en_ru_dictionary[string_number.lower()] if not is_capital else en_ru_dictionary[
            string_number.lower()].title()


def thesaurus(*args: str):
    """
    Функция создает словарь с ключем из первой буквы имени и со списом значений имен.

    :param args: неопределенное колличество строковых литералов состоящих из имен
    :return: возвращает словарь обработанных имен
    """
    firstnames_dictionary: Dict[str, List[str]] = dict()

    for i in args:
        item: str = i[0].upper()

        if item in firstnames_dictionary:
            firstnames_dictionary[item].append(i.title())
        else:
            firstnames_dictionary[item] = [i]

    return {k: v for k, v in sorted(firstnames_dictionary.items())}


def thesaurus_adv(*args: str):
    """
    Функция создает словарь с ключем из первой буквы отчества, внутреннего словаря с ключем из первой буквы имени и
    со списом значений полученных имен.

    :param args: неопределенное колличество строковых литералов состоящих из имен
    :return: возвращает словарь обработанных имен
    """
    patronymic_firstname_dictionary = dict()

    for i in args:
        patronymic_firstname_dictionary[i.split()[1][0].upper()] = {}

    for j in args:
        p_val: str = j.split()[1][0].upper()
        f_val: str = j.split()[0][0].upper()

        if f_val not in patronymic_firstname_dictionary[p_val]:
            patronymic_firstname_dictionary[p_val][f_val] = [j]
        else:
            patronymic_firstname_dictionary[p_val][f_val].append(j)

    return {k: v for k, v in sorted(patronymic_firstname_dictionary.items())}


def get_jokes(jokes_amount: int):
    """
    Функция возвращает n шуток, сформированных из двух случайных слов, взятых из трёх списков:
    nouns, adverbs, adjectives.

    :param jokes_amount: количество шуток, которое надо вернуть
    :return: возвращает сгенерированный список шуток
    """
    nouns: List[str] = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs: List[str] = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives: List[str] = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    return [f'{random.choice(nouns)} '
            f'{random.choice(adverbs)} '
            f'{random.choice(adjectives)}'
            for _ in range(jokes_amount)]


if __name__ == '__main__':
    print('Task #1:')
    print(num_translate("one"))
    print(num_translate("eight"))
    print(num_translate("None"))

    print('\nTask #2:')
    print(num_translate_adv("One"))
    print(num_translate_adv("eight"))
    print(num_translate_adv("None"))

    print('\nTask #3:')
    print(thesaurus("Иван", "Мария", "Петр", "Илья", "леха"))

    print('\nTask #4:')
    print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "семен семеныч"))

    print('\nTask #5:')
    print(get_jokes(2))
