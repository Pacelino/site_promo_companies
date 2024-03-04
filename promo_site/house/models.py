from django.db import models


# Create your models here.
class Houses(models.Model):
    city = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    house_number = models.IntegerField()
    entrance = models.IntegerField()
    # count_apartments = Null


class Apartments(models.Model):
    # entrance
    pass
