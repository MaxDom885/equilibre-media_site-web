# contact/urls.py
from django.urls import path
from .views import ContactView # À créer si besoin

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact_form"),
]