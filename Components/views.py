from django.http import HttpResponse
from django.template import RequestContext, loader
import json

from Components.models import Component, supplier


def newSupplier(request):
    """
        Create a new supplier in the database
    """
    if request.method == "POST":
        #check to see if we have the optional account_no
        data = json.loads(request.POST['DATA'])
        if "account_no" in data.keys():
            account_no = data['account_no']
        else:
            account_no = None
        #now create a new supplier
        try:
            newSupply = supplier(name=data['name'], url=data['url'], account_no=account_no, account_username=data['account_username'])
            newSupply.save()
            json_data = json.dumps({"HTTPRESPONSE": newSupply.id})
        except:
            json_data = json.dumps({"HTTPRESPONSE": None})
    else:
        json_data = json.dumps({"HTTPRESPONSE": None})
    # json data is just a JSON string now.
    return HttpResponse(json_data, mimetype="application/json")

def newComponent(request):
    """
        Add a new component to the database
    """
    if request.method == "POST":
        #we have some data! Woo
        #we should recieve a posted JSON encoded dictionary containing
        #name,cosr,manufacturer,part_no,datasheet_uri,supplier
        #and optionally max_quantity and min_quantity
        data = json.loads(request.POST['DATA'])
        if "max_quantity" in data.keys():
            max_quantity = data['max_quantity']
        else:
            max_quantity = None

        if "min_quantity" in data.keys():
            min_quantity = data['min_quantity']
        else:
            min_quantity = None
        try:
            #get the supplier object
            sup = supplier.objects.filter(id=data['supplier']).get()
            comp = Component(name=data['name'], cost=data['cost'], manufacturer=data['manufacturer'],
                             part_no=data['part_no'], datasheet_uri=data['datasheet_uri'],
                             supplier=sup, max_quantity=max_quantity, min_quantity=min_quantity)

            comp.save()
            json_data = json.dumps({"HTTPRESPONSE": comp.id})
        except Exception, e:
            json_data = json.dumps({"ERROR": e.message})
    else:
        json_data = json.dumps({"HTTPRESPONSE": None})
    # json data is just a JSON string now.
    return HttpResponse(json_data, mimetype="application/json")
