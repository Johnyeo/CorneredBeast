# coding:utf-8

def getTestAddress():
    return 0


# coding:utf-8
'''
12学各个地区的地址，均为生产环境。包含地址、常用的用户。

例1：
qingdao.url --- > 青岛地区的登录地址
qingdao.user --- > 一个默认的用户名
qingdao.pwd --- > 该用户的密码

如果存了多个用户，可以变量名加数字。最多到3。
例2：
qingdao.user3 -- 用户名
qingdao.pwd3 -- 密码

如果很多用户，可以调用name_ls。例如下面调用第8个用户的用户名，密码。
例3：
qingdao.name_ls[5]['name']
qingdao.name_ls[5]['pwd']

'''


# 地区
class Env(object):
    def __init__(self, url, user_ls, name, type):
        self.url = url
        self.user_ls = user_ls
        self.name = name
        self.type = type
        try:
            self.user = user_ls[0]['name']
            self.pwd = user_ls[0]['pwd']
            self.user1 = user_ls[1]['name']
            self.pwd1 = user_ls[1]['pwd']
            self.user2 = user_ls[2]['name']
            self.pwd2 = user_ls[2]['pwd']
            self.user3 = user_ls[2]['name']
            self.pwd3 = user_ls[2]['pwd']
        except IndexError as e:
            pass


# 青岛
qingdao = Env('https://www.qdeduyun.cn/ptzyzx-zzfw/app/jsp/main/login.html',
              [
                  {'name': 'jmt01', 'pwd': '111111'},
                  {'name': '2000249690', 'pwd': '111111'},
              ],
              '青岛',
              '青岛'
              )
# 即墨
jimo = Env('https://jimo.qdeduyun.cn/ptzyzx-zzfw/app/jsp/main/login.html',
           [
               {'name': 'jmt01', 'pwd': '111111'}
           ],
           '即墨', '青岛'

           )
# 平度
pingdu = Env('https://jimo.qdeduyun.cn/ptzyzx-zzfw/app/jsp/main/login.html',
             [
                 {'name': '2001952207', 'pwd': '111111'}
             ],
             '平度', '青岛'
             )
# 武侯
wuhou = Env('https://whjyy.wdcloud.cc',
            [
                {'name': 'wht01', 'pwd': '111111'}
            ],
            '武侯', '武侯'
            )
# 佳木斯
jiamusi = Env('https://jmsedu.wdcloud.cc',
              [
                  {'name': '2002047252', 'pwd': '111111'}
              ],
              '佳木斯', '武侯'
              )
# 韶山
shaoshan = Env('https://ssjyy.wdcloud.cc/',
               [
                   {'name': '2002048627', 'pwd': '111111'}
               ],
               '韶山', '武侯'
               )
# 博山
boshan = Env('https://bs.wdcloud.cc',
             [
                 {'name': '2002169724', 'pwd': '111111'}
             ],
             '博山', '武侯'
             )
# 崂山
laoshan = Env('http://lsjky.laoshanedu.com',
              [
                  {'name': '2001909216', 'pwd': '111111'}
              ],
              '崂山', '武侯'
              )
# 鸡西
jixi = Env('https://www.12study.cn/ptzyzx-zzfw/app/jsp/main/login.html',
           [
               {'name': 'yinn', 'pwd': '111111'}
           ],
           '鸡西', '青岛'
           )
# 海南
hainan = Env('https://tobres.wdcloud.cc/ptzyzx-zzfw/app/jsp/main/login.html',
             [
                 {'name': '2001909470', 'pwd': '111111'}
             ],
             '海南', '青岛'
             )

# # # # # # # # # # 交易中心登录地址 # # # # # # # # # #
# 交易中心测试
jyzx_test = Env('https://yflogin.vviton.com/ptyhzx-login/app/jsp/main/login.html',
                [
                    {'name': '2000245048', 'pwd': '111111'},
                ],
                '交易中心测试', '唯通网'
                )
# 测试后台
jyzx_test_admin = Env('https://yfalogin.wdcloud.cc/admin-login/app/jsp/main/login.html',
                      [
                          {'name': 'zhangzhijian', 'pwd': '111111'},
                      ],
                      '测试后台', '唯通网'
                      )
# 交易中心生产
jyzx_pro = Env('https://login.wdcloud.cc/ptyhzx-login/app/jsp/main/login.html',
               [
                   {'name': 'lxcs1', 'pwd': '111111'},
               ],
               '交易中心生产', '唯通网'
               )
# 生产后台
jyzx_pro_admin = Env('https://alogin.wdcloud.cc/admin-login/app/jsp/main/login.html',
                     [
                         {'name': 'jyzxadmin', 'pwd': 'Wd_Wzl_0568'},
                         {'name': 'jyzxdev', 'pwd': 'dev_admin'},
                     ],
                     '生产后台', '唯通网'
                     )
# 交易中心国际版
jyzx_en = Env('https://enlogin.vviton.com/ptyhzx-login/app/jsp/main/login.html',
              [
                  {'name': 'vincent', 'pwd': '111111'},
              ],
              '交易中心国际版', '唯通网'
              )
# 国际版后台
jyzx_en_admin = Env('https://enalogin.vviton.com/admin-login/app/jsp/main/login.html',
                    [
                        {'name': 'zhangzhijian', 'pwd': '111111'},
                    ],
                    '国际版后台', '唯通网'
                    )
# 交易中心演示
jyzx_demo = Env('https://wdlogin.wdcloud.cc/ptyhzx-login/app/jsp/main/login.html',
                [
                    {'name': 'biyue', 'pwd': '111111'},
                ],
                '交易中心演示', '唯通网'
                )
# 演示后台
jyzx_demo_admin = Env('https://wdalogin.wdcloud.cc/admin-login/app/jsp/main/login.html',
                      [
                          {'name': 'zhangzhijian', 'pwd': '111111'},
                      ],
                      '演示后台', '唯通网'
                      )
# 交易中心法国 -- 无法访问，这个是首页地址
jyzx_fr = Env('http://entc.learningischanging.com/',
              [
                  {'name': 'vincent', 'pwd': '111111'},
              ],
              '交易中心法国', '唯通网'
              )
# 法国后台 -- 无法访问，这个是首页地址
jyzx_fr_admin = Env('https://enalogin.learningischanging.com/admin-login/app/jsp/main/index.html',
                    [
                        {'name': 'zhangzhijian', 'pwd': '111111'},
                    ],
                    '法国后台', '唯通网'
                    )

# # # # # # # # # # 问卷调查登录地址 # # # # # # # # # #
# 问卷调查生产 -- 管理员账号找张琦要
wjdt_pro = Env(
    'https://login.wdcloud.cc/ptyhzx-login/app/jsp/main/login.html',
    [
        {'name': 'vincent', 'pwd': '111111'},
    ],
    '问卷调查生产', '问卷调查'
)

# 问卷调查测试
wjdt_test = Env(
    'https://yflogin.vviton.com/ptyhzx-login/app/jsp/main/login.html',
    [
        {'name': '2000245878', 'pwd': '111111'},
    ],
    '问卷调查测试', '问卷调查'
)

# 个人中心测试
grzx_test = Env('http://yfi.wdcloud.cc/ptyhzx-grzx/app/jsp/jbxx/index.html',
                [
                    {'name': 'buyunjiao', 'pwd': '111111'},
                    {'name': '18622749772', 'pwd': 'qqqqqq'}
                ],
                '个人中心设置测试', '个人中心'
                )
# 个人中心生产
grzx_pro = Env('http://login.qdeduyun.cn/ptyhzx-grzx/app/jsp/jbxx/index.html',
               [
                   {'name': 'jmt01', 'pwd': '111111'},
               ],
               '青岛个人中心设置生产', '个人中心'
               )

# 国学
guoxue_test = Env('http://yfysgx.wdcloud.cc/webapp/app/jsp/qt/login.html',
                  [{'name': '18608051805', 'pwd': '111111'}],
                  '云上国学', "国学")
guoxueadmin_test = Env('http://yfgxadmin.wdcloud.cc/webapp/app/jsp/ht/login.html',
                       [{'name': 'jingde', 'pwd': '111111'}],
                       '国学后台', '国学')
guoxue_prod = Env('http://ysgx.xqngx.net',
                  [{'name': '15408221415', 'pwd': '111111'},
                   {'name': '15408231115', 'pwd': '111111'},
                   {'name': '15408231945', 'pwd': '111111'}, ],
                  '云上国学', '国学'
                  )
guoxueadmin_prod = Env('http://gxadmin.xqngx.net/webapp/app/jsp/ht/login.html',
                       [{'name': 'cswdgly1', 'pwd': 'wd1234'}],
                       '国学后台', '国学')
