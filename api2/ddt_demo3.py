
# pip install ddt
import ddt  # (data driven test)
import unittest


def add(a, b):
    return a + b


@ddt.ddt
class AddTests(unittest.TestCase):

    # @ddt.data([3, 5, 8], [-3, 5, 2], [-3, -5, -8])
    # 支持json和yaml
    @ddt.file_data('add_student_tc.json')
    @ddt.unpack
    def test1(self, m, n, r):
        print('m = %d, n = %d, r = %d'%(m, n, r))
        ret = add(m, n)
        self.assertEqual(r, ret, '返回值错误')

