import unittest
from unittest import TestCase


# coding:utf-8
from urllib import request

import simplejson


class TestNetworkInterface(TestCase):
    # 测试接口
    def test_getData(self):
        response = request.urlopen('http://localhost:8000/rtxspy/getData')
        ls = simplejson.loads(response.read())


class TestNet2(TestCase):
    def test_getErrorCode(self):
        response = request.urlopen('http://localhost:8000/rtxspy/getError')
        self.assertEqual(response.status, '200','status error')