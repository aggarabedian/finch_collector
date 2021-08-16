from django.db import models
from django.db.models import Model, CharField, TextField, BooleanField, DateTimeField, ForeignKey
from django.db.models.fields import IntegerField
# Create your models here.

class Record(Model):

  title = CharField(max_length = 100)
  img = CharField(max_length = 600)
  artist = CharField(max_length = 100)
  year = IntegerField(default = 0)
  created_at = DateTimeField(auto_now_add = True)

  def __str__(self):
    return self.title

  class Meta:
    ordering = ['title']