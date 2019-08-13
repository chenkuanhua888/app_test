
# pip install ddt

import ddt  # (data driven test)


import unittest


def add(a, b):
    return a + b


class AddTests(unittest.TestCase):


    def test1(self):
        ret = add(3, 5)
        self.assertEqual(8, ret, '返回值错误')

    def test2(self):
        ret = add(-3, 5)
        self.assertEqual(2, ret, '返回值错误')

    def test3(self):
        ret = add(-3, -5)
        self.assertEqual(-8, ret, '返回值错误')