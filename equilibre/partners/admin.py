from django.contrib import admin
from .models import PartnerType, Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', )
    list_filter = ( 'is_active')
    
    
