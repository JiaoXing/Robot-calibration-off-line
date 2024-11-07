"""
# @Project  :Python
# @File     :my_Sqlite3
# @Date     :2024/5/20 18:04
# @Author   :叫猩
# @Email    :1027918098@qq.com
# @Software :PyCharm
"""
# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime


class my_Sqlite3:
    def __init__(self):
        # 连接到SQLite数据库
        self.conn = sqlite3.connect('./my_database.db')
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        """创建表，只在首次运行时执行。"""
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS licence
                                 (id INTEGER PRIMARY KEY AUTOINCREMENT, key TEXT, timestamp TEXT)''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"创建表时出错：{e}")

    def write_data(self, id, key_hash, timestamp):
        """
        写入数据到数据库。
        :param id: 要写入的ID，应为正整数。
        """
        # 参数验证
        if not isinstance(id, int) or id <= 0:
            raise ValueError("ID必须是正整数。")
        if timestamp is None:
            # 当前时间戳
            timestamp = datetime.utcnow().date()

        # 使用参数化查询，防止SQL注入
        insert_query = "INSERT INTO licence (id, key, timestamp) VALUES (?, ?, ?)"
        update_query = "UPDATE licence SET key = ?, timestamp = ? WHERE id = ?"

        try:
            self.cursor.execute(insert_query, (id, key_hash, timestamp))  # 使用参数化防止SQL注入
            print("数据插入。")
        except sqlite3.IntegrityError:  # 如果出现唯一性冲突，执行更新操作
            self.cursor.execute(update_query, (key_hash, timestamp, id))
            print("数据更新。")
        self.conn.commit()

    def compare_keys_by_id(self, id1, id2):
        check_authored_result = 0  # 初始化返回值
        check_authored_ValueError = None  # 初始化返回值

        current_time = datetime.utcnow().date()
        try:
            # 使用参数化查询以防止SQL注入
            licence1 = self.cursor.execute("SELECT key,timestamp FROM licence WHERE id = ?", (id1,)).fetchone()
            if licence1 is not None:
                try:
                    licence2 = self.cursor.execute("SELECT key,timestamp FROM licence WHERE id = ?", (id2,)).fetchone()
                    if licence2 is not None:
                        # 优化日期转换，处理异常
                        try:
                            # 将timestamp1和timestamp2从Unix时间戳转换为datetime对象
                            date1 = datetime.strptime(licence1[1], "%Y-%m-%d").date()
                            date2 = datetime.strptime(licence2[1], "%Y-%m-%d").date()
                        except ValueError as e:
                            check_authored_result = -3  # 日期解析错误
                            check_authored_ValueError = f"日期格式错误: {e}"
                            return check_authored_result, check_authored_ValueError

                        if licence1[0] == licence2[0]:
                            # 修正时间比较逻辑，包含边界
                            if date1 <= current_time <= date2:
                                check_authored_result = 1
                                check_authored_ValueError = f"有效期:{date2}"
                            else:
                                check_authored_result = -2
                                check_authored_ValueError = f"秘钥过期!"
                        else:
                            check_authored_result = -1
                            check_authored_ValueError = f"密钥无效!"
                    else:
                        check_authored_result = -3  # 未找密钥
                        check_authored_ValueError = f"未找到注册文件!"
                except sqlite3.Error as e:
                    check_authored_result = -3  # 未找密钥
                    check_authored_ValueError = f"未找到注册文件!"
            else:
                check_authored_result = 0  # 未找到注册文件
                check_authored_ValueError = f"未找到特征码!"
        except Exception as e:
            check_authored_result = 0  # 未找到注册文件
            check_authored_ValueError = f"未找到特征码!"

        return check_authored_result, check_authored_ValueError