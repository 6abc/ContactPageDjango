# admin.py
from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'subj', 'desc' ]
    list_display = ['name', 'email', 'subj' ]
    list_filter = ['name', 'email', 'subj' ]
    search_fields = ['name', 'email', 'subj', 'desc' ]