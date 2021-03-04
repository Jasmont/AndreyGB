from datetime import datetime
import calendar

SECS = 60
MINS = 60
HOURS = 24


def task1(dur_in_secs: int):
    min, sec = divmod(dur_in_secs, SECS)
    hour, min = divmod(min, MINS)
    _, hour = divmod(hour, HOURS)

    print(f'до суток:\t'
          f'{hour} час. '
          f'{min} мин. '
          f'{sec} сек;')


def digit_sum_can_div_7(digit: int):
    return sum([int(i) for i in str(digit)]) % 7 == 0


def task2():
    lst = [i ** 3 for i in range(1001) if i % 2 != 0]
    print('Sum: ', sum([i for i in lst if digit_sum_can_div_7(i)]))
    print('Sum (+17): ', sum([i + 17 for i in lst if digit_sum_can_div_7(i)]))


def task3(perc: int):
    if perc < 1 or perc > 20:
        return

    lst = ['процент', 'процента', 'процентов']

    if perc % 10 == 1:
        print(perc, 'процент')
    elif perc % 10 in [2, 3, 4]:
        print(perc, 'процента')
    else:
        print(perc, 'процентов')

    print('\nСклонения:')
    for i in lst:
        print(i.capitalize())


if __name__ == '__main__':
    print('Task #1')
    duration = int(input('Введите секунды: '))
    task1(duration)
    print('\nTask #2')
    task2()
    print('\nTask #3')
    percentage = int(input('Введите процент (1 - 20): '))
    task3(percentage)
