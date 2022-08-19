import pytest
import json
import requests
import re


class Judgeassert:

    def __init__(self):
        self.tmp = []
        self.key_list = []

    """
    1、json_result是response返回的json字符串，read_yaml_assert是读取到yaml里的断言字符串
    2、yaml文件里的判断格式必须严格按照要求写
    3、eq_assert断言返回值里第一层的内容
    4、contain_assert断言返回值内是否包含关键字
    5、notnull_assert断言返回值的某些key是否为空
    """

    def all_assert(self, json_result, read_yaml_assert):

        read_yaml_assert = read_yaml_assert['assert']

        if 'eq' in read_yaml_assert and read_yaml_assert['eq'] is not None:
            self.eq_assert(json_result, read_yaml_assert)
        if 'contain' in read_yaml_assert and read_yaml_assert['contain'] is not None:
            self.contain_assert(json_result, read_yaml_assert)
        if 'not_null' in read_yaml_assert and read_yaml_assert['not_null'] is not None:
            self.notnull_assert(json_result, read_yaml_assert)
        else:
            pass

    # 断言等于
    def eq_assert(self, json_result, read_yaml_assert):
        read_yaml_assert = read_yaml_assert['eq']
        result = self.ergodic_(json_result, [])
        for ii in read_yaml_assert:
            assert ii in result
        self.eq_qq(json_result, read_yaml_assert)

    # 断言包含
    def contain_assert(self, json_result, read_yaml_assert):
        if 'contain' in read_yaml_assert:
            assert re.search(str(read_yaml_assert['contain']), str(json_result))
        else:
            pass

    # 断言字段不为空
    def notnull_assert(self, json_result, read_yaml_assert):
        key_list = []
        if 'not_null' in read_yaml_assert:

            # 获取到断言里不为空的key的value
            get_value_list = self.ttt(json_result, read_yaml_assert)
            for i in get_value_list:
                if i is None:
                    assert False
                else:
                    assert True

            get_key_list = list(self.get_target_key(json_result, key_list))
            for j in read_yaml_assert['not_null']:
                # print(j)
                # print(get_key_list)
                assert j in get_key_list
        else:
            pass

    # 只作判断
    def ttt(self, json_result, read_yaml_assert):

        tmp = []

        key = read_yaml_assert['not_null']
        # key = read_yaml_assert

        if type(key) == str:
            self.get_target_value(key, json_result, tmp)
        elif type(key) == list:
            for i in key:
                self.get_target_value(i, json_result, tmp)
        # print('this is tmp', self.tmp)
        return tmp

    # 遍历value，返回传入的key对于的value
    def get_target_value(self, key, dic, tmp_list):
        """
        :param key: 目标key值
        :param dic: JSON数据
        :param tmp_list: 用于存储获取的数据
        :return: list
        """

        # if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
        #     return 'argv[1] not an dict or argv[-1] not an list '

        if key in dic.keys():
            tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
            for val in dic.values():
                if isinstance(val, dict):
                    self.get_target_value(key, val, tmp_list)  # 传入数据的value值是字典，则直接调用自身
                elif isinstance(val, (list, tuple)):
                    self.get_value(key, val, tmp_list)  # 传入数据的value值是列表或者元组，则调用get_value
        else:
            for value in dic.values():  # 传入数据不符合则对其value值进行遍历
                if isinstance(value, dict):
                    self.get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
                elif isinstance(value, (list, tuple)):
                    self.get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用get_value

        return tmp_list

    def get_value(self, key, val, tmp_list):
        for val_ in val:
            if isinstance(val_, dict):
                self.get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
            elif isinstance(val_, (list, tuple)):
                self.get_value(key, val_, tmp_list)

    # 默认传入的key_lists是空的, dic是response.json()
    def get_target_key(self, dic, key_lists):
        for i in dic.keys():
            key_lists.append(i)
            if isinstance(dic[i], dict):
                self.get_target_key(dic[i], key_lists)
            elif isinstance(dic[i], (list, tuple)):
                self.get_key(dic[i], key_lists)

            # for val in dic.values():
            #     if isinstance(val, dict):
            #         self.get_target_key(val, key_list)
            #     elif isinstance(val, (list, tuple)):
            #         self.get_key(val, key_list)

        return set(key_lists)

    def get_key(self, val, key_lists):
        for val_ in val:
            if isinstance(val_, dict):
                self.get_target_key(val_, key_lists)  # 传入数据的value值是字典，则调用get_target_value
            elif isinstance(val_, (list, tuple)):
                self.get_key(val_, key_lists)

    def eq_qq(self, json_result, read_yaml_assert):

        for i in read_yaml_assert:
            # print(i, read_yaml_assert[i])
            if i in json_result:
                # print('1*')
                assert json_result[i] == read_yaml_assert[i]
            else:
                for j in json_result.values():
                    if isinstance(j, dict):
                        self.eq_qq(j, read_yaml_assert)
                    elif isinstance(j, (list, tuple)):
                        self.list_tuple_loop(j, read_yaml_assert)

    def list_tuple_loop(self, json_result, read_yaml_assert):

        for val_ in json_result:
            if isinstance(val_, dict):
                self.eq_qq(val_, read_yaml_assert)
            elif isinstance(val_, (tuple, list)):
                self.list_tuple_loop(val_, read_yaml_assert)

    def ergodic_(self, dic, result):
        for i in dic:
            result.append(i)
            if isinstance(dic[i], dict):
                self.ergodic_(dic[i], result)
            elif isinstance(dic[i], (tuple, list)):
                self.ergodic_tuple_list(dic[i], result)
        return result

    def ergodic_tuple_list(self, dic, result):
        for val_ in dic:
            if isinstance(val_, dict):
                self.ergodic_(val_, result)
            elif isinstance(val_, (tuple, list)):
                self.ergodic_tuple_list(val_, result)


judge = Judgeassert()
json_result = {'msg': '获取成功', 'code': 0, 'data': {'taskId': '1539159199623262208', 'phonenumber': '15258830878',
                                                  'powerPhotoState': 1, 'isWorkOrder': 1, 'ebike_type': None, 'key': '', 'imei': '', 'ebike_id': '', 'ebike_no': ''}}
read_yaml_assert_eq = {'msg': '获取成功', 'code': 0, 'isWorkOrder': 1}

