import os
stat_dict: dict = {10 ** i: 0 for i in range(1, 6)}


if __name__ == '__main__':
    os.chdir('../')
    for root, folder, files in os.walk('.'):
        for file in files:
            size = os.stat(os.path.join(root, file)).st_size
            counter = 1
            while counter < 6:
                if size % (10 ** counter) == 0:
                    stat_dict[(10 ** counter)] += 1
                counter += 1

    for (index, item) in stat_dict.items():
        print(f'{index} : {item}')
