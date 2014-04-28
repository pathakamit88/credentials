from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class CommonData(models.Model):
    published = models.BooleanField(default=True)
    created = models.DateTimeField(
        verbose_name=_('Created'),
        auto_now_add=True,
        editable=False
    )

    modified = models.DateTimeField(
        verbose_name=_('Modified'),
        auto_now=True,
        null=True,
        editable=False
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Created by'),
        related_name="%(class)s_related",
        editable=False
    )

    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Modified by'),
        related_name="%(class)s_related_mod",
        null=True,
        editable=False
    )

    class Meta:
        abstract = True
