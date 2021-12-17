from django.db import models

# Create your models here.
class DealershipRest(models.Model):
    dealerId = models.IntegerField()
    state = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
