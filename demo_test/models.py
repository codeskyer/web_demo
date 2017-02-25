#coding=utf-8
from django.db import models
import pymysql
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

# Person.objects.get_or_create(name='wdliu',age=30)


