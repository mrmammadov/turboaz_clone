from django.db import models

# Create your models here.
class CarModel(models.Model):
    name = models.CharField(max_length=250)
    price = models.CharField(max_length=100)
    city = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    color = models.CharField(max_length=100)
    engine = models.CharField(max_length=200)
    year = models.CharField(max_length=50)

    def __str__(self):
        return self.name