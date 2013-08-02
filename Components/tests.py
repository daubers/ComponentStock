__author__ = 'Matt'
from django.test import TestCase
from django.test.client import Client
import json


class ComponentTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_adding_a_supplier(self):
        """
            Attempts to add a new supplier
        """
        compDict = {
            "name": "Google",
            "url": "http://www.google.com",
            "account_username": "Bob",
        }
        postDict = json.dumps(compDict)
        response = self.client.post('/supplier/add/', {'DATA': postDict,})
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
        print response
        self.assertContains(response, "{\"HTTPRESPONSE\": 1}")
