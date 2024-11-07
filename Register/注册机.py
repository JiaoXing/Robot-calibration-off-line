#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
from pyDes import *

class Register:
    def __init__(self):
        self.Des_Key = b"JIAOXING"  # Key 应确保为字节串
        self.Des_IV = b"\x15\x01*\x03\x15#\x02\x00"  # IV也应为字节串
        self.EncryptStr = des(self.Des_Key, CBC, self.Des_IV, pad=None, padmode=PAD_PKCS5)

    # DES+base64加密
    def encrypt_and_encode(self, key, timestamp):
        combined = self.EncryptStr.encrypt(key.encode('utf-8'))  # 先编码为字节串再加密
        combined= base64.b64encode(combined).decode('utf-8')
        combined = str(combined) + '|' + timestamp
        encrypted = self.EncryptStr.encrypt(combined.encode('utf-8'))  # 先编码为字节串再加密
        return  base64.b64encode(encrypted).decode('utf-8') # 返回Base64编码的字符串

    def regist(self):
        key = input('请输入机器特征码:')
        timestamp = input('请输入激活日期如2024-06-20:')
        content = self.encrypt_and_encode(key, timestamp)
        print('永久注册码：', content)

    def decrypt_and_decode(self, encoded_ciphertext):
        decoded_ciphertext = base64.b64decode(encoded_ciphertext)  # 先解码Base64
        decrypted = self.EncryptStr.decrypt(decoded_ciphertext).decode('utf-8')  # 解密后解码为字符串
        return decrypted

    def verify(self):
        key = input('请输入注册码:')
        licen = self.decrypt_and_decode(key)
        if licen:
            key, timestamp = licen.split("|")
            print("解密后：", licen)
            print(key, timestamp)
        else:
            print("注册码解密失败，请确认输入是否正确。")


reg = Register()
reg.regist()
reg.verify()
input()
