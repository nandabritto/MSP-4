from django.db import models

# Create your models here.

# Model for Provider section
class Providers(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='providers/images/', null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)
    
    class Meta:
        ordering = ['created']