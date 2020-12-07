# 定义一个计算器类
import pytest
import yaml


class calculator:
    def add(self, a, b):
        return a + b

    def div(self, a, b):
        return a / b


with open('calculator.yaml', encoding='utf-8') as f:
    calcdata = yaml.safe_load(f)
    add_data = calcdata['datas']['add']
    add_ids = calcdata['datas']['add_ids']
    div_data = calcdata['datas']['div']
    div_ids = calcdata['datas']['div_ids']


class Test_calculator:

    def setup_class(self):
        # 使局部变量cale变成一个实例变量
        self.calc = calculator()
        print("开始计算")

    def teardown_class(self):
        print("计算结束")

    @pytest.mark.parametrize('a, b, c', add_data, ids=add_ids)
    def test_add(self, a, b, c):
        result = self.calc.add(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == c

    @pytest.mark.parametrize('a, b , c', div_data, ids=div_ids)
    def test_div(self, a, b, c):
        result = self.calc.div(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        if b == 0:
            print("除数不能为0")
            return
        assert result == c
