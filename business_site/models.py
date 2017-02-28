from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    contract_no = models.CharField(u'ID单号',max_length=50,unique=True)
    describe = models.TextField(u'描述',max_length=200,blank=True)
    update_date = models.DateTimeField(u'更新时间',auto_now=True, null=True)
    create_date = models.DateTimeField(u'创建时间', auto_now_add=True, editable = True)
    operater = models.ForeignKey(User) #使用自带认证用户model
    def __str__(self):
        return self.contract_no

class Imageurl(models.Model):
    imageid = models.ForeignKey(Image,related_name='image_u') #利用外键反向关联image的单号
    image_url =models.ImageField(u'图片',upload_to='./image/')