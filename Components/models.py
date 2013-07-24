from django.db import models

# Create your models here.


class supplier(models.Model):
    """
        Describes a supplier
    """
    name = models.CharField(max_length=255)
    url = models.URLField()
    account_no = models.CharField(max_length=255, null=True)
    account_name = models.CharField(max_length=255)


class Manufacturer(models.Model):
    """
        Describes a manufacturer
    """
    name = models.CharField(max_length=255)


class Component(models.Model):
    """
        Basic component class
    """
    name = models.CharField(max_length=255)
    supplier = models.ForeignKey(supplier)
    cost = models.IntegerField()
    manufacturer = models.ForeignKey(Manufacturer)
    datasheet_uri = models.URLField(null=True)
    max_quantity = models.IntegerField(null=True)
    min_quantity = models.IntegerField(null=True)