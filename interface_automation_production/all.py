import pytest
import os
import shutil
import time
import pytest_ordering
import xdist
import pytest_rerunfailures


if __name__ == '__main__':

    shutil.rmtree(os.getcwd() + r'/temp')
    time.sleep(0.5)
    os.mkdir(os.getcwd() + r'/temp')
    time.sleep(0.5)

    # pytest.main(['-vs'])
    # pytest.main(['-vs', "./test_production.py"])
    pytest.main(['-vs', "./test_a.py"])

    time.sleep(1)
    os.system("allure generate ./temp -o ./reports --clean")

    with open(os.getcwd() + '/environment.yml', mode='r', encoding='utf-8') as f:
        txt = f.read()
    with open(os.getcwd() + '/reports/widgets/environment.json', mode='w', encoding='utf-8') as f:
        f.write(txt)

