import os
import re


if __name__ == '__main__':
    os.chdir(r'../lesson_6')
    with open(r'nginx_logs.txt', 'r', encoding='utf-8') as file:
        ip = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
        datetime = re.compile(r' - - \[(.*?)\] "')
        request_type = re.compile(r'] "(.*?) /')
        request_target = re.compile(r'(?:GET|HEAD) (.*?) HTTP/1.1')
        response_code = re.compile(r'" (\d{3}) ')
        response_size = re.compile(r'(\d{1,3}) "-"')

        for i in file:
            part = re.findall(ip, i.strip())
            if len(part) > 1:
                print(f'parsed_raw = (\'{part[0]}\', '
                      f'\'{re.findall(datetime, i.strip())[0]}\', '
                      f'\'{re.findall(request_type, i.strip())[0]}\', '
                      f'\'{re.findall(request_target, i.strip())[0]}\', '
                      f'\'{re.findall(response_code, i.strip())[0]}\', '
                      f'\'{re.findall(response_size, i.strip())[0]}\')')
