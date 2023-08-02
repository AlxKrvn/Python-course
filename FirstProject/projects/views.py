from django.shortcuts import render

# Create your views here.
from projects.models import Projects

def project_index(request):
    projects = Projects.objects.all()
    context = {
        'projects' : projects
    }
    return render(request, 'project_index.html', context)