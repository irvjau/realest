from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Properties(models.Model):    
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    zip = models.IntegerField()
    state = models.CharField(max_length=2)
    beds = models.IntegerField()
    baths = models.IntegerField()
    sq_ft = models.IntegerField()
    type = models.CharField(max_length=25)
    sale_date = models.DateTimeField()
    price = models.IntegerField()
    latitude = models.DecimalField(decimal_places=6, max_digits=6)
    longitude = models.DecimalField(decimal_places=6, max_digits=6)
    image = models.FileField(null=True, blank=True)

    def get_absolute_url(self):
        return '%s' %{self.street}

    def slug(self):
        slug = slugify(self.street)
        return slug