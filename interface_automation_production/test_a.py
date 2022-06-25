import pytest
import allure


@allure.feature('一次尝试')
class Test_as:

    @allure.story('这是story')
    @allure.title('这是title')
    def test_ababa(self):
        url = ''
        if not url.startswith(''):
            pass
        assert 1 == 1

    @allure.story('这是story')
    def test_ababasssd(self):
        assert 1 == 1

    @allure.story('这是story——————————————————————')
    @allure.title('这是title')
    def test_ababaasd12(self):
        url = ''
        if not url.startswith(''):
            pass
        assert 1 == 1

    @allure.story('这是story——————')
    def test_ababasssd123(self):
        assert 1 == 1

@allure.feature('第二次')
class Test_asd:

    @allure.id('这是id')
    def test_ababaasd(self):
        url = ''
        if not url.startswith(''):
            pass
        assert 1 == 1

    def test_ababasssdads(self):
        assert 1 == 1

