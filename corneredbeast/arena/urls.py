# coding:utf-8
from django.conf.urls import url

from corneredbeast.arena import views

urlpatterns = [
    url(r'^index', views.index),

]
