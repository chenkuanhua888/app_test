
import requests


if __name__ == '__main__':
    # 创建Session对象
    s = requests.Session()
    login_url = 'http://127.0.0.1:8000/login'
    # 通过Session对象调用方法提交请求
    ret = s.post(login_url, data={'username':'lizhichao', 'password':'abc123abc'})
    print(ret.status_code)
    print(ret.headers)

    ####################################################


    url = 'http://127.0.0.1:8000/student/search'

    ret = s.get(url, params={'name':'Jack'})
    print(ret.status_code)
    # 请求的headers
    print(ret.request.headers)
    print(ret.text)

    # 关闭会话
    s.close()