from django.contrib import admin
from django.contrib.redirects.models import Redirect
from .models import RedirectHitCounter


class RedirectHitCounterAdmin(admin.ModelAdmin):
    list_filter = ('redirect__old_path', 'redirect__old_path',)
    search_fields = ['redirect__old_path', 'redirect__old_path',]
    
admin.site.register(RedirectHitCounter, RedirectHitCounterAdmin)