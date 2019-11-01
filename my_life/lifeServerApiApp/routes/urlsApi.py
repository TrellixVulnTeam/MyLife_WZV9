from django.urls import path, re_path
from .package_list import *

app_name = 'api'

# 注册上一级的路由地址并添加
urlpatterns = [
    re_path(r'^userInfo/$', UserApi.as_view(), name='userInfo'),
    re_path(r'^diaryInfo/$', DiaryApi.as_view(), name='diaryInfo'),
    re_path(r'^diaryMsg/$', DiarySpecMsg.as_view(), name='diaryMsg'),
]
