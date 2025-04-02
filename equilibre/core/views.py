from django.views.generic import TemplateView  
from partners.models import Partner

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['partners'] = Partner.objects.filter(is_active=True)
        return context
class AboutView(TemplateView):  
    template_name = "core/about.html" 

class ServicesView (TemplateView):
    template_name= "core/services.html"