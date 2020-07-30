"""manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'orm_userinfo$', views.orm_userinfo),
    re_path(r'orm_business$', views.orm_business),
    re_path(r'orm_host$', views.orm_host),
    re_path(r'orm_ip$', views.orm_ip),

    path(r'login/', views.login),
    path(r'home/index',views.index),
    path(r'home/host',views.host),
    path(r'home/ipPool',views.ipPool),
    path(r'home/sjbTool',views.sjbTool),
    re_path(r'home/detail-(?P<nid>\d+)',views.host_detail),
    re_path(r'host_add$', views.host_add),
    re_path(r'host_edit$', views.host_edit),
    re_path(r'home/del-(?P<nid>\d+)',views.host_del),



]
