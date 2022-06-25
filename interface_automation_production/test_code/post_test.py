import time
import requests
import random
import pytest

from interface_automation_production.common.yaml_util import YamlUtil

url = 'http://3.chensanli.com:8080/api/bike/bikeSearch/nearBike'


def a():
    for i in range(10):
        data = {'lng': random.uniform(118.20, 120.37), 'lat': random.uniform(29.11, 30.34), 'limit': 10}
        response = requests.post(url=url, data=data)
        print(response.json(), '      ', len(response.json()['data']), '      ', data['lng'], data['lat'])
        time.sleep(0.5)
        print(response.cookies)


class est_asd:
    # class Test_asd:   yaml文件好像不能用这个方法就行调用函数

    @pytest.mark.parametrize('aaa', YamlUtil().read_testcase_yaml('woyaocese.yml'))
    def test_a(self, aaa):
        print(aaa)



a()