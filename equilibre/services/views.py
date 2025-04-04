from django.views.generic import ListView , DetailView
from .models import Service

class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'
    paginate_by = 6  # Pagination optionnelle

    def get_queryset(self):
        return Service.objects.filter(is_active=True).order_by('name')
    
class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Service.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_services'] = Service.objects.filter(is_active=True).exclude(id=self.object.id)
        return context
    
    


