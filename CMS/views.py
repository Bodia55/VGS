from django.shortcuts import render
from .models import Resource

# Create your views here.
def cms(request):
    resources = Resource.objects.all()
    context = {'resources':resources}
    return render(request, 'cms.html', context)

def gdd_view(request):
    resources = Resource.objects.filter(committee='GDD')
    context = {'name':'GDD', 'resources':resources}
    return render(request, 'committee-view.html', context)

def gsd_view(request):
    resources = Resource.objects.filter(committee='GSD')
    context = {'name':'GSD', 'resources':resources}
    return render(request, 'committee-view.html', context)

def gad_view(request):
    resources = Resource.objects.filter(committee='GAD')
    context = {'name':'GAD', 'resources':resources}
    return render(request, 'committee-view.html', context)