# django_hide
Django package to hide from wappalyzer

# usage
Install it by:
``` pip install django-hide ```

Add `django_hide` to the installed apps.

Add `django_hide.middleware.CSRFHIDEMiddleware` to middlewares.

`{% load django_hide %}` in template.

Use `{% h_csrf_token %}` instead of `{% csrf_token %}` in forms in template.