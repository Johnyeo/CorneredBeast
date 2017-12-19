# coding:utf-8

from django.conf.urls import url
from django.contrib import admin

from corneredbeast.vincent import views

urlpatterns = [
    # url(r'^dont_do_it_unless_u_know_what_it_is/init_db$',views.init_db),#初始化db
    url(r'^admin/', admin.site.urls), # vincent下的admin
    url(r'^rtxspy$', views.rtxspy),
    url(r'^getData/',views.getData),
    url(r'^getError/',views.getError),
    url(r'^hive$',views.getHive), #获取首页
    url(r'^newPhone$',views.updatePhone), #更新手机号
    url(r'^testUrls$',views.getTestUrls), #链接列表
    url(r'^prodUrls$',views.getProdUrls), #链接列表



]