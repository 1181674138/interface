
from git_open.interface_automation_production.common.requests_util import RequestsUtil
import jsonpath


class Rel:

    # 前置接口
    """
        caseinfo: 用例
        hope: 期望值的jsonpath
    """
    def front_call(self, case_info, hope):
        pam = case_info['front']
        response = RequestsUtil().send_requests(method=pam['method'],
                                                data=pam['data'],
                                                url=pam['url'],
                                                param_type=pam['param_type'],
                                                )
        result = response.json()
        return jsonpath.jsonpath(result, hope)

    # 后置接口
    def real_call(self, case_info):
        pam = case_info['rear']
        response = RequestsUtil().send_requests(method=pam['method'],
                                                data=pam['data'],
                                                url=pam['url'],
                                                param_type=pam['param_type'],
                                                )


