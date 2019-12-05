from __future__ import unicode_literals
import re

from django.conf import settings
from django.contrib.redirects.models import Redirect
from django.http import HttpResponsePermanentRedirect
try:
    from django.contrib.sites.models import get_current_site
except: 
    from django.contrib.sites.shortcuts import get_current_site

from django.core.exceptions import ImproperlyConfigured
from django import http

from .models import *

class RedirectFallbackMiddleware(object):

    # Defined as class-level attributes to be subclassing-friendly.
    response_gone_class = http.HttpResponseGone
    response_redirect_class = http.HttpResponsePermanentRedirect

    def __init__(self):
        if 'django.contrib.sites' not in settings.INSTALLED_APPS:
            raise ImproperlyConfigured(
                "You cannot use RedirectFallbackMiddleware when "
                "django.contrib.sites is not installed."
            )

    def process_response(self, request, response):
        # No need to check for a redirect for non-404 responses.
        if response.status_code != 404:
            return response

        full_path = request.get_full_path()
        current_site = get_current_site(request)

        r = None
        try:
            r = Redirect.objects.get(site=current_site, old_path=full_path)
        except Redirect.DoesNotExist:
            pass
        if settings.APPEND_SLASH and not request.path.endswith('/'):
            # Try appending a trailing slash.
            path_len = len(request.path)
            full_path = full_path[:path_len] + '/' + full_path[path_len:]
            try:
                r = Redirect.objects.get(site=current_site, old_path=full_path)
            except Redirect.DoesNotExist:
                pass
        if r is not None:
            if r.new_path == '':
                return self.response_gone_class()
            # store hit
            rhc = RedirectHitCounter(redirect=r)    
            rhc.save()
            return self.response_redirect_class(r.new_path)

        # No redirect was found. Return the response.
        return response
        
        
        
class RedirectForceMiddleware(object):
    """ Taken from https://djangosnippets.org/snippets/510/ 
        
        This middleware lets you match a specific url and redirect the request to a new url.

        You keep a tuple of url regex pattern/url redirect tuples on your site settings, example:

        URL_REDIRECTS = (
            (r'www\.example\.com/hello/$', 'http://hello.example.com/'),
            (r'www\.example2\.com/$', 'http://www.example.com/example2/'),
        )
    
    """
    def process_request(self, request):
        host = request.META['HTTP_HOST'] + request.META['PATH_INFO']
        for url_pattern, redirect_url in settings.URL_REDIRECTS:
            regex = re.compile(url_pattern)
            if regex.match(host):
                return HttpResponsePermanentRedirect(redirect_url)
