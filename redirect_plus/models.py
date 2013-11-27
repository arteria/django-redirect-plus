from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

from django.contrib.redirects.models import Redirect

class RedirectLog(models.Model):
    redirect = models.ForeignKey('Redirect')
    hit = models.DateTimeField(auto_now=False)