from django.shortcuts import render
from django.views.generic import DetailView , ListView , TemplateView
from .models import Partner



class PartnerCarouselView(ListView):
    model = Partner 
    template_name = 'home.html'
    context_object_name = 'partners'
    

    def get_queryset(self):return Partner.objects.filter(is_active=True ).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['partners'] = Partner.objects.filter(is_active=True)
        return context

    
    
    
    
    
    


