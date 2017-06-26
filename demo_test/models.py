# coding=utf-8
from django.db import models


class User(models.Model):
    name = models.CharField(u'用户名', max_length=20)
    pwd = models.CharField(u'密码', max_length=30)


class PcPageObject(models.Model):
    page_name = models.CharField(u'页面名称', max_length=100)
    locator_zh_name = models.CharField(u'控件定位名称', max_length=100)
    locator_type = models.CharField(u'定位方式', max_length=20)
    locator_key = models.CharField(u'定位关键字', unique=True, max_length=50)
    locator_value = models.CharField(u'定位值', max_length=100)
    mark = models.TextField(u'备注', max_length=100)

