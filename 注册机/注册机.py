#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/20 12:21
# @Author : 叫兽
# @Site:
# @File : 注册机.py
# @Software: PyCharm

import base64

from pyDes import *


class register:
    def __init__(self):
        self.Des_Key = "JIAOXING"  # Key
        self.Des_IV = "\x15\1\x2a\3\1\x23\2\0"  # 自定IV向量

    # DES+base64加密
    def Encrypted(self, tr):
        k = des(self.Des_Key, CBC, self.Des_IV, pad=None, padmode=PAD_PKCS5)
        EncryptStr = k.encrypt(tr)
        return base64.b64encode(EncryptStr)  # 转base64编码返回

    def regist(self):
        key = input('请输入机器注册码： ')
        tent = bytes(key[0:32], encoding='utf-8')
        content = str(self.Encrypted(tent), encoding=('utf-8'))
        print('永久注册码：', content)
        tent = bytes(key[32:], encoding='utf-8')
        content_sy = "sy" + str(self.Encrypted(tent), encoding=('utf-8'))
        print('试用注册码：',content_sy)

reg = register()
reg.regist()
input()
