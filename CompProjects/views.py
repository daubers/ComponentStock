# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
import json
from models import Project, Note, BOMQuant
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
        try:
            inputData = json.loads(request.POST['DATA'])
            newProject = Project()
            newProject.name = inputData['name']
            newProject.save()
            if len(inputData['components']) > 0:
                #We have to ensure we have these components in the linker table
                for component_id, quantity in inputData['components']:
                    component = Component.objects.filter(id=component_id).get()
                    newBOMQuant = BOMQuant.objects.create(project=newProject, component=component, quantity=quantity)
            if len(inputData['notes']) > 0:
                #add lots of notes if we have any
                for note_id in inputData['notes']:
                    newNote = Note.objects.filter(id=note_id).get()
                    newProject.notes.add(newNote)
            newProject.save()
            json_data = json.dumps({"HTTPRESPONSE": newProject.id})
        except Exception, e:
            json_data = json.dumps({"ERROR": e.message})
    else:
        json_data = json.dumps({"HTTPRESPONSE": None})
    # json data is just a JSON string now.
    return HttpResponse(json_data, mimetype="application/json")


def addForm(request):
    """
        Creates a form for adding new projects
    """
    t = get_template('CompProjects/AddProject.html')
    html = t.render(RequestContext(request))
    return HttpResponse(html)