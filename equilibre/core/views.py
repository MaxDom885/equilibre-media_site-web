from django.shortcuts import render
from django.views.generic import TemplateView  
from team.models import Member
from services.models import Service
from partners.models import Partner

def home(request):
    return render(request, 'home.html', {
        'services': Service.objects.filter(is_active=True),
        'partners': Partner.objects.filter(is_active=True)
    })
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['partners'] = Partner.objects.filter(is_active=True)
        return context
class AboutView(TemplateView):
    template_name = "core/about.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = Member.objects.filter(is_active=True)
        return context 



