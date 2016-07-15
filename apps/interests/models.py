from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.
@python_2_unicode_compatible
class Interest(models.Model):
    name = models.CharField(max_length = 200)
    created_at = models.DateTimeField()
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'interests'


@python_2_unicode_compatible
class User(models.Model):
    """docstring for User"""
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    age = models.IntegerField()
    created_at = models.DateTimeField(timezone.now())
    occupation = models.CharField(max_length = 200)
    interest = models.ForeignKey(Interest)
    def __str__(self):
        return self.first_name
    class Meta:
        db_table = 'users'
