from datetime import datetime
from django.db import models


class Realtor(models.Model):
    name = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length=20)
    is_mvp = models.IntegerField(default=False)
    hire_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
