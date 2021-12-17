from django.db import models

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

class ReviewRest(models.Model):
    _id = models.CharField(default="default_id", max_length=100)
    _rev = models.CharField(null=True, blank=True, max_length=100)
    id = models.IntegerField(primary_key=True, blank=True)
    name = models.CharField(null=True, blank=True, max_length=100)
    dealership = models.IntegerField(null=True, blank=True)
    review = models.CharField(null=True, blank=True, max_length=300)
    purchase = models.BooleanField(null=True, blank=True)
    purchase_date = models.CharField(null=True, blank=True, max_length=100)
    car_make = models.CharField(null=True, blank=True, max_length=100)
    car_model = models.CharField(null=True, blank=True, max_length=100)
    car_year = models.CharField(null=True, blank=True, max_length=100)

