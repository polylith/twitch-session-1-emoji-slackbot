from django.db import models


# Create your models here.
class Employee(models.Model):
    slack_user_id = models.CharField(max_length=255)
    last_emoji = models.CharField(max_length=255)