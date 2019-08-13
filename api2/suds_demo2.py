
# pip install suds-jurko
from suds.client import Client
from suds.xsd.doctor import Import, ImportDoctor

if __name__ == '__main__':
    # 典型异常的解决方法
    # suds.TypeNotFound: Type not found:
    url = 'http://www.webxml.com.cn/WebServices/ChinaZipSearchWebService.asmx?wsdl'
    imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')

    # 参数是WSDL文档根元素targetNamespace
    imp.filter.add('http://WebXml.com.cn/')
    d = ImportDoctor(imp)
    c = Client(url=url, doctor=d)
    print(c)
    print('-------------------------------------')
    port = c.service['ChinaZipSearchWebServiceSoap12']
    # ret = port.getSupportProvince()
    ret = port.getSupportCity('广东')
    print(ret)
