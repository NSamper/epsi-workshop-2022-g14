import uuid

from django.conf import settings
from django.db import models as m


# Create your models here.

class Person(m.Model):
    id = m.UUIDField(unique=True, primary_key=True, default=uuid.uuid4())
    f_name = m.CharField(max_length=15)
    l_name = m.CharField(max_length=15)
    username = m.ForeignKey(settings.AUTH_USER_MODEL, on_delete=m.SET_NULL, null=True, blank=True)


class Feedbacks(m.Model):
    id = m.UUIDField(unique=True, primary_key=True, default=uuid.uuid4())
    personKey = m.ForeignKey(Person, on_delete=m.SET_NULL, null=True)
    message = m.CharField(max_length=100)
    date = m.DateTimeField(auto_now=True)



