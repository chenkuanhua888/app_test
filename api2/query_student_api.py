

import ddt
import unittest
import requests

@ddt.ddt
class QueryStudentApiTests(unittest.TestCase):
    """
    查询学生信息接口测试用例
    """
    url = 'http://127.0.0.1:8000/student/'

    @ddt.file_data('query_student_api_tc.json')
    @ddt.unpack
    def test1(self, name, expected_result, expected_msg, expected_student):
        """
        查询学生信息成功
        :return:
        """

        url = self.url + name
        resp = requests.get(url)
        self.assertEqual(200, resp.status_code)
        data = resp.json()
        # print(data)
        self.assertEqual(expected_result, data['result'], msg='result字段错误')
        self.assertEqual(expected_msg, data['msg'], msg='msg字段错误')
        self.assertEqual(expected_student, data['student'], msg='student字段错误')

