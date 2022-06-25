import allure
import pytest
from interface_automation_production.common.judgeassert_util import Judgeassert
from interface_automation_production.common.yaml_util import YamlUtil
from interface_automation_production.common.requests_util import RequestsUtil


judge = Judgeassert()


@allure.feature('接口测试')
class Testcase_mobile_management:

    # 获取手机验证码
    # @pytest.mark.skip(reason='no')
    @allure.title('获取手机验证码')
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_testcase_yaml('test.yml'))
    def test_get_phone_verification_code(self, caseinfo):

        response = RequestsUtil().session.request(method=caseinfo['method'], url=caseinfo['url'], data=caseinfo['data'])
        result_code = response.status_code
        result = response.json()

        assert result_code == 200
        judge.all_assert(result, caseinfo)
