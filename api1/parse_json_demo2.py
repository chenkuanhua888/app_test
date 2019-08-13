

import json

if __name__ == '__main__':
    d = {'name': 'jack', 'age': 22}
    # 把python对象转换成json格式字符串
    ret = json.dumps(d)
    print(type(ret))
    print(ret)