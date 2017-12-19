# coding:utf-8


from urllib import request

import simplejson

# 测试接口
class TestNetworkInterface(object):
    def test1_getData(self):
        response = request.urlopen('http://localhost:8000/vincent/getData')
        ls = simplejson.loads(response.read())

    def test2_getErrorCode(self):
        response = request.urlopen('http://localhost:8000/vincent/getError')
        assert response.status == 201
