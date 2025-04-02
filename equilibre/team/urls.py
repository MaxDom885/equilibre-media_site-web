from django.urls import path  
from .views import TeamListView  

urlpatterns = [  
    path("notre-equipe/", TeamListView.as_view(), name="team_list"),  # Note le nom de route clair  
]  