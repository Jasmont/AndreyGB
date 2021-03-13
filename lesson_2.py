def task_1():
    print('Task 1')

    print(f'15 * 3 type: {type(15 * 3)}')
    print(f'15 / 3 type: {type(15 / 3)}')
    print(f'15 // 2 type: {type(15 // 2)}')
    print(f'15 ** 2 type: {type(15 ** 2)}')


def task_2_3():
    print('\nTask 2 & 3')

    original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
    index = 0
    end_of_list = len(original_list)

    while index < end_of_list:
        if original_list[index][-1].isdigit():
            original_list[index: index + 1] = ['"',
                                               original_list[index][:-1] + '0' + original_list[index][-1]
                                               if int(original_list[index]) // 10 == 0
                                               else original_list[index],
                                               '"']
            index += 2
            end_of_list = len(original_list)
        index += 1

    print(original_list)

    string_from_list = ''

    for i in original_list:
        if i.isalpha():
            string_from_list += i + ' '
        elif i[-1].isdigit():
            string_from_list += '"' + i + '" '

    print(string_from_list)


def task_4():
    print('\nTask 3')

    original_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
                     'директор аэлита']
    for i in original_list:
        print(f'Привет, {i.split()[-1].title()}!')


def task_5():
    import random

    print('\nTask 4')

    original_list = [57.8, 46.51, 97] + [round(random.uniform(10., 100.), 2) for _ in range(7)]

    print('Original list: ' + str(original_list))

    subtask_list_1 = [str(i).split('.')[0] + ' руб ' + str(i).split('.')[1] + ' коп'
                      if len(str(i).split('.')) > 1
                      else str(i) + ' руб 00 коп'
                      for i in original_list]
    print('Subtask #1: ' + ', '.join(subtask_list_1))

    subtask_list_2 = [str(i).split('.')[0] + ' руб ' + str(i).split('.')[1] + ' коп'
                      if len(str(i).split('.')) > 1
                      else str(i) + ' руб 00 коп'
                      for i in sorted(original_list)]
    print('Subtask #2: ' + ', '.join(subtask_list_2))

    subtask_list_3 = [str(i).split('.')[0] + ' руб ' + str(i).split('.')[1] + ' коп'
                      if len(str(i).split('.')) > 1
                      else str(i) + ' руб 00 коп'
                      for i in sorted(original_list, reverse=True)]
    print('Subtask #3: ' + ', '.join(subtask_list_3))

    print('Subtask #4: ' + ', '.join(subtask_list_3[:5]))


if __name__ == '__main__':
    task_1()
    task_2_3()
    task_4()
    task_5()



