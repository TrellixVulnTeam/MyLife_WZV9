"""本模块为了减少重复工作"""


class ModelsType(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            from ...models import (Diary)
            cls._instance[cls] = super(ModelsType, cls).__call__(*args, **kwargs)
            cls._diary_model = Diary.objects  # 日记数据库模型
        return cls._instance[cls]


class ModelObject(metaclass=ModelsType):

    @property
    def diary_model(self):
        return self._diary_model


modelObject = ModelObject()
