from django.contrib import admin
from django.contrib.redirects.models import Redirect
from .models import RedirectHitCounter


class RedirectHitCounterAdmin(admin.ModelAdmin):
    pass

admin.site.register(RedirectHitCounter, RedirectHitCounterAdmin)