import os
import warnings

if __name__ == '__main__':
    with open('config.yaml', 'r', encoding='utf-8') as config_file:
        default_project_name = 'my_project'
        parent_folder = ''
        try:
            for i in config_file.readlines():
                entity = i.strip().split('-')

                if len(entity) == 2:
                    default_project_name = i.strip().split('-')[-1]
                    os.mkdir(default_project_name)

                if len(entity) == 3:
                    parent_folder = entity[-1]
                    os.mkdir(os.path.join(default_project_name, entity[-1]))

                if len(i.strip().split('-')) == 4:
                    subfolder = os.path.join(default_project_name, parent_folder)
                    if entity[-1].count('.') > 0:
                        if not os.path.exists(os.path.join(subfolder, entity[-1])):
                            open(os.path.join(subfolder, entity[-1]), 'w').close()
                    else:
                        os.mkdir(os.path.join(subfolder, entity[-1]))

            for (a, b, c) in os.walk(default_project_name):
                if 'templates' in b:
                    temp_entity = a.split('\\')[1]
                    os.chdir(os.path.join(a, b[0]))
                    os.mkdir(temp_entity)
                    open(temp_entity + '\\base.html', 'w').close()
                    open(temp_entity + '\\index.html', 'w').close()
                    os.chdir('../../..')

        except FileExistsError:
            warnings.warn('File already exists')
