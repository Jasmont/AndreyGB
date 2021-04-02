
def user_hobby_parser(filename1: str, filename2: str, filename3: str):
    """
    Функция принимает названия файлов с данными о пользователях и хобби, преобразовывает и записывает в последний файл
    :param filename1: файл с хобби
    :param filename2: файл с именами
    :param filename3: файл вывода обработанного результата
    :return: None
    """
    with open(filename1, 'r', newline='\n', encoding='utf-8') as file1, \
         open(filename2, 'r', newline='\n', encoding='utf-8') as file2, \
         open(filename3, 'w', encoding='utf-8', newline='') as file3:
        for (hobby, user) in zip(file1, file2):
            file3.write(f'{user.replace(",", " ").strip()}: {hobby}')


if __name__ == '__main__':
    user_hobby_parser('hobby.csv', 'users.csv', 'task_4_result.txt')

    with open('task_4_result.txt', 'r', encoding='utf-8') as f:
        for i in f:
            print(i.strip())
