
import requests

if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/student/'
    # 提交一个POST请求
    resp = requests.post(url, data={'name':'roy', 'age':20, 'class':'C99'})
    print(resp.status_code)
    print(resp.text)