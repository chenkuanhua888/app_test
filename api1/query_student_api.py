


import unittest
import requests


class QueryStudentApiTests(unittest.TestCase):
    """
    查询学生信息接口测试用例
    """
    url = 'http://127.0.0.1:8000/student/tom/'
    def test1_success(self):
        """
        查询学生信息成功
        :return:
        """
        name = 'tom'
        url = self.url + name
        resp = requests.get(url)
        self.assertEqual(200, resp.status_code)
        data = resp.json()
        # print(data)
        self.assertEqual(1, data['result'], msg='result字段错误')
        self.assertEqual('success', data['msg'], msg='msg字段错误')
        self.assertEqual({'age': 19, 'class': 'A01', 'name': 'tom'}, data['student'], msg='student字段错误')

    def test2_failed(self):
        """
        查询学生信息失败
        :return:
        """
        name = 'roy'
        url = self.url + name
        resp = requests.get(url)
        self.assertEqual(200, resp.status_code)
        data = resp.json()
        # print(data)
        self.assertEqual(0, data['result'], msg='result字段错误')
        self.assertEqual('failed', data['msg'], msg='msg字段错误')
        self.assertEqual(None, data['student'], msg='student字段错误')