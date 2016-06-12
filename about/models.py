from django.db import models

# Create your models here.

class About(models.Model):
    title_text = models.CharField(max_length=200)
    body_text = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title_text