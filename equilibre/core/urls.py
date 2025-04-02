# core/urls.py  
from django.urls import path, include  # Ajoute include()  
from .views import HomeView, AboutView, ServicesView  

urlpatterns = [  
    path('', HomeView.as_view(), name='home'),
    path("notre-agence/", AboutView.as_view(), name="about"),  
    path("",include("services.urls")),  # À remplacer plus tard par include("services.urls")  
    path("", include("team.urls")),  # Inclus les URLs de team/ 
    path("", include("contact.urls")) ,
    path("", include("partners.urls")) 
]  