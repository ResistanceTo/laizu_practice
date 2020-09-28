#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File               :abd_class.py
@Instructions       :
@Date               :2020/09/28 15:06:27
@Author             :LaiZu
@Version            :
@Desc               :
'''

import os, sys
base_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)

from abc import ABC, abstractclassmethod


class F1(ABC):
    @abstractclassmethod
    def func1(self):
        ''


class F2(F1):
    pass


class F3(F1):
    def func1(self):
        print('asdasd')


if __name__ == "__main__":
    # fa = F2()
    fa2 = F3()
