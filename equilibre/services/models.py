from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=100)
    slug= models.SlugField(max_length=100, unique=True)
    short_description = models.CharField( max_length=300 , blank=True )
    full_description = models.TextField()
    image = models.ImageField(upload_to='services/')
    is_active = models.BooleanField(default=True)
    icon = models.CharField(max_length=50, blank=True)
  

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']