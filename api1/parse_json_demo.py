


import json


if __name__ == '__main__':
    # print(json.__file__)
    f = open('data.json', 'r')

    ret = json.load(f)
    print( type(ret) )
    print(ret)

    f.close()