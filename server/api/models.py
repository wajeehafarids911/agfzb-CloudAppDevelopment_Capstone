from django.db import models

# Create your models here.
class DealershipRest(models.Model):
    entry_id = models.IntegerField(default=999)
    dealerId = models.IntegerField()
    state = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
