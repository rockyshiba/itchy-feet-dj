from django.contrib import admin
from .models import Traveller, About, Homepage

# Register your models here.

admin.site.register(Traveller)
admin.site.register(Homepage)
admin.site.register(About)