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
    context = {'sing_traveller': sing_traveller,}
    return HttpResponse(template.render(context, request))

def detail(request, traveller_id):
    return HttpResponse("You're looking at traveller %s." % traveller_id)