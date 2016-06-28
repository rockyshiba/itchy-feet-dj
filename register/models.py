from django.db import models
from django.forms import ModelForm
from datetime import date
from django import forms

#makes all date fields as html input type=date or datetime
forms.DateInput.input_type = "date"
forms.DateTimeInput.input_type = "datetime-local"

# Create your models here.

class Homepage(models.Model):
    title_text = models.CharField(max_length = 50)
    body_text = models.TextField(null = True, blank = True)
    logo_image = models.ImageField(upload_to = None, height_field = None, width_field = None, max_length = 100)
    def __str__(self):
        return self.title_text

class Traveller(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    GENDERS = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length = 1, choices = GENDERS)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 100)
    hometown = models.CharField(max_length = 200)
    current_location = models.CharField(max_length = 200, blank = True, help_text = "You can leave this blank")
    biography = models.TextField(null = True, blank = True, help_text = "Don't write your life story! Just a little bit")
    image = models.ImageField(null = True, blank = True, upload_to = None, height_field = None, width_field = None, max_length=10000, default = 'images/feet.png')
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now = False, auto_now_add = True)
    edited_at = models.DateTimeField(auto_now = True, auto_now_add = False)
    deleted_at = models.DateTimeField(null = True, blank = True)
    terms = models.BooleanField(help_text = "I agree to the terms and conditions.")
    def __str__(self):
        return self.username

class TravellerForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = Traveller
        fields = ["first_name", "last_name", "email", "gender", "username", "password", "hometown", "current_location", "biography", "image", "date_of_birth", "terms"]
        date_of_birth = forms.DateField()

class About(models.Model):
    title_text = models.CharField(max_length=200)
    body_text = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title_text