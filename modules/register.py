# -*- coding: utf-8 -*-
"""
# @Project  :Python
# @File     :register
# @Date     :2024/5/16 16:08
# @Author   :叫猩
# @Email    :1027918098@qq.com
# @Software :PyCharm
"""

# 加密
from base64 import b64encode, b64decode
from pyDes import des, CBC, PAD_PKCS5
from wmi import WMI
from modules.my_Sqlite3 import my_Sqlite3


class Register:
    def __init__(self):
        self.Des_Key = b"JIAOXING"  # Key 应确保为字节串
        self.Des_IV = b"\x15\x01*\x03\x15#\x02\x00"  # IV也应为字节串
        self.EncryptStr = des(self.Des_Key, CBC, self.Des_IV, pad=None, padmode=PAD_PKCS5)

    def get_cpu_id(self):  # CPU序列号，唯一且无法修改
        self.ID = WMI()
        ID_list = []
        for cpu in self.ID.Win32_Processor():
            ID_list.append(cpu.ProcessorId.strip())
        return ID_list[0]

    #  由于机器码太长，故选取机器码字符串部分字符
    def getCombinNumber(self):
        matcher = my_Sqlite3()
        get_cpu_id = self.get_cpu_id()
        machinecode = self.encrypt_and_encode(self.get_cpu_id())
        print(machinecode)
        matcher.write_data(1, machinecode, None)  # 使用函数进行数据写入
        matcher.conn.close()  # 显示关闭数据库连接
        return get_cpu_id

    # DES+base64加密
    def encrypt_and_encode(self, key_str):
        EncryptStr = self.EncryptStr.encrypt(key_str)
        return b64encode(EncryptStr).decode('utf-8')  # 转base64编码返回

    # DES+base64解密
    def decrypt_and_decode(self, encoded_ciphertext):
        decoded_ciphertext = b64decode(encoded_ciphertext)  # 先解码Base64
        decrypted = self.EncryptStr.decrypt(decoded_ciphertext).decode('utf-8')  # 解密后解码为字符串
        print(decrypted)
        key, timestamp = decrypted.split("|")
        return key, timestamp

    def regist(self, key):
        matcher = my_Sqlite3()
        key, timestamp = self.decrypt_and_decode(key)
        matcher.write_data(2, key, timestamp)  # 使用函数进行数据写入
        matcher.conn.close()  # 显示关闭数据库连接

    # 打开程序先调用注册文件，比较注册文件中注册码与此时获取的硬件信息编码后是否一致
    def checkAuthored(self):
        matcher = my_Sqlite3()
        # 比较写入的两条数据
        checkAuthoredResult = matcher.compare_keys_by_id(1, 2)
        matcher.conn.close()
        return checkAuthoredResult
