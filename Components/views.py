from django.http import HttpResponse
from django.template import RequestContext, loader
import json

from Components.models import Component, Supplier, Manufacturer
from django.template.loader import get_template
from django.template import Context


def newManufacturerForm(request):
    """
        A simple form to add a new manufacturer
    """
    t = get_template('Components/newManufacturerForm.html')
    html = t.render(RequestContext(request))
    return HttpResponse(html)


def newComponentForm(request):
    """
        A simple form to add a new component
    """
    t = get_template('Components/newComponent.html')
    html = t.render(RequestContext(request))
    return HttpResponse(html)


def newManufacturer(request):
    """
        Create a new manufacturer in the database
    """
    if request.method == "POST":
        data = json.loads(request.POST['DATA'])
        print request.POST['DATA']
        try:
            print(data)
            newMan = Manufacturer(name=data['name'], url=data['url'])
            newMan.save()
            json_data = json.dumps({"HTTPRESPONSE": newMan.id})
        except Exception, e:
            json_data = json.dumps({"HTTPRESPONSE": e.message})
    else:
        json_data = json.dumps({"HTTPRESPONSE": None})
    return HttpResponse(json_data, mimetype="application/json")


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
            newSupply = Supplier(name=data['name'], url=data['url'], account_no=account_no,
                                 account_username=data['account_username'])
            newSupply.save()
            json_data = json.dumps({"HTTPRESPONSE": newSupply.id})
        except Exception, e:
            json_data = json.dumps({"HTTPRESPONSE": None, "Error": e.message})
    else:
        json_data = json.dumps({"HTTPRESPONSE": None})
    # json data is just a JSON string now.
    return HttpResponse(json_data, mimetype="application/json")


def newSupplierForm(request):
    """
        Creates a form for adding new suppliers
    """
    t = get_template('Components/newSupplier.html')
    html = t.render(RequestContext(request))
    return HttpResponse(html)

def getSuppliers(request):
    """
        Returns a JSON formatted dictionary of suppliers
    """
    returnObject = None
    if request.method == "POST":
        data = json.loads(request.POST['DATA'])
        if data['id'] is None:
            returnObject = list(Supplier.objects.all().values())
        else:
            returnObject = Supplier.objects.filter(id=data['id']).get()
        return HttpResponse(json.dumps(returnObject), mimetype="application/json")
    else:
        returnObject = list(Supplier.objects.all().values())
        return HttpResponse(json.dumps(returnObject))


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
            sup = Supplier.objects.filter(id=data['supplier']).get()
            manf = Manufacturer.objects.filter(id=data['manufacturer']).get()
            comp = Component(name=data['name'], cost=data['cost'], manufacturer=manf,
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


def getManufacturer(request):
    """
        Returns a json dictionary of all the manufacturers
        Can optionally be filtered by id
    """
    returnObject = None
    if request.method == "POST":
        data = json.loads(request.POST['DATA'])
        if data['id'] is None:
            returnObject = list(Manufacturer.objects.all().values())
        else:
            returnObject = Manufacturer.objects.filter(id=data['id']).get()
        return HttpResponse(json.dumps(returnObject), mimetype="application/json")
    else:
        returnObject = list(Manufacturer.objects.all().values())
        return HttpResponse(json.dumps(returnObject))

def getComponents(request, dataTable=None):
    """
        Returns a JSON dictionary containing all of the components in the database
    """
    returnObject = None
    if dataTable is not None:
        #We need to put this into an aaData object
        componentsList = []
        for i in Component.objects.all().values():
            i["manufacturer"] = list(Manufacturer.objects.filter(id=i["manufacturer_id"]).all().values())
            componentsList.append(i)
        returnObject = {"aaData": [i,], }
    return HttpResponse(json.dumps(returnObject), mimetype="application/json")

def viewComponents(request):
    """
        Goes to a page where all existing components can be viewed
    """
    t = get_template('Components/viewComponents.html')
    html = t.render(RequestContext(request))
    return HttpResponse(html)