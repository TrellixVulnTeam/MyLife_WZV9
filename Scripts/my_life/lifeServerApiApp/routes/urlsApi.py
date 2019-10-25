from django.urls import path, re_path
from django.conf.urls import url
from .package_list import *

app_name = 'api'

# 注册上一级的路由地址并添加
urlpatterns = [
    re_path(r'^userInfo/$', UserApi.as_view(), name='userInfo')
]
