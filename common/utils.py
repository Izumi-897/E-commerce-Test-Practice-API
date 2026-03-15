import json
import os
from config import BASE_DIR
import time
import random

def generate_mobile():
    """
    生成基于时间戳的随机手机号
    用于规避自动化测试中注册接口的唯一性校验冲突
    :return: str, 11位随机手机号
    """
    return "138" + str(int(time.time() * 1000))[-8:]

def read_json_data(file_name):
    """
    从项目 data 目录加载并解析 JSON 格式测试用例数据
    :param file_name: str, 目标数据文件名（需包含后缀）
    :return: dict/list, 解析后的 Python 对象
    """
    file_path = os.path.join(BASE_DIR, "data", file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)