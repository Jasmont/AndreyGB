import csv
import json


def user_hobby_parser(filename1: str, filename2: str):
    with open(filename1, newline='\n', encoding='utf-8') as file1, \
         open(filename2, newline='\n', encoding='utf-8') as file2:

        csv_hobby, csv_users = csv.reader(file1), csv.reader(file2)

        header_length = len(next(csv_hobby))
        file1.seek(0)

        result = {}
        for i in zip(csv_users, csv_hobby):
            result[' '.join(i[0])] = i[1] if len(i[1]) == header_length else i[1] + ([None] * (header_length - len(i[1])))

        with open('task_3_result.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(result))

        with open('task_3_result.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(type(data))
            print(data)


if __name__ == '__main__':
    user_hobby_parser('hobby.csv', 'users.csv')
