from django.urls import path, re_path
from .package_list import *

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index')  # 首页
]
