from django.core.urlresolvers import reverse
from django.forms import widgets
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.db import connection, transaction
from django import forms
from selenium.webdriver.common.by import By

from .models import User, PcPageObject
from django.contrib.admin.sites import AdminSite


# from django.views.decorators.cache import cache_page


class Addforms(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()


# @cache_page(60*30) #可设定页面缓存和缓存时间
def test_index(request):
    string = list(range(10))
    cursor = connection.cursor()
    cursor.execute("select * from business_site_image")
    row = cursor.fetchone()
    if request.method == "POST":
        form = Addforms(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        form = Addforms()
    return render(request, 'demo_test/home.html', {'string': form})


def add(request, a, b):
    return HttpResponse(str(int(a) + int(b)))


def add3(request):
    a = request.POST['a']
    b = request.POST['b']
    return HttpResponse(str(int(a) + int(b)))


def old_add_redirect(request, a, b):  # 重定向
    return HttpResponseRedirect(reverse('add2', args=(a, b)))


class Userform(forms.Form):
    name = forms.CharField(label='用户名：', max_length=20)
    password = forms.CharField(label='密码：', widget=forms.PasswordInput())


# 注册
def regiter(request):
    if request.method == "POST":
        form = Userform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']  # 获取form里的值
            password = form.cleaned_data['password']
            User.objects.get_or_create(name=name, pwd=password)  # 插入数据库
            return render(request, 'demo_test/sucessful.html', {'username': name})
    else:
        form = Userform()
    return render(request, 'demo_test/resgiter.html', {'form': form})


# 登陆
def login(request):
    if request.method == "POST":
        form = Userform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            pwd = form.cleaned_data['password']
            user = User.objects.filter(name__exact=name, pwd__exact=pwd)  # 用户名密码对比
            if user:
                return render(request, 'demo_test/sucessful.html', {'username': name})
            else:
                return HttpResponseRedirect('/login')
    else:
        form = Userform()
    return render(request, 'demo_test/login.html', {'form': form})


class PageForm(forms.Form):
    page_name = forms.CharField(label='页面名称', max_length=100)
    locator_zh_name = forms.CharField(label='控件定位名称', max_length=100)
    choice = (
        ('ID', 'ID'), ('NAME', 'NAME'), ('LINK_TEXT', 'LINK_TEXT'), ('CLASS_NAME', 'CLASS_NAME'),
        ('CSS_SELECTOR', 'CSS_SELECTOR'), ('TAG_NAME', 'TAG_NAME'), ('XPATH', 'XPATH'),
        ('PARTIAL_LINK_TEXT', 'PARTIAL_LINK_TEXT'))
    locator_type = forms.ChoiceField(label='定位方式', choices=choice, required=True, initial=1, widget=widgets.RadioSelect)
    locator_key = forms.CharField(label='定位关键字', max_length=50)
    locator_value = forms.CharField(label='定位值', max_length=100)
    mark_content = forms.CharField(label='备注', required=False, widget=forms.Textarea)


def data(request):
    if request.method == 'POST':
        page_form = PageForm(request.POST)
        if page_form.is_valid():
            page_name = page_form.cleaned_data['page_name']
            locator_zh_name = page_form.cleaned_data['locator_zh_name']
            locator_type = page_form.cleaned_data['locator_type']
            locator_key = page_form.cleaned_data['locator_key']
            locator_value = page_form.cleaned_data['locator_value']
            mark_content = page_form.cleaned_data['mark_content']
            obj_result = PcPageObject.objects.get_or_create(page_name=page_name, locator_zh_name=locator_zh_name,
                                                            locator_type=locator_type, locator_key=locator_key,
                                                            locator_value=locator_value, mark=mark_content)
            if obj_result[1]:
                result = '数据创建成功!'
            else:
                result = '数据创建失败,定位关键字已存在!'
            # return render(request, 'demo_test/data_result.html', {'result': result})
            return HttpResponse(result)
    else:
        page_form = PageForm()
    return render(request, 'demo_test/data.html', {'page_form': page_form})
