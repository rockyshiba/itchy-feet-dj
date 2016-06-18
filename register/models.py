from django.db import models
from django.forms import ModelForm

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
    email = models.EmailField(max_length = 100)
    hometown = models.CharField(max_length = 200)
    current_location = models.CharField(max_length = 200, blank = True, help_text = "You can leave this blank")
    biography = models.TextField(null = True, blank = True, help_text = "Don't write your life story! Just a little bit")
    image = models.ImageField(upload_to = None, height_field = None, width_field = None, max_length=100)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now = False, auto_now_add = True)
    edited_at = models.DateTimeField(auto_now = True, auto_now_add = False)
    deleted_at = models.DateTimeField(auto_now = False, auto_now_add = True)
    terms = models.BooleanField(help_text = "I agree to the terms and conditions.")
    def __str__(self):
        return self.username

class TravellerForm(ModelForm):
    class Meta:
        model = Traveller
        fields = ["first_name", "last_name", "email", "username", "hometown", "current_location", "biography", "image", "date_of_birth", "terms"]
