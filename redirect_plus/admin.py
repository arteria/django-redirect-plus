from django.contrib import admin
from django.contrib.redirects.models import Redirect
from .models import RedirectLog

class RedirectLogAdmin(admin.ModelAdmin):
    pass

admin.site.register(RedirectLog, RedirectLogAdmin)