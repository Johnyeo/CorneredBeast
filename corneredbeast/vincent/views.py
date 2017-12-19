import simplejson
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
# 首页
from django.utils.timezone import pytz

from corneredbeast.vincent.main import hiveToolkit
from corneredbeast.vincent.main.hiveToolkit import NewPhone
from corneredbeast.vincent.main.init_db import init_weidongurls


# ------------------------初始化方法开始------------------------#
# 初始化数据库
from corneredbeast.vincent.models import weidongurls

localtimezone = pytz.timezone('Asia/Shanghai')

def init_db(request):
    init_weidongurls()
    return HttpResponse("init_db has run")


# ------------------------初始化方法结束------------------------#

# ------------------------rtxspy开始------------------------#
def rtxspy(request):
    return render(request, 'vincent/rtxspy.html')


# 设置图表y轴的值
def getData(request):
    # requestdata = request.read()
    # requestdata = simplejson.loads(requestdata)
    responsedata = [2, 2, 3, 4, 5, 2]
    responsedata_json = simplejson.dumps(responsedata)
    return HttpResponse(responsedata_json)


def getError(request):
    # requestdata = request.read()
    # requestdata = simplejson.loads(requestdata)
    return HttpResponse(status=201)


# ------------------------rtxspy结束------------------------#

# ------------------------蜂巢页开始------------------------#
# 蜂巢页
def getHive(request):
    return render(request, 'vincent/hive.html')


# todo 通过替换，释放账号绑定的手机号或者邮箱的功能
# 修改绑定的手机号
def updatePhone(request):
    # todo
    # 1. 登录获取cookie等
    # 2. 发送修改绑定手机号的请求
    np = NewPhone()
    response_lc = np.loginGetCookie()
    # 登录是否成功
    response_lc_dict = simplejson.loads(response_lc.read())
    login_success = response_lc_dict['isSuccess']
    # 登录成功接着发改号码的请求
    if login_success:
        response_up = np.updatePhone()
        response_up_dict = simplejson.loads(response_up.read())
        response = response_up
    else:
        response = response_lc

    return HttpResponse(response)


# 获取测试地址列表
def getTestUrls(request):
    all_data = weidongurls.objects.filter(environment="test")
    result = []
    for data in all_data:
    # taget_model = [{name:"青岛",url:"www.baidu.com"}, {xxxxx}, {xxxx}]
        # 格式化时间
        time = data.create_time.astimezone(localtimezone()).strftime("%Y-%m-%d %H:%M:%S")
        # 构造json对象
        result.append({"name":data.name,"addr":data.url,"update":time})
    return JsonResponse({"theUrls":result})

# 获取生产地址列表
def getProdUrls(request):
    all_data = weidongurls.objects.filter(~Q(environment="test"))
    result = []
    for data in all_data:
    # taget_model = [{name:"青岛",url:"www.baidu.com"}, {xxxxx}, {xxxx}]
        # 格式化时间
        time = data.create_time.astimezone(localtimezone()).strftime("%Y-%m-%d %H:%M:%S")
        # 构造json对象
        result.append({"name":data.name,"addr":data.url,"update":time})
    return JsonResponse({"theUrls":result})



# ------------------------蜂巢页结束------------------------#
