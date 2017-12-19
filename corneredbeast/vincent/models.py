from django.db import models

# Create your models here.
# 环境url表
class weidongurls(models.Model):
    name = models.CharField(max_length=40)
    environment = models.CharField(max_length=40)
    url = models.CharField(max_length=1000)
    business = models.CharField(max_length=40,blank=True,null=True)
    category = models.CharField(max_length=40, blank=True,null=True)
    comment = models.CharField(max_length=100, blank=True,null=True)
    flag = models.CharField(max_length=10, blank=True,null=True)
    create_user = models.CharField(max_length=50, blank=True,null=True) #help_text="添加者")
    create_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

# 环境用户表
class weidongusers(models.Model):
    username = models.CharField(max_length=40, blank=True)
    nickname = models.CharField(max_length=40, blank=True,null=True)
    password = models.CharField(max_length=40, blank=True,null=True)
    phone = models.CharField(max_length=40, blank=True,null=True)
    email = models.CharField(max_length=100, blank=True,null=True)
    portrait = models.CharField(max_length=300, blank=True,null=True)
    belongtourl = models.ForeignKey(weidongurls,blank=True,null=True)
    environment = models.CharField(max_length=40, blank=True)
    flag = models.CharField(max_length=10, blank=True)
    create_time = models.DateTimeField(auto_now=True)

# 所属项目表
# class weidongprojects(models.Model):
#     name = models.CharField(max_length=40)
#     create_user = models.CharField(max_length=50, blank=True, null=True)  # help_text="添加者")
#     create_time = models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.name

