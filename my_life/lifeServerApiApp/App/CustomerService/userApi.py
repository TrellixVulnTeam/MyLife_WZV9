from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from ...settings.config import *


class UserApi(APIView):

    def get(self, request):

        return Response(data)
