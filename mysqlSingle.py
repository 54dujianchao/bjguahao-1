import sys
import pymysql
from functools import wraps
from pymysql import connect

try:
    import yaml
except ModuleNotFoundError as e:
    sys.exit(-1)

def singleton(cls):
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return get_instance

@singleton
class mysqlSingle(object):
    def __init__(self, conn='', cursor=''):
        self.conn = conn
        self.cursor = cursor

    def get_conn(self, config_path = 'mysql.yaml'):
        try:
            # 创建connection对象
            with open(config_path, "r", encoding="utf-8") as yaml_file:
                data = yaml.load(yaml_file, Loader=yaml.FullLoader)
                host = data["host"]
                password = data["password"]
                user = data["user"]
                port = data["port"]
                database = data["database"]
            self.conn = connect(host=host, port=port, user=user, password=password, database=database,charset='utf8')
            # 获取cursor对象
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

        except Exception as e:
            print('File to connect database: %s' % e)
        return self.conn, self.cursor


    def __del__(self):
        pass
        # 关闭游标对象
        # self.cursor.close()
        # 关闭连接对象
        # self.conn.close()

    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def execute_sql_one(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def find_goods_brands(self):
        sql = "select name from goods_brands;"
        self.execute_sql(sql)
