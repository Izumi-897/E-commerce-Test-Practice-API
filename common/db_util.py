import pymysql
from config import DB_CONFIG

class DBUtil:
    """
    数据库基础操作封装类
    支持基于 DictCursor 的结果集映射及基础事务控制
    """

    def __init__(self):
        """
        初始化数据库连接并获取字典型游标
        """
        try:
            self.conn = pymysql.connect(**DB_CONFIG)
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        except Exception as e:
            # 记录连接初始化异常并上抛
            print(f"\n[数据库连接失败] 请检查 config.py 里的配置信息。报错详情: {e}")
            raise e

    def query_one(self, sql):
        """
        执行查询语句并获取单行结果
        :param sql: str, SQL 查询语句
        :return: dict/None, 成功返回首行数据字典，无结果或异常返回 None
        """
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            print(f"SQL查询失败: {sql}, 错误: {e}")
            return None

    def execute(self, sql):
        """
        执行 DML 操作（Insert/Update/Delete）
        :param sql: str, 待执行的 SQL 语句
        :return: int, 受影响的记录行数，发生异常返回 0
        """
        try:
            # 执行语句并提交事务
            self.cursor.execute(sql)
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            # 捕获异常执行事务回滚
            self.conn.rollback()
            print(f"SQL执行失败: {sql}, 错误: {e}")
            return 0

    def close(self):
        """
        安全释放游标与数据库连接资源
        """
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'conn') and self.conn:
            self.conn.close()