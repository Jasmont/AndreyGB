import sys
import warnings


if __name__ == '__main__':
    if len(sys.argv) == 1:
        with open('bakery.csv', 'r', encoding='utf-8') as file:
            while True:
                try:
                    print(next(file).strip())
                except StopIteration:
                    break

    elif len(sys.argv) == 2 and sys.argv[1].isdigit():
        with open('bakery.csv', 'r', encoding='utf-8') as file:
            for index, line in enumerate(file):
                item = line.strip()
                if index + 1 > int(sys.argv[1]) - 1:
                    print(item)

    elif len(sys.argv) == 3 and sys.argv[1].isdigit() and sys.argv[2].isdigit():
        with open('bakery.csv', 'r', encoding='utf-8') as file:
            for index, line in enumerate(file):
                item = line.strip()
                if index + 1 > int(sys.argv[1]) - 1:
                    print(item)

                if index + 1 + 1 == int(sys.argv[2]):
                    break

    else:
        warnings.warn('Скрипт может принимать не больше двух переменных типа int! Например: py show_sales.py 1 3.')
        sys.exit(1)
