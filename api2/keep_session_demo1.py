
import requests


if __name__ == '__main__':
    login_url = 'http://127.0.0.1:8000/login'
    ret = requests.post(login_url, data={'username':'lizhichao', 'password':'abc123abc'})
    print(ret.status_code)
    # 响应的headers
    print(ret.headers)
    # print(ret.headers['Set-Cookie'].split(';')[0])
    # print(ret.text)
    # 获取sessionid的值
    sid = ret.cookies['sessionid']
    print(sid)
    ####################################################


    url = 'http://127.0.0.1:8000/student/search'
    # headers 更新请求的header
    # ret = requests.get(url, params={'name':'Jack'}, headers={'Cookie':'sessionid=%s'%sid})

    # cookies 添加cookie
    ret = requests.get(url, params={'name':'Jack'}, cookies={'sessionid': sid})
    print(ret.status_code)
    # 请求的headers
    print(ret.request.headers)
    print(ret.text)