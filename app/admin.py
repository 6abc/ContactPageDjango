# admin.py
from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'email', 'description' ]
    list_display = ['first_name', 'last_name', 'email', 'description' ]
    list_filter = ['first_name', 'last_name', 'email', 'description' ]
    search_fields = ['first_name', 'last_name', 'email', 'description' ]
