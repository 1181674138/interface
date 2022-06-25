from interface_automation_production.common.yaml_util import YamlUtil
import pytest


def get_token():
    token = 'ef716fbbd2f79fb2188a0986924f86a5f0d321f7b668696a09d903fa1ea967b9467f36513ac4c491096ff7550d698a96'
    abc = 'asd123'
    YamlUtil().write_extract_yaml({"token": token})
    YamlUtil().write_extract_yaml({"abc": abc})


class Test_abc:

    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('switching_operators.yml'))
    def test_getname(self, caseinfo):
        print(type(YamlUtil().read_testcase_yaml('switching_operators.yml')))
        print(caseinfo)
        print(type(caseinfo))


if __name__ == '__main__':
    pytest.main()



# get_token()
# value = YamlUtil().read_extract_yaml('token')
# print(value)
# print(type(value))