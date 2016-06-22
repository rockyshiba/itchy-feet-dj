from django.forms import Form
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Traveller
from .models import Homepage
from .models import TravellerForm

# Create your views here.

def home(request):
    homepage_content = Homepage.objects.all()
    template = loader.get_template('register/homepage.html')
    context = {'homepage_content': homepage_content,}
    return HttpResponse(template.render(context, request))

def travellers(request):
    travellers = Traveller.objects.all()
    template = loader.get_template('register/travellers.html')
    context = {'travellers': travellers,}
    return HttpResponse(template.render(context, request))

def traveller(request):
    sing_traveller = Traveller.objects.all()
    template = loader.get_template('register/travellers.html')
    context = {'sing_traveller': sing_traveller,}
    return HttpResponse(template.render(context, request))

#def detail(request, traveller_id):
#    return HttpResponse("You're looking at traveller %s." % traveller_id)

def detail(request, traveller_id):
    person = get_object_or_404(Traveller, pk = traveller_id)
    return render(request, 'register/traveller.html', {'person' : person})

# def register(request):
#     template = loader.get_template('register/register.html')
#     return HttpResponse(template.render())

def register(request):
    if request.method == 'POST':
        new_traveller = TravellerForm(request.POST)
        if new_traveller.is_valid():
            new_traveller.save()
            template = loader.get_template('register/thanks.html')
            return HttpResponse(template.render())
        else:
            form = new_traveller
            return render(request, 'register/register.html', {'form': form})
    else:
        form = TravellerForm()
    return render(request, 'register/register.html', {'form': form})