from django.shortcuts import render

from .models import Profile, Project

# Create your views here.


def index(request):
    projects = Project.objects.all()
    profile = Profile.objects.get(pk=1)
    context = {'all_projects': projects, 'profile': profile}
    return render(request, 'index.html', context)
