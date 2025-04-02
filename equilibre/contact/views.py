from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm

class ContactView(FormView):
    template_name = "contact/form.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact_success")

    def form_valid(self, form):
        form.save()  # Sauvegarde automatique grâce au ModelForm
        return super().form_valid(form)