from django.urls import path
from .views import home_view
from .views import (
    ServiceListView,
    ServiceDetailView,
)

urlpatterns = [
    path('', ServiceListView.as_view(), name='service-list'),
    path('<slug:slug>/', ServiceDetailView.as_view(), name='service-detail'),
    path('', home_view, name='home_view'),
    
]