import os
import sys
import warnings


if __name__ == '__main__':
    if len(sys.argv) != 3 or not sys.argv[1].isdigit():
        warnings.warn('Введите, пожалуйста, правильные параметры. Например: py edit_sales.py 2 1234,5')
        sys.exit(1)

    with open("bakery.csv", "r", encoding='utf-8') as file_input:
        with open("temp.arch", "w", encoding='utf-8') as output:
            for index, line in enumerate(file_input):
                if index != int(sys.argv[1]) - 1:
                    output.write(line)
                else:
                    output.write(sys.argv[2].replace(',', '.') + '\n')

    os.remove('bakery.csv')
    os.rename('temp.arch', 'bakery.csv')
