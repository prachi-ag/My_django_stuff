import django_filters
from . import models


class UserPartiInfoFilter(django_filters.FilterSet):

    class Meta:
        model = models.UserPartiInfo
        fields = ('user','event')
