# django_hide
Django package to hide from wappalizer. 
Wappalizer detects django by csrf-token tag in post forms. This package, encrypts the name of csrf-token tag.

# usage
Install it by:
``` pip install django-hide ```

Add `django_hide` to the installed apps.

Add `django_hide.middleware.CSRFHIDEMiddleware` to middlewares.

`{% load django_hide %}` in template.

Use `{% h_csrf_token %}` instead of `{% csrf_token %}` in forms in template.
