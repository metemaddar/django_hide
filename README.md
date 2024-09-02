# Django Hide
![Django CI](https://github.com/metemaddar/django_hide/actions/workflows/django.yml/badge.svg)

Django package to hide any Django application's programming languages and frameworks from apps such as Wappalyzer.
Wappalizer detects django by csrf-token tag in post forms. This package, encrypts the name of csrf-token tag.

# Requirements

## Python
Python versions 3.6 or later are supported with a limit to what Django itself supports.
See also [What Python version can I use with Django?](https://docs.djangoproject.com/en/stable/faq/install/#what-python-version-can-i-use-with-django)

## Installation
You can install from [PyPI](https://pypi.python.org/pypi/django-hide) using `pip` to install `django-hide` and its dependencies:

```shell
$ pip install django-hide
```

## Setup
Add the following apps to the `INSTALLED_APPS`:

```django
INSTALLED_APPS = (
    ...
    'django_hide',
)
```

Add the `django_hide` middleware to your `MIDDLEWARE`:

```django
MIDDLEWARE = (
    ...
    'django_hide.middleware.CSRFHIDEMiddleware',
)
```

Load the `{% load django_hide %}` templatetag in your templates:

```html
{% extends "base.html" %}
{% load django_hide %}
```

Change `{% csrf_token %}` to `{% h_csrf_token %}` in your forms in every template:

```html
<form method="post" action="{% url 'action' %}" 
      onsubmit="return confirm('Are you sure?')">
    
    {% h_csrf_token %}

    <button class="btn btn-sm btn-warning"
            type="submit">{% "Submit" %}</button>
</form>
```

## Note

Clear Wappalyzer cookies to make sure your django app is hidden.
