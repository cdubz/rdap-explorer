from django.db import models


class Log(models.Model):
    id = models.AutoField(primary_key=True)
    query = models.CharField(max_length=45)
    date = models.DateTimeField(auto_now=True)
    private = models.BooleanField(default=False)
