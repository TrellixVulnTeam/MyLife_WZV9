from django.urls import path, re_path
from .package_list import *

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),  # 首页
    re_path(r'^archives/$', DiaryInfoDisplayView.as_view(), name='lifeShare')  # 生活日记详细信息
]
