from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Foo(models.Model):
    title = models.CharField(max_length=100)


class Bar(models.Model):
    title = models.CharField(max_length=100)
    target_content_type = models.ForeignKey(ContentType)
    target_object_id = models.PositiveIntegerField()
    target = GenericForeignKey(
        "target_content_type", "target_object_id"
    )
