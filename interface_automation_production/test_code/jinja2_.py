import json

import jinja2
import yaml
from string import Template

a = {'token': '46e3a4a86b41e884e9ff7d7e39370b3bb318554260eac3abf38dff359b3cc14cc7380bbb797ac75'}
new_data = {"parent_id": "被替换的成功的数据-1"}


def read_ini_yaml():
    with open(r"C:/Users/DELL/PycharmProjects/selenium_test/interface_automation_production/ini.yml", mode='r',
              encoding='utf-8') as f:
        value = yaml.load(f, Loader=yaml.FullLoader)

        data = Template(str(value))
        data = data.safe_substitute(token='sad')
        # value = f.read()
        # resp = jinja2.Template(value).render(new_data)
    return data


# 读取extract.yml的yaml文件
def read_extract_yaml():
    with open(r"C:/Users/DELL/PycharmProjects/selenium_test/interface_automation_production/testcase/adminMalfunctionList.yml",
              mode='r', encoding='utf-8') as f:
        # value = yaml.load(stream=f, Loader=yaml.FullLoader)
        # resp = jinja2.Template(value).render(new_data)
        # return value[key]
        value2 = f.read()
        print(value2, type(value2))
        # return value


print(read_ini_yaml())
# read_extract_yaml()
# print(read_extract_yaml())
