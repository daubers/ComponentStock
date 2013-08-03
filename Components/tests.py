__author__ = 'Matt'
from django.test import TestCase
from django.test.client import Client
import json


class ComponentTestCase(TestCase):
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

    def test_adding_a_manufacturer(self):
        """
            Attempts to add a manufactuerer to the database
        """
        response = self.addManufacturer()
        self.assertContains(response, "{\"HTTPRESPONSE\": 1}")

    def test_adding_a_supplier(self):
        """
            Attempts to add a new supplier to the database
        """
        response = self.addSupplier()
        self.assertContains(response, "{\"HTTPRESPONSE\": 1}")

    def test_adding_a_component(self):
        """
            Attempts to add a new supplier
        """
        response = self.addSupplier()
        self.assertContains(response, "{\"HTTPRESPONSE\": 1}")

        response = self.addManufacturer()
        self.assertContains(response, "{\"HTTPRESPONSE\": 1}")

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
        self.assertContains(response, "{\"HTTPRESPONSE\": 1}")
