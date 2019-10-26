from django.shortcuts import render
from django.views import View


class IndexView(View):
    """主页视图处理类"""

    template_name = 'lifeInterfaceApp/home/index.html'

    def get(self, request):

        return render(request, template_name=self.template_name)
