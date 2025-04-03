from django.urls import path  
from .views import TeamListView  

urlpatterns = [  
    path("", TeamListView.as_view(), name="about"),  # Note le nom de route clair  
]  