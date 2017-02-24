from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
def test_index(request):
    return render(request,'home.html')
def add(request,a,b):
    return HttpResponse(str(int(a)+int(b)))
def old_add_redirect(request,a,b):
    return HttpResponseRedirect(reverse('add2',args=(a,b)))


