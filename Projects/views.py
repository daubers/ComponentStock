# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
import json
from models import Project, Note
from Components.models import Component
from django.template.loader import get_template


def addProject(request):
    """
        Creates a new project in the database
        Returns a JSON thingied thing with the
        id on success, or an error message
        otherwise
    """
    if request.method == "POST":
        inputData = json.loads(request.POST['DATA'])
        newProject = Project()
        if len(inputData['components']) > 0:
            #We have to ensure we have these components in the linker table
            for component_id, quantity in inputData['components']:
                component = Component.objects.filter(id=component_id).get()
                newProject.bill_of_materials.create(component=component, quantity=quantity)
        if len(inputData['notes']) > 0:
            #add lots of notes if we have any
            for note_id in inputData['notes']:
                newNote = Note.objects.filter(id=note_id).get()
                newProject.notes.add(newNote)