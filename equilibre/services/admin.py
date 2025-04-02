from django.contrib import admin

from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', )
    list_filter = ('is_active', )
    prepopulated_fields = {'slug': ('name',)}  # Génère le slug automatiquement
  