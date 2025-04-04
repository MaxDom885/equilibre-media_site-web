from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=100)
    slug= models.SlugField(max_length=100, unique=True)
    short_description = models.CharField( max_length=300 , blank=True )
    full_description = models.TextField()
    image = models.ImageField(upload_to='services/')
    is_active = models.BooleanField(default=True)
    icon = models.CharField(max_length=50, blank=True ,help_text="Utilise les classes Bootstrap Icons. Exemple: bi-rocket-takeoff → écrire 'bi-rocket-takeoff'")
    header_image = models.ImageField(upload_to='services/headers/', default= 'services/headers/default_header.jpg')
    strengths_image = models.ImageField(upload_to='services/strengths/', blank=True)
    strengths_text = models.TextField(
        "Atouts clés",
        max_length=500,
        blank=True,
        default="Notre expertise dans ce domaine inclut :\n- Solution personnalisée\n- Technologie de pointe\n- Support premium"
    )

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']