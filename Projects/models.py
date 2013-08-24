from django.db import models
from Components.models import Component

class ReferenceType(models.Model):
    """
        Just holds the different reference types
    """
    type_name = models.CharField()


class Reference(models.Model):
    """
        Class to define a reference link
    """
    reference_url = models.URLField(null=True)
    reference_type = models.ForeignKey(ReferenceType)
    reference_name = models.CharField()
    reference_notes = models.ManyToManyField(Note)


class Note(models.Model):
    """
        Class to describe "note" objects
    """
    subject = models.CharField()
    note = models.CharField()


class BOMQuant(models.Model):
    project = models.ForeignKey(Project)
    component = models.ForeignKey(Component)
    quantity = models.IntegerField()


class Project(models.Model):
    """
        Class to hold all of the links to a model thing
    """
    name = models.CharField()
    sub_projects = models.ManyToManyField("Project", null=True)
    bill_of_materials = models.ManyToManyField(Component, through="BOMQuant", null=True)
    notes = models.ManyToManyField(Note, null=True)