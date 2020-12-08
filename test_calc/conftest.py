from typing import List

import pytest
import yaml
import os

from test_calculator import calculator


@pytest.fixture()
def get_calc():
    calc = calculator()
    print("开始计算")
    yield calc
    print("结束计算")


# 需要获取yaml文件的绝对路劲
yaml_file_path = os.path.dirname(__file__) + '/calculator.yaml'
with open(yaml_file_path, encoding='utf-8') as f:
    calcdata = yaml.safe_load(f)
    add_data = calcdata['datas']['add_data']
    add_ids = calcdata['datas']['add_ids']
    div_data = calcdata['datas']['div_data']
    div_ids = calcdata['datas']['div_ids']
    sub_data = calcdata['datas']['sub_data']
    sub_ids = calcdata['datas']['sub_ids']
    take_data = calcdata['datas']['take_data']
    take_ids = calcdata['datas']['take_ids']


@pytest.fixture(params=add_data, ids=add_ids)
def get_add_datas(request):
    data = request.param
    yield data


@pytest.fixture(params=div_data, ids=div_ids)
def get_div_datas(request):
    data = request.param
    yield data


@pytest.fixture(params=sub_data, ids=sub_ids)
def get_sub_data(request):
    data = request.param
    yield data


@pytest.fixture(params=take_data, ids=take_ids)
def get_take_data(request):
    data = request.param
    yield data


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    """Called after collection has been performed. May filter or re-order
    the items in-place.

    :param pytest.Session session: The pytest session object.
    :param _pytest.config.Config config: The pytest config object.
    :param List[pytest.Item] items: List of item objects.
    """

    # 在钩子函数中修改编码格式
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode-escape')
