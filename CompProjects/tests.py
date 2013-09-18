"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
import json


class SimpleTest(TestCase):
    def setUp(self):
        self.client = Client()

    def addSupplier(self):
        """
            Add a supplier to the database
            returns the response
        """
        compDict = {
            "name": "Google",
            "url": "http://www.google.com",
            "account_username": "Bob",
        }
        postDict = json.dumps(compDict)
        response = self.client.post('/supplier/add/', {'DATA': postDict, })
        return response

    def addManufacturer(self):
        """
            Add a manufacturer to the database
            returns the response
        """
        compDict = {
            "name": "Google",
            "url": "http://www.google.com",
        }
        postDict = json.dumps(compDict)
        response = self.client.post('/manufacturer/add/', {'DATA': postDict,})
        return response

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_adding_project(self):
        """
        Tests adding a new project using the json methods.
        """
        #first we'll need a supplier and a manufacturer
        self.addSupplier()
        self.addManufacturer()
        #add a component or two as we'll need them
        compDict = {
            "name": 'Test1',
            "cost": 4.00,
            "manufacturer": 1,
            "part_no": "ghykjh",
            "datasheet_uri": "http://www.google.com/",
            "supplier": 1
        }
        postDict = json.dumps(compDict)
        response = self.client.post('/component/add/', {'DATA': postDict,})
        response = self.client.post('/component/add/', {'DATA': postDict,})

        addJsonDict = {
            "name": "Test Project",
            "components": [(1,1),(2,1)],
            "notes": [],
        }
        addJson = json.dumps(addJsonDict)
        client = Client()
        response = client.post('/project/add/', {'DATA': addJson, })
        self.assertContains(response, "{\"HTTPRESPONSE\": 1}")