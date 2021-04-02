import sys
import os
from task_4 import user_hobby_parser

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Please specify 2 input files and 1 output file. Ex: py task_5.py hobby.csv users.csv task_5_result.txt')
    else:
        for i in sys.argv[1:3]:
            if i not in os.listdir():
                print(f'File {i} is not found in the current directory')
                exit(1)

        user_hobby_parser(sys.argv[1], sys.argv[2], sys.argv[3])
