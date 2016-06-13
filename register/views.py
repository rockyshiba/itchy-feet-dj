from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Traveller

# Create your views here.

def index(request):
    travellers = Traveller.objects.all()
    template = loader.get_template('register/travellers.html')
    context = {'travellers': travellers,}
    return HttpResponse(template.render(context, request))

def traveller(request, traveller_id):
    sing_traveller = Traveller.objects.all()
    template = loader.get_template('register/travellers.html')
    context = {'travellers': travellers,}
    return HttpResponse(template.render(context, request))