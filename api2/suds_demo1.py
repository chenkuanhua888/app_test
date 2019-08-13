
# pip install suds-jurko
from suds.client import Client


if __name__ == '__main__':
    # WSDL文档的路径
    url = 'http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl'
    # 创建客户端对象
    c = Client(url=url)
    print(c)
    print('-------------------------------------')
    port = c.service['IpAddressSearchWebServiceSoap12']
    # 通过port对象调用方法
    ret = port.getCountryCityByIp('8.8.8.8')
    # ret = port.getCountryCityByIp('114.114.114.114')
    # ret = port.getCountryCityByIp('119.122.112.230')
    print(type(ret[0]))
    print(ret[0][1])