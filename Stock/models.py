from django.db import models
from Components.models import Component, Supplier


class PurchaseOrder(models.Model):
    """
        Describes a supplier order
    """
    date = models.DateField()
    supplier = models.ForeignKey(Supplier)
    components = models.ManyToManyField(Component, through='PurchaseOrderToComponent')
    delivery_cost = models.FloatField()
    date_arrived = models.DateField(null=True, blank=True)


class PurchaseOrderToComponent(models.Model):
    po = models.ForeignKey(PurchaseOrder)
    component = models.ForeignKey(Component)
    quantity = models.IntegerField()


class Stock(models.Model):
    """
        The master stock sheet
    """
    component = models.ForeignKey(Component)
    quantity = models.IntegerField()
