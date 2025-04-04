# core/urls.py
from django.urls import path, include
from .views import HomeView, AboutView

urlpatterns = [
    # Page d'accueil
    path('', HomeView.as_view(), name='home'),
    
    # Page "Notre Agence" avec la section équipe
    path("notre-agence/", AboutView.as_view(), name="about"),
    
    # Applications incluses
    path("services/", include("services.urls")),  # Structuré avec préfixe
    path("", include("team.urls")),       # URLs dédiées pour l'équipe
    path("contact/", include("contact.urls")),   # Contact avec préfixe clair
    path("partenaires/", include("partners.urls")),  # Partenaires avec préfixe
    
    
]