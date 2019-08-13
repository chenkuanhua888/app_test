

import unittest
import requests

class AddStudentApiTests(unittest.TestCase):
    """
    添加学生信息接口测试用例
    """

    url = 'http://127.0.0.1:8000/student/'
    def test1_name_success(self):
        """
        添加学生信息测试用例
        """
        resp = requests.post(url=self.url, data={'name':'roy'})
        self.assertEqual(200, resp.status_code, '状态码错误')

        data = resp.json()
        self.assertEqual(1, data['result'], 'result字段错误')
        self.assertEqual('add student success', data['msg'], 'msg字段错误')
        self.assertEqual('roy', data['student']['name'], 'student字段错误')

    def test2_name_age_success(self):
        """
        添加学生信息测试用例
        """
        resp = requests.post(url=self.url, data={'name':'roy1', 'age':22})
        self.assertEqual(200, resp.status_code, '状态码错误')

        data = resp.json()
        self.assertEqual(1, data['result'], 'result字段错误')
        self.assertEqual('add student success', data['msg'], 'msg字段错误')
        self.assertEqual('roy1', data['student']['name'], 'student字段错误')

    def test3_name_class_success(self):
        """
        添加学生信息测试用例
        """
        resp = requests.post(url=self.url, data={'name':'roy2', 'class':'D01'})
        self.assertEqual(200, resp.status_code, '状态码错误')

        data = resp.json()
        self.assertEqual(1, data['result'], 'result字段错误')
        self.assertEqual('add student success', data['msg'], 'msg字段错误')
        self.assertEqual('roy2', data['student']['name'], 'student字段错误')

    def test4_name_age_class_success(self):
        """
        添加学生信息测试用例
        """
        resp = requests.post(url=self.url, data={'name':'roy3', 'age':23 , 'class':'D01'})
        self.assertEqual(200, resp.status_code, '状态码错误')

        data = resp.json()
        self.assertEqual(1, data['result'], 'result字段错误')
        self.assertEqual('add student success', data['msg'], 'msg字段错误')
        self.assertEqual('roy3', data['student']['name'], 'student字段错误')

    def test5_age_class_fail(self):
        """
        添加学生信息测试用例
        """
        resp = requests.post(url=self.url, data={'age':23 , 'class':'D01'})
        self.assertEqual(200, resp.status_code, '状态码错误')

        data = resp.json()
        self.assertEqual(0, data['result'], 'result字段错误')
        self.assertEqual('add student failed', data['msg'], 'msg字段错误')
        self.assertEqual(None, data['student'], 'student字段错误')