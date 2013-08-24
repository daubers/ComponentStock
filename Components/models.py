from django.db import models

# Create your models here.


class Supplier(models.Model):
    """
        Describes a supplier
    """
    name = models.CharField(max_length=255)
    url = models.URLField()
    account_no = models.CharField(max_length=255, null=True)
    account_username = models.CharField(max_length=255)


class Manufacturer(models.Model):
    """
        Describes a manufacturer
    """
    name = models.CharField(max_length=255)
    url = models.URLField()

class Component(models.Model):
    """
        Basic component class
    """
    name = models.CharField(max_length=255)
    part_no = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier)
    cost = models.FloatField()
    manufacturer = models.ForeignKey(Manufacturer)
    datasheet_uri = models.URLField(null=True)
    max_quantity = models.IntegerField(null=True)
    min_quantity = models.IntegerField(null=True)