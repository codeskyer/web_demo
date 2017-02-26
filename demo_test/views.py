from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.db import connection,transaction
from django import forms
from .models import User
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
    if request.method =="POST":
        form = Addforms(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a)+int(b)))
    else:
        form = Addforms()
    return render(request, 'demo_test/home.html',{'string':form})
def add(request,a,b):
    return HttpResponse(str(int(a)+int(b)))
def add3(request):
    a = request.POST['a']
    b = request.POST['b']
    return HttpResponse(str(int(a)+int(b)))
def old_add_redirect(request,a,b): #重定向
    return HttpResponseRedirect(reverse('add2',args=(a,b)))

class Userform(forms.Form):
    name = forms.CharField(label='用户名：',max_length=20)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())
#注册
def regiter(request):
    if request.method =="POST":
        form = Userform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'] #获取form里的值
            password = form.cleaned_data['password']
            User.objects.get_or_create(name=name,pwd=password) #插入数据库
            return render(request,'demo_test/sucessful.html',{'username':name})
    else:
        form = Userform()
    return render(request,'demo_test/resgiter.html',{'form':form})
#登陆
def login(request):
    if request.method=="POST":
        form = Userform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            pwd = form.cleaned_data['password']
            user = User.objects.filter(name__exact=name,pwd__exact=pwd)#用户名密码对比
            if user:
                return render(request,'demo_test/sucessful.html',{'username':name})
            else:
                return HttpResponseRedirect('/login')
    else:
        form = Userform()
    return render(request,'demo_test/login.html',{'form':form})
