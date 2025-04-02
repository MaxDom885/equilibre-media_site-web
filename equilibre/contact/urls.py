# contact/urls.py
from django.urls import path
from .views import ContactView, ContactSuccessView  # À créer si besoin

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact_form"),
    path("contact/success/", ContactSuccessView.as_view(), name="contact_success"),  # Optionnel
]