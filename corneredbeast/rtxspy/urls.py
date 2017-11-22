# coding:utf-8

from django.conf.urls import url

from corneredbeast.rtxspy import views

urlpatterns = [
    url(r'^rtxspy$', views.rtxspy),
    url(r'^getData/',views.getData),
    url(r'^getError/',views.getError)
]