from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'fbuid', 'ospid', 'created_at', 'updated_at',)

    autocomplete_fields = ['user']