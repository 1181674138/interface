import os
import re

import yaml


def read_yaml():
    with open(os.path.dirname(os.getcwd()) + r'/token.yml', mode='r', encoding='utf-8') as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
    return value
# {'token': '${token}', 'headers': '${header}', 'body': '${body}', 'data': '${data}'}


def read_ini_yaml():
    with open(os.path.dirname(os.getcwd()) + r'/ini.yml', mode='r', encoding='utf-8') as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
    return value
# {'token': '46e3a4a86b41e884e9ff7d7e39370b3bb318554260eac3abf38dff359bb8b5e78d98be5eecc893914360170b8d992f51c825ff3b2793cc14cc7380bbb797ac75', 'body': {'id': 123, 'switch': 'ok'}}


read_ini_yaml_file = read_ini_yaml()


def read_lines():
    with open(os.path.dirname(os.getcwd()) + r'/testcase/adminMalfunctionList.yml', mode='r', encoding='utf-8') as f:
        value = f.readlines()
        return value


def replace_value(file_so):
    final_list = []

    for line in file_so:
        new_line = line
        if new_line.find('${') > 0:
            env_list = new_line.split(':')
            env_name = env_list[1].strip().split('{', 1)[1].split('}')[0]

            replacement = ""
            if env_name in read_ini_yaml_file.keys():
                replacement = read_ini_yaml_file[env_name]
                new_line = new_line.replace(env_list[1].strip(), str(replacement))

        final_list.append(new_line)
    return final_list


replace_value(read_lines())
print(replace_value(read_lines()))

data = [{'name': '正常用例', 'method': 'post', 'url': 'https://task.letfungo.com/api/task/show/adminMalfunctionList',
         'param_type': 'FORM', 'data': {'token': '${token}', 'type':'${token}', 'pageNum': 1, 'pageSize': 10}, 'assert': {'contain': None, 'eq': {'msg': '请求成功', 'code': 0}, 'not_null': ['add_time', 'created_at', 'ebike_no']}}, {'name': '正常用例', 'method': 'post', 'url': 'https://task.letfungo.com/api/task/show/adminMalfunctionList', 'param_type': 'FORM', 'data': {'token': 'c10363237f8e01ed34db47667d049ccbb318554260eac3abf38dff359bb8b5e720a85f14a7d2b321c37935b9758aa03cc825ff3b2793cc14cc7380bbb797ac75', 'type': 0, 'pageNum': 1, 'pageSize': 10}, 'assert': {'eq': {'msg': '请求成功', 'code': 0}, 'not_null': ['id']}}]
token1 = 123


def change():
    aa = re.findall(r'\${token}', str(data))
    for i in aa:
        a = str(data).replace(i, str(read_ini_yaml_file['token']))
        return a


# print('////',data)
print(change())


[{'name': '正常用例', 'method': 'post', 'url': 'https://task.letfungo.com/api/task/show/adminMalfunctionList', 'param_type': 'FORM', 'data': {'token': '${token}', 'type': 0, 'pageNum': 1, 'pageSize': 10}, 'assert': {'contain': None, 'eq': {'msg': '请求成功', 'code': 0}, 'not_null': ['add_time', 'created_at', 'ebike_no']}}, {'name': '正常用例', 'method': 'post', 'url': 'https://task.letfungo.com/api/task/show/adminMalfunctionList', 'param_type': 'FORM', 'data': {'token': 'c10363237f8e01ed34db47667d049ccbb318554260eac3abf38dff359bb8b5e720a85f14a7d2b321c37935b9758aa03cc825ff3b2793cc14cc7380bbb797ac75', 'type': 0, 'pageNum': 1, 'pageSize': 10}, 'assert': {'eq': {'msg': '请求成功', 'code': 0}, 'not_null': ['id']}}]
[{'name': '正常用例', 'method': 'post', 'url': 'https://task.letfungo.com/api/task/show/adminMalfunctionList', 'param_type': 'FORM', 'data': {'token': '46e3a4a86b41e884e9ff7d7e39370b3bb318554260eac3abf38dff359bb8b5e78d98be5eecc893914360170b8d992f51c825ff3b2793cc14cc7380bbb797ac75', 'type': 0, 'pageNum': 1, 'pageSize': 10}, 'assert': {'contain': None, 'eq': {'msg': '请求成功', 'code': 0}, 'not_null': ['add_time', 'created_at', 'ebike_no']}}, {'name': '正常用例', 'method': 'post', 'url': 'https://task.letfungo.com/api/task/show/adminMalfunctionList', 'param_type': 'FORM', 'data': {'token': 'c10363237f8e01ed34db47667d049ccbb318554260eac3abf38dff359bb8b5e720a85f14a7d2b321c37935b9758aa03cc825ff3b2793cc14cc7380bbb797ac75', 'type': 0, 'pageNum': 1, 'pageSize': 10}, 'assert': {'eq': {'msg': '请求成功', 'code': 0}, 'not_null': ['id']}}]
