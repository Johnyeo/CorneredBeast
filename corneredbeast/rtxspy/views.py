import simplejson
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# 首页
def rtxspy(request):
    return render(request, 'rtxspy/rtxspy.html')

# 设置图表y轴的值
def getData(request):
    # requestdata = request.read()
    # requestdata = simplejson.loads(requestdata)
    responsedata = [2,2,3,4,5,2]
    responsedata_json = simplejson.dumps(responsedata)
    return HttpResponse(responsedata_json)

def getError(request):
    # requestdata = request.read()
    # requestdata = simplejson.loads(requestdata)
    return HttpResponse(status=201)