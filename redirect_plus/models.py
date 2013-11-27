from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

from django.contrib.redirects.models import Redirect

class RedirectHitCounter(models.Model):
    redirect = models.ForeignKey(Redirect)
    timestamp = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return "%s was called at %s" % (str(self.redirect), str(self.timestamp))
        