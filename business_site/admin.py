from django.contrib import admin
from .models import Image
class ImageAdmin(admin.ModelAdmin):
    list_display = ['contract_no','image_url','describe','update_date','create_date','operater']
    # list_display_links =['contract_no'] #可以通过哪些字段link到详细内容
    search_fields = ['contract_no','describe'] #搜索
    list_filter = ['contract_no'] #筛选
    def save_model(self, request, obj, form, change):
        obj.operater = request.user #自定义操作，添加操作用户到数据库
        obj.save()
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj=None, **kwargs)
        self.exclude = ['operater'] #隐藏操作人field
        return form

# admin.site.register(Image)
admin.site.register(Image,ImageAdmin)

