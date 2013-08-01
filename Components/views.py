from django.http import HttpResponse
from django.template import RequestContext, loader
import json

from Components.models import Component


def newComponent(request):
    """
        Add a new component to the database
    """
    if request.method == "POST":
        #we have some data! Woo
        #start a new object
        name = request.POST['name']
        part_no = request.POST['part_no']
        cost = request.POST['cost']
        manufacturer = request.POST['manufacturer']
        supplier = request.POST['supplier']
        datasheet_uri = request.POST['datasheet_uri']
        if "max_quantity" in request.POST.keys():
            max_quantity = request.POST['max_quantity']
        else:
            max_quantity = None

        if "min_quantity" in request.POST.keys():
            min_quantity = request.POST['min_quantity']
        else:
            min_quantity = None
        comp = Component(name=name, cost=cost, manufacturer=manufacturer, part_no=part_no, datasheet_uri=datasheet_uri,
                         supplier=supplier, max_quantity=max_quantity, min_quantity=min_quantity)
        try:
            comp.save()
            json_data = json.dumps({"HTTPRESPONSE": comp.id})
        except:
            json_data = json.dumps({"HTTPRESPONSE": None})
    else:
        json_data = json.dumps({"HTTPRESPONSE": None})
    # json data is just a JSON string now.
    return HttpResponse(json_data, mimetype="application/json")
