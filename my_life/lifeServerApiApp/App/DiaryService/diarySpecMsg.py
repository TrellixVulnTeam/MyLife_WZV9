from rest_framework.views import APIView
from django.http import JsonResponse
from .order.diary_serializer import SpecDiarySerializer
from ...utils.AppFunctools import modelObject


class DiarySpecMsg(APIView):
    """指定id获取对应日记的信息"""

    data = {
        "appStatus": {
            "errorCode": 0,
            "errorParameter": "",
            "message": "操作成功!"
        },
        "content": {}
    }

    def post(self, request):

        diary_id = self.get_diary_id()

        diary = modelObject.diary_model.filter(pk=diary_id)

        if diary:
            diary_data = SpecDiarySerializer(instance=diary[0]).data
            self.data['content']['item'] = diary_data
        else:
            self.data['appStatus']['errorCode'] = 1
            self.data['appStatus']['message'] = "操作失败!"

        return JsonResponse(self.data)

    def get_diary_id(self):
        """获取日记id"""
        diary_id = self.request.data.get('id')
        if diary_id:
            if not isinstance(diary_id, int) or not diary_id > 0:
                # 如果不为integer抛异常
                raise TypeError('exception %s => Type not is integer or scope of not less than zero' % diary_id)
            return diary_id
        raise ValueError("exception id can't be empty...")
