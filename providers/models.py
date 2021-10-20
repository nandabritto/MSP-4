from django.db import models

# Create your models here.

# Model for the provider section
class Providers(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=50)
    image = models.ImageField(uploaded_to='providers/images/', null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)