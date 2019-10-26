from rest_framework import serializers


class HomeDiarySerializer(serializers.Serializer):

    # read_only = True  只能读不能写
    id = serializers.IntegerField(read_only=True, label='id')
    name = serializers.CharField(max_length=255, label='名称')
    title = serializers.CharField()
    comment = serializers.CharField()
    date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    classification = serializers.CharField(max_length=255, label='分类')
