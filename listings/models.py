from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    sub_district = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    floor_view = models.CharField(max_length=50)
    unit_type = models.CharField(max_length=10)
    condition = models.TextField(max_length=15)
    price_per_month = models.IntegerField()
    price_per_year = models.IntegerField()
    sqft = models.DecimalField(max_digits=5, decimal_places=1)
    facility = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name