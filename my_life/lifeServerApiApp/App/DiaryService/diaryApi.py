from ...settings.config import data
from rest_framework.views import APIView
from django.http import JsonResponse
from .order.diary_serializer import HomeDiarySerializer
from ...utils.AppFunctools import modelObject
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class DiaryApi(APIView):

    PAGE_COUNT = 6  # 每页显示n条数据

    data = {
        "appStatus": {
            "errorCode": 0,
            "errorParameter": "",
            "message": "操作成功!"
        },
        "content": {}
    }

    def get(self, request):
        """首页获取日记简介的部分内容/首页不展示日记所有内容"""

        diary_list = modelObject.diary_model.all()

        paginator = Paginator(diary_list, self.PAGE_COUNT)

        page = request.GET.get('page', 1)  # 获取当前页数,None则取1

        try:
            diary = paginator.page(page)
        except PageNotAnInteger:
            # 如果page不为int类型,则返回第1页
            diary = paginator.page(self.PAGE_COUNT)
        except EmptyPage:
            # 如果page超出获取范围,则返回最后一页
            diary = paginator.page(paginator.num_pages)

        diary_data = HomeDiarySerializer(instance=diary, many=True).data
        self.data['content']['list'] = diary_data

        return JsonResponse(self.data)
