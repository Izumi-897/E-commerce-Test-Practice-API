import os

# 项目根目录
BASE_DIR = os.path.dirname(__file__)

# 被测服务器地址
BASE_URL = "http://127.0.0.1:8080/wx"

DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "litemall",
    "charset": "utf8mb4"
}