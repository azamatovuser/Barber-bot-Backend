from django.db import models


class Client(models.Model):
    telegram_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=221)
    last_name = models.CharField(max_length=221)
    number = models.CharField(max_length=21, unique=True)

    def __str__(self):
        return self.first_name


class Schedule(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    month = models.CharField(max_length=221)
    day = models.IntegerField()
    time = models.TimeField()