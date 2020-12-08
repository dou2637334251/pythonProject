# 定义一个计算器类
import allure
import pytest
import yaml


class calculator:
    def add(self, a, b):
        return a + b

    def div(self, a, b):
        return a / b

    def sub(self, a, b):
        return a - b

    def take(self, a, b):
        return a * b


# @allure.feature("测试计算器")
@allure.feature("测试技算器")
class Test_calculator:

    # def setup_class(self):
    #     # 使局部变量cale变成一个实例变量
    #     self.calc = calculator()
    #     print("开始计算")
    #
    # def teardown_class(self):
    #     print("计算结束")

    # @pytest.mark.parametrize('a, b, c', add_data, ids=add_ids)
    @allure.story("测试加法")
    @pytest.mark.run(order=1)
    def test_add(self, get_calc, get_add_datas):
        result = None
        try:
            with allure.step("计算俩个数的相加和"):
                result = get_calc.add(get_add_datas[0], get_add_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)
        assert result == get_add_datas[2]

    # @pytest.mark.parametrize('a, b , c', div_data, ids=div_ids)
    @allure.story("测试除法")
    @pytest.mark.run(order=4)
    def test_div(self, get_calc, get_div_datas):
        with allure.step("计算俩个数的相加除"):
            result = get_calc.div(get_div_datas[0], get_div_datas[1])
        if isinstance(result, float):
            result = round(result, 2)
        if get_div_datas[1] == 0:
            print("除数不能为0")
            return
        assert result == get_div_datas[2]

    @allure.story("测试减法")
    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, get_sub_data):
        with allure.step("计算俩个数的相加减"):
            result = get_calc.sub(get_sub_data[0], get_sub_data[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_sub_data[2]

    @allure.story("测试乘法")
    @pytest.mark.run(order=3)
    def test_take(self, get_calc, get_take_data):
        with allure.step("计算俩个数的相加乘"):
            result = get_calc.take(get_take_data[0], get_take_data[1])
        if isinstance(result, float):
            result = round(result, 2)
        assert result == get_take_data[2]
