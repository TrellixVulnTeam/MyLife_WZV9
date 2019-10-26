def SingleType(cls):

    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            from ...models import Diary
            _instance[cls] = cls(*args, **kwargs)
            cls._diary = Diary.objects
        return _instance[cls]

    return _singleton


@SingleType
class ModelObject(object):

    @property
    def diary_model(self):
        return self._diary


modelObject = ModelObject()
