"""web_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from demo_test import views as demo_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^index/',demo_views.test_index),
    url(r'^add/(\d+)/(\d+)/$',demo_views.old_add_redirect),
    url(r'^new_add/(\d+)/(\d+)/$',demo_views.add,name='add2'),
    url(r'^add3/$',demo_views.add3,name='add3'),
    url(r'^regiter/$',demo_views.regiter,name='regiter'),
    url(r'^login/$',demo_views.login,name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/data', demo_views.data,name='locator_data'),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', include(admin.site.urls)),
    # url(r'^accounts/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)