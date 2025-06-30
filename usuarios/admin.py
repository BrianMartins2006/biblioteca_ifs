# usuarios/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_bibliotecario', 'matricula')}),
    )
    list_display = UserAdmin.list_display + ('is_bibliotecario', 'matricula')
    list_filter = UserAdmin.list_filter + ('is_bibliotecario',)
    search_fields = UserAdmin.search_fields + ('matricula',)

