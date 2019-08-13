


import unittest
import requests

class APITest(unittest.TestCase):



    def test1(self):
        """
        接口测试用例
        :return:
        """
        url = 'http://apis.juhe.cn/mobile/get'
        resp = requests.get(url=url, params={'key':'abcde', 'dtype':'json'})
        self.assertEqual(200, resp.status_code)

        data = resp.json()
        self.assertEqual('101', data['resultcode'])
        self.assertEqual('错误的请求KEY', data['reason'])
        self.assertEqual(10001, data['error_code'])