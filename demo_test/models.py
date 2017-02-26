#coding=utf-8
from django.db import models
import pymysql
class User(models.Model):
    name = models.CharField(u'用户名',max_length=20)
    pwd = models.CharField(u'密码',max_length=30)


