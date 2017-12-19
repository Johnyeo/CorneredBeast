# coding:utf-8
from corneredbeast.vincent import models
from corneredbeast.vincent.main.properties import *

'''
This script is used for initializing the data in database

name 具体名称，例如青岛生产环境
envroment 环境test还是prod
url 地址
flag 新建A，更新U，无效D
comment 属于哪个系统
category 是前台user还是后台admin
business 属于哪一个业务 toc tob 职教

'''


# 往地址表里插入数据
def insert_weidongurl(name, environment, url, flag, comment, category, business):
    models.weidongurls.objects.update_or_create(name=name, environment=environment, url=url, flag=flag, comment=comment,
                                                category=category, business=business)


def init_weidongurls():
    # 12学生产地址
    insert_weidongurl('青岛', 'prod', qingdao.url, 'A', qingdao.type, 'user', 'tob')
    insert_weidongurl('即墨', 'prod', jimo.url, 'A', jimo.type, 'user', 'tob')
    insert_weidongurl('崂山', 'prod', laoshan.url, 'A', laoshan.type, 'user', 'tob')
    insert_weidongurl('博山', 'prod', boshan.url, 'A', boshan.type, 'user', 'tob')
    insert_weidongurl('平度', 'prod', pingdu.url, 'A', pingdu.type, 'user', 'tob')
    insert_weidongurl('武侯', 'prod', wuhou.url, 'A', wuhou.type, 'user', 'tob')
    insert_weidongurl('韶山', 'prod', shaoshan.url, 'A', shaoshan.type, 'user', 'tob')
    insert_weidongurl('海南', 'prod', shaoshan.url, 'A', hainan.type, 'user', 'tob')
    insert_weidongurl('佳木斯', 'prod', shaoshan.url, 'A', jiamusi.type, 'user', 'tob')
    insert_weidongurl('鸡西', 'prod', shaoshan.url, 'A', jixi.type, 'user', 'tob')
    # 交易中心地址
    insert_weidongurl(jyzx_test.name, 'test', jyzx_test.url, 'A', jyzx_test.type, 'user', 'toc')
    insert_weidongurl(jyzx_test_admin.name, 'test', jyzx_test_admin.url, 'A', jyzx_test_admin.type, 'admin', 'toc')
    insert_weidongurl(jyzx_pro.name, 'prod', jyzx_pro.url, 'A', jyzx_pro.type, 'user', 'toc')
    insert_weidongurl(jyzx_pro_admin.name, 'prod', jyzx_pro_admin.url, 'A', jyzx_pro_admin.type, 'admin', 'toc')
    insert_weidongurl(jyzx_demo.name, 'demo', jyzx_demo.url, 'A', jyzx_demo.type, 'user', 'toc')
    insert_weidongurl(jyzx_demo_admin.name, 'demo', jyzx_demo_admin.url, 'A', jyzx_demo_admin.type, 'admin', 'toc')
    insert_weidongurl(jyzx_en.name, 'en', jyzx_en.url, 'A', jyzx_en.type, 'user', 'toc')
    insert_weidongurl(jyzx_en_admin.name, 'en', jyzx_en_admin.url, 'A', jyzx_en_admin.type, 'admin', 'toc')
    insert_weidongurl(jyzx_fr.name, 'fr', jyzx_fr.url, 'A', jyzx_fr.type, 'user', 'toc')
    insert_weidongurl(jyzx_fr_admin.name, 'fr', jyzx_fr_admin.url, 'A', jyzx_fr_admin.type, 'admin', 'toc')
    # 公共服务地址
    # 问卷调查
    insert_weidongurl(wjdt_test.name, 'test', wjdt_test.url, 'A', wjdt_test.type, 'admin', '')
    insert_weidongurl(wjdt_pro.name, 'prod', wjdt_pro.url, 'A', wjdt_pro.type, 'admin', '')
    # 个人中心
    insert_weidongurl(grzx_test.name, 'test', grzx_test.url, 'A', grzx_test.type, 'user', '')
    insert_weidongurl(grzx_pro.name, 'prod', grzx_pro.url, 'A', grzx_pro.type, 'user', '')
    # 国学
    insert_weidongurl(guoxue_test,'test',guoxue_test.url,'A',guoxue_test.type,'user','guoxue')
    insert_weidongurl(guoxueadmin_test,'test',guoxueadmin_test.url,'A',guoxueadmin_test.type,'admin','guoxue')
    insert_weidongurl(guoxue_prod,'prod',guoxue_prod.url,'A',guoxue_prod.type,'user','guoxue')
    insert_weidongurl(guoxueadmin_prod,'prod',guoxueadmin_prod.url,'A',guoxueadmin_prod.type,'admin','guoxue')
