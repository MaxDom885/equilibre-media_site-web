# votre_projet/urls.py
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from core.views import HomeView  # Importez directement la vue HomeView
from services.views import ServiceListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),  # Racine du site pointe vers HomeView
    path('', include('core.urls')),  # Inclut les autres URLs de l'app core
    path('nos-services/', ServiceListView.as_view(), name='service-list'),
    path('notre-agence/', include('team.urls')),
    path('', include('partners.urls')),  # Inclusion des URLs de l'application partners

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)