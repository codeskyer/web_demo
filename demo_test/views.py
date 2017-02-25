from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.db import connection,transaction
from django import forms
class Addforms(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()


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
    a = request.GET.get('a',None)
    b = request.GET.get('b',None)
    return HttpResponse(str(int(a)+int(b)))
def old_add_redirect(request,a,b): #重定向
    return HttpResponseRedirect(reverse('add2',args=(a,b)))


