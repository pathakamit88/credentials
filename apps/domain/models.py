from django.db import models

from apps.common.models import CommonData


class DomainDetail(CommonData):

    name = models.CharField(max_length=25)
    url = models.URLField()
    username = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=25)
    additional_info = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

