from django.forms import Form
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Traveller, About, Homepage
from .models import TravellerForm
from django.views.generic.edit import UpdateView

# Create your views here.

def home(request):
    #homepage_content = Homepage.objects.all()
    travellers = Traveller.objects.all()
    template = loader.get_template('register/homepage.html')
    context = {'travellers': travellers,}
    return HttpResponse(template.render(context, request))

def about(request):
    abt = About.objects.all()
    about_us = abt[0]
    template = loader.get_template('register/about.html')
    context = {'about_us': about_us,}
    return HttpResponse(template.render(context, request))

def travellers(request):
    """
    Returns all travellers from the DB
    :param request:
    :return:
    """
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
    """
    Returns a traveller by id or a 404 error if no such traveller is found.
    :param request:
    :param traveller_id:
    :return:
    """
    person = get_object_or_404(Traveller, pk = traveller_id)
    return render(request, 'register/traveller.html', {'person' : person})


def register(request):
    """
    If form submits a POST request, a new TravellerForm instance containing a Traveller model is created with new_traveller.
    If the form data is valid, the new instance is saved to the DB and user is redirected to a thank you page.
        If the form isn't valid, the page reloads with the contents of the new instance.
    Arriving at the page creates a form object instance of TravellerForm and renders that form on the view.
    :param request:
    :return:
    """
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

def login(request, provided_email, provided_password):
    return render(request, 'register/login.html')

def update(request, traveller_email):
    """
    :param request:
    :param traveller_email:
    Find an existing Traveller object by email.
    :return:
    Returns a view contanting the object.
    """
    existing_traveller = get_object_or_404(Traveller, email = traveller_email)