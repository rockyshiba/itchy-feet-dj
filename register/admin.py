from django.contrib import admin
from .models import Traveller
from .models import Homepage

# Register your models here.

admin.site.register(Traveller)
admin.site.register(Homepage)