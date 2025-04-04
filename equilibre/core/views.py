from django.shortcuts import render
from django.views.generic import TemplateView  
from team.models import Member
from services.models import Service
from partners.models import Partner

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Services (avec featured si vous utilisez ce champ)
        context['services'] = Service.objects.filter(
            is_active=True,
            is_featured=True  # Optionnel - retirez si vous ne voulez pas filtrer
        ).order_by('display_order', 'name')[:6]
        
        # Partenaires
        partners = Partner.objects.filter(is_active=True)
        context['partners'] = partners
        context['partners_count'] = partners.count()
        
        return context

class AboutView(TemplateView):
    template_name = "core/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Le contexte des services est déjà fourni par le processeur
        context['members'] = Member.objects.filter(is_active=True)
        return context

# Vue Contact
def contact_view(request):
    return render(request, 'contact.html')  # Les services sont déjà dans le contexte