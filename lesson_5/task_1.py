def odd_nums(number: int):
    """
    Фкнкция возвращает генератор чисел от 1 до number

    :param number: последнее число генератора
    :return: возвращает генератор
    """
    for i in range(1, number + 1, 2):
        yield i


if __name__ == '__main__':
    odd_to_15 = odd_nums(15)
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
    print(next(odd_to_15))
