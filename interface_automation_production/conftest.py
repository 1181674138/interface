
import pytest


@pytest.fixture(scope='function')
def conn_database():
    print('xxx')


@pytest.fixture(scope='session', autouse=True)
def aaaa():
    pass


@pytest.fixture(scope='function')
def xxx():
    pass


