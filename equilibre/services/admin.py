from django.contrib import admin

from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', )
    list_filter = ('is_active', )
    prepopulated_fields = {'slug': ('name',)}  # Génère le slug automatiquement
    fieldsets = (
        ('Informations de base', {
            'fields': ('name', 'slug', 'is_active')
        }),
        ('Contenu principal', {
            'fields': ('short_description', 'full_description', 'icon','strengths_text')
        }),
        ('Gestion des images', {
            'fields': ('image', 'header_image', 'strengths_image'),
            'classes': ('collapse',)  # Section pliable
        }),
    )
  