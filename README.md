Django's built-in redirect app with some extras added.
============

Based on Django's built-in redirect app with some extras added. 
Starting point for this app was https://github.com/django/django/tree/master/django/contrib/redirects. Now with these extra features:

* Simple hit counter on each redirect rule

Installation
------------

To get the latest stable release from PyPi

    pip install django-redirect-plus

To get the latest commit from GitHub

    pip install -e git+git://github.com/arteria/django-redirect-plus.git#egg=redirect_plus




Add ``redirect_plus`` to your ``INSTALLED_APPS``

    INSTALLED_APPS = (
        ...,
        'django.contrib.redirects',
        'redirect_plus',
    )


Update your ``MIDDLEWARE_CLASSES`` in your project settings 
	
	MIDDLEWARE_CLASSES = (
	    ...
	    # 'django.contrib.redirects.middleware.RedirectFallbackMiddleware' , # <= comment this 
		'redirect_plus.middleware.RedirectFallbackMiddleware', # <= replace by /add this middleware
		...
	)

  

Don't forget to sync your database


    ./manage.py syncdb redirect_plus

 


 