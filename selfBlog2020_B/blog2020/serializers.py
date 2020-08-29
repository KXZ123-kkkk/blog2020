from rest_framework import serializers
from . import models


class LeaveMessageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LeaveMessage
        fields = '__all__'


class WebReadPersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recording
        fields = '__all__'


class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = ['id', 'title', 'subTitle', 'passage', 'gitHubUrl', 'blogReadPerson', 'Tag',
                  'Create_Time','leaveMessageCount']
        depth = 3


class ReplyMessageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReplyMessage
        fields = '__all__'


class MusicModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Music
        fields = '__all__'


class CartoonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cartoon
        fields = '__all__'
        depth = 2
