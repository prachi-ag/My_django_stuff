from .import models
from rest_framework import serializers

class UserPartiInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserPartiInfo
        fields = ('user', 'event', 'sub_event')
