def find_spammer_in_logs(filename: (str, "название файла для чтения")) -> str:
    """
    Функция читает построчно файл и собирает колличество обращений, возвращает 

    :param filename: название файла для чтения
    :return: None
    """
    result: dict = {}

    with open(filename, 'r', encoding='utf-8') as file:
        for item in file:
            line = item.strip().split()
            if line[0] not in result:
                result[line[0]] = 0
            else:
                result[line[0]] += 1
        
    return max(result, key=result.get)


if __name__ == '__main__':
    print(find_spammer_in_logs('nginx_logs.txt'))
