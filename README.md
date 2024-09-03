# Django Hide

![Django CI](https://github.com/metemaddar/django_hide/actions/workflows/django.yml/badge.svg)

<p align="center">
  <img src="https://raw.githubusercontent.com/metemaddar/django_hide/master/docs/logo.svg" alt="Logo"/>
</p>

**Django Hide** is a Django package designed to obscure your application's programming languages and frameworks from detection tools like Wappalyzer. By encrypting the CSRF token tag, this package helps prevent Wappalyzer and similar tools from identifying your application as a Django project.

## Requirements

### Python
Supports Python versions 3.6 and later, in line with Django’s compatibility. For more details on Python versions compatible with Django, see [What Python version can I use with Django?](https://docs.djangoproject.com/en/stable/faq/install/#what-python-can-i-use-with-django)

## Installation

Install `django-hide` and its dependencies from [PyPI](https://pypi.python.org/pypi/django-hide) using `pip`:

```shell
pip install django-hide
```

## Setup

1. Add `django_hide` to your `INSTALLED_APPS`:

    ```python
    INSTALLED_APPS = (
        ...
        'django_hide',
    )
    ```

2. Add `django_hide` middleware to your `MIDDLEWARE`:

    ```python
    MIDDLEWARE = (
        ...
        'django_hide.middleware.CSRFHIDEMiddleware',
    )
    ```

3. Load the `{% load django_hide %}` template tag in your templates:

    ```html
    {% extends "base.html" %}
    {% load django_hide %}
    ```

4. Replace `{% csrf_token %}` with `{% h_csrf_token %}` in your forms:

    ```html
    <form method="post" action="{% url 'action' %}" 
          onsubmit="return confirm('Are you sure?')">
        
        {% h_csrf_token %}

        <button class="btn btn-sm btn-warning"
                type="submit">{% "Submit" %}</button>
    </form>
    ```

## Note

To ensure your Django application remains hidden, clear Wappalyzer cookies.
