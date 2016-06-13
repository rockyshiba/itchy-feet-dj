from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import About
# Create your views here.

def index(request):
    abt = About.objects.all()
    about_us = abt[0]
    template = loader.get_template('about/index.html')
    context = {'about_us': about_us,}
    return HttpResponse(template.render(context, request))

