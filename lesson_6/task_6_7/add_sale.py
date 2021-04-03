import sys, warnings
ERROR_MESSAGE = 'Пожалуйста, введите сумму!'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        warnings.warn(ERROR_MESSAGE)
    else:
        try:
            item: float = float(sys.argv[1].replace(',', '.'))
            with open('bakery.csv', 'a', encoding='utf-8') as file:
                file.write(str(item) + '\n')
        except ValueError:
            warnings.warn(ERROR_MESSAGE)
