from django.db import models
class Image(models.Model):
    contract_no = models.CharField(u'ID单号',max_length=50)
    image_url = models.CharField(u'图片URL',max_length=200)
    update_date = models.DateTimeField(u'更新时间',auto_now=True, null=True)
    create_date = models.DateTimeField(u'创建时间', auto_now_add=True, editable = True)
    operater = models.CharField(u'操作人',max_length=30,null=True,blank=True)
    def __str__(self):
        return self.image_url

