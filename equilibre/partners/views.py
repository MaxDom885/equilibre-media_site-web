from django.shortcuts import render
from django.views.generic import DetailView , ListView , TemplateView
from .models import Partner, PartnerType



class PartnerCarouselView(ListView):
    model = Partner 
    template_name = 'partners/home.html'
    context_object_name = 'partners'
    

    def get_queryset(self):return Partner.objects.filter(is_active=True ).order_by('name')

    
    
    
    
    
    


