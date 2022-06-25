import random
import allure
import pytest
import yaml
from interface_automation_production.common.requests_util import RequestsUtil
from interface_automation_production.common.yaml_util import YamlUtil


@pytest.fixture(scope='function')
def conn_database():
    print('xxx')


@pytest.fixture(scope='session', autouse=True)
def aaaa():
    pass


@pytest.fixture(scope='function')
def xxx():
    pass


