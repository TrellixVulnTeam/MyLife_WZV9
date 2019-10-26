from django.shortcuts import render
from django.views import View


class DiaryInfoDisplayView(View):
    """返回对应日记内的信息展示"""

    template_name = 'lifeInterfaceApp/archives/archives.html'

    def get(self, request):

        diary_id = self.get_diary_id()  # 获取对应日记id

        context = {
            'id': diary_id
        }

        return render(request, template_name=self.template_name, context=context)

    def get_diary_id(self):
        """获取当前对应日记的id"""
        diary_id = self.request.GET.get('life-share')
        if diary_id:
            if not isinstance(diary_id, int):
                # 如果id不为int类型,则返回空
                return None
            if diary_id <= 0:
                return None
            return diary_id
        return None

