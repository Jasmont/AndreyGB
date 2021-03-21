from itertools import zip_longest


def lists_iterator(tutor: list, klass: list):
    """
    Функция возвращает генератор пар учитель/класс

    :param tutor: список преподователей
    :param klass: список классов
    :return: генератор пар учитель/класс
    """
    return (i for i in zip_longest(tutor, klass))


if __name__ == '__main__':
    tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена'
    ]
    klasses = [
        '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
    ]

    generator = lists_iterator(tutors, klasses)

    while True:
        try:
            print(next(generator))
        except StopIteration:
            break
