# pip install ddt

import ddt  # (data driven test)
import unittest

def add(a, b):
    return a + b


class AddTests(unittest.TestCase):

    def foo(self, m, n, r):
        ret = add(m, n)
        self.assertEqual(r, ret, '返回值错误')

    def test1(self):
        self.foo(3, 5, 8)

    def test2(self):
        self.foo(-3, 5, 2)

    def test3(self):
        self.foo(-3, -5, -8)