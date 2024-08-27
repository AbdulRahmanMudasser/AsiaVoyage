from django.db import models

# Create your models here.
class Tour(models.Model):
    # orgin country
    origin_conutry = models.CharField(max_length=64)
    
    # destination country
    destination_country = models.CharField(max_length=64)
    
    # number of nights
    number_of_nights = models.IntegerField()
    
    # price of tour
    price = models.IntegerField()
