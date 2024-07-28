from django.http import HttpResponse
from django.shortcuts import render
from .models import Playground


def index(request):
    playground = Playground.objects.all()
    return render(request, 'index.html',
                  {'playgrounds': playground})
                  

def new(request):
    return HttpResponse('New playground')
