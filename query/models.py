from django.db import models


class Log(models.Model):
    query = models.CharField(max_length=45)
    date = models.DateTimeField(auto_now=True)
