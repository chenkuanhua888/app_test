

# pip install requests
import requests


if __name__ == '__main__':
    # url = 'http://apis.juhe.cn/mobile/get?phone=15814616795&dtype=json'
    # url = 'http://apis.juhe.cn/mobile/get?key=sdfkdsfsdfsdf&dtype=json'
    url = 'http://apis.juhe.cn/mobile/get'
    params = {'key':'abcde', 'dtype':'json'}
    # 提交一个GET请求
    resp = requests.get(url=url, params=params)
    # 状态码
    print(resp.status_code)
    # 状态码说明
    print(resp.reason)
    # print(resp.url)
    # 响应的头部
    print(resp.headers)
    print(resp.headers['content-type'])
    # 响应的正文
    print( type(resp.text) )
    print(resp.text)

    # 把json格式的正文转换成python对象
    data = resp.json()
    print( type(data) )
    print( data )
    print( data['resultcode'] )