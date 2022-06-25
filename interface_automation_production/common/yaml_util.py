import os
import yaml
import re
import ast
import json


class YamlUtil:

    # 读取extract.yml的yaml文件
    def read_extract_yaml(self, yaml_name):
        with open(os.getcwd() + "interface_automation_production/testcase/" + yaml_name,
                  mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            # return value[key]
            return value

    # 写入extract.yml的yaml文件
    def write_extract_yaml(self, data):
        with open(os.getcwd() + "/token.yml", mode='a', encoding='utf-8') as f:
            value = yaml.dump(data=data, stream=f, allow_unicode=True)
            return value

    # 清除extract.yml的yaml文件
    def clean_extract_yaml(self):
        with open(os.getcwd() + "/token.yml", mode='w', encoding='utf-8') as f:
            f.truncate()

    # 读取case用例yaml文件
    def read_testcase_yaml(self, yaml_name):
        with open(os.getcwd() + "interface_automation_production/testcase" + yaml_name,
                  mode='r',
                  encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            # value = f.read()
        return value

    def change_token(self, data):

        # 从读取到的文件查询出token
        aa = re.findall(r'\${token}', str(data))
        for i in aa:
            a = str(data).replace(i, str(self.read_ini_yaml()['token']))
            return a

    def read_ini_yaml(self):
        with open(os.getcwd() + "interface_automation_production/ini.yml", mode='r', encoding='utf-8') as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
        return value

    # 是依靠于readlines进行替换，暂时不用
    def replace_value(self, file_so):
        final_list = []

        for line in file_so:
            new_line = line
            if new_line.find('${') > 0:
                env_list = new_line.split(':')
                env_name = env_list[1].strip().split('{', 1)[1].split('}')[0]

                replacement = ""
                if env_name in self.read_ini_yaml().keys():
                    replacement = self.read_ini_yaml()[env_name]
                    new_line = new_line.replace(env_list[1].strip(), str(replacement))

            final_list.append(new_line)
        return final_list

    def read_lines(self):
        with open(os.path.dirname(os.getcwd()) + r'/testcase/adminMalfunctionList.yml', mode='r', encoding='utf-8') as f:
            value = f.readlines()
            return value
