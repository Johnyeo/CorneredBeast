# coding:utf-8
import http.cookiejar
import ssl
from urllib import request, parse

# post方法
loginurl = "https://login.wdcloud.cc/ptyhzx-login/user/login/auth"
updatephone = "http://i.wdcloud.cc/ptyhzx-grzx/security/updateMobile"

class NewPhone(object):
    def __init__(self):
        pass
    # 登录并保存cookie
    def loginGetCookie(self,username,password):
        # 把要传的data从dict转成正式格式
        data = {"loginname": username, "loginpwd": password}
        data = parse.urlencode(data)
        data = data.encode('ascii')
        # https请求免证书
        ssl_context = ssl._create_unverified_context()
        # 定义请求体
        req = request.Request('https://login.wdcloud.cc/ptyhzx-login/user/login/auth',
                              method='POST',
                              data=data,
                              )
        # cookieJar是装cookies的
        self.userCookie = http.cookiejar.CookieJar()
        cookiejar_hdl = request.HTTPCookieProcessor(self.userCookie)
        # 用来处理https请求的
        https_hdl = request.HTTPSHandler(debuglevel=0, context=ssl_context, check_hostname=None)
        # 把多个handler传进opener
        opener = request.build_opener(cookiejar_hdl,https_hdl)
        # 把请求传进去
        response = opener.open(req)
        return response

    def updatePhone(self,newPhone):
        # 把要传的data从dict转成正式格式
        data = {"cellphone":newPhone,"validatecode":"109821","country_calling_code":"86"}
        data = parse.urlencode(data)
        data = data.encode("ascii")
        # 设置request
        req = request.Request(updatephone,data=data)
        # 使用cookie
        cookie_hdl = request.HTTPCookieProcessor(self.userCookie)
        opener = request.build_opener(cookie_hdl)
        response = opener.open(req)
        return response



