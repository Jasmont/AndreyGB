from typing import List


def read_logs(filename: (str, "название файла для чтения")) -> List[tuple]:
    """
    Функция читает построчно файл и выводит инфу о запросе от кого, тип и куда

    :param filename: название файла для чтения
    :return: None
    """
    result: List[tuple] = []
    
    with open(filename, 'r', encoding='utf-8') as file:
        for item in file:
            line = item.strip().split()
            request_from = line[0]
            request_type = line[5].replace('"', '')
            request_target = line[6]
            result.append((request_from, request_type, request_target))
    
    return result


if __name__ == '__main__':
    for i in read_logs('nginx_logs.txt'):
        print(i)
