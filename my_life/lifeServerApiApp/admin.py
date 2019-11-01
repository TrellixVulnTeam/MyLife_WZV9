from django.contrib import admin
from .models import Diary

# Register your models here.
model_iterable = [Diary]

admin.site.register(model_iterable)
