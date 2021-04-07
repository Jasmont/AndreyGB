import os
import sys
import warnings

ROOT_PATH = os.getcwd()
FOLDERS = ['settings', 'mainapp', 'adminapp', 'authapp']


if __name__ == '__main__':
    default_directory_name = 'my_project'

    if len(sys.argv) > 1:
        default_directory_name = sys.argv[1]

    try:
        os.mkdir(os.path.join(ROOT_PATH, default_directory_name))
        os.chdir(default_directory_name)

        for folder in FOLDERS:
            os.makedirs(folder)

    except FileExistsError:
        warnings.warn('Project already exists!')
        os.chdir(default_directory_name)

        for folder in FOLDERS:
            os.makedirs(folder, exist_ok=True)
