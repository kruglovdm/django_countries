from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)


class LanguagesCountries(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    languages = models.CharField(max_length=100)
