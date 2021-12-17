from django.db import models

# Create your models here.
class DealershipRest(models.Model):
    _id = models.CharField(default="default_id", max_length=100)
    _rev = models.CharField(null=True, blank=True, max_length=100)
    id = models.CharField(primary_key=True, blank=True, max_length=100)
    city = models.CharField(null=True, blank=True, max_length=100)
    state = models.CharField(null=True, blank=True, max_length=100)
    st = models.CharField(null=True, blank=True, max_length=100)
    address = models.CharField(null=True, blank=True, max_length=100)
    zip_code = models.CharField(null=True, blank=True, max_length=100)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    short_name = models.CharField(null=True, blank=True, max_length=100)
    full_name = models.CharField(null=True, blank=True, max_length=100)
