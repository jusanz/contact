# contact
Django Contact App Example

Djangoの問い合わせフォームです。


- Django Rest Framework
- Sites Framework

に依存しています

## Example


```shell
$ git submodule add git@github.com:zoonaka/contact.git
```

```python3
# PROJECT_NAME/settings.py

INSTALLED_APPS = [
    ...
    'django.contrib.sites',
    'rest_framework',
    'contact',
    'theme',
    ...
]
...

SITE_ID = 1

```

```shell
$ python manage.py migrate
```

```python3
# PROJECT_NAME/urls.py

...
from django.urls import include
from django.views.generic import TemplateView

...
urlpatterns = [
    ...
    path('', TemplateView.as_view(template_name="theme/home.html"), name='home'),
    path('contact/', include('contact.urls')),
]
```

```html
<!-- theme/template/theme/base.html -->

{% load static %}
<!doctype html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.8.1/font/bootstrap-icons.css">
    <link rel="stylesheet" href="{% static 'theme/css/base.css' %}">
    {% block extra_css %}{% endblock %}

    <title>{% block title %}SITE_NAME{% endblock %}</title>
  </head>
  <body>

    {% block content %}{% endblock %}

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    {% block extra_js %}{% endblock %}

  </body>
</html>
```

```
<!-- theme/template/theme/home.html -->

{% extends "theme/base.html" %}

{% block content %}
<!-- hero -->
<div class="bg-dark text-secondary px-4 py-5 text-center">
  <div class="py-5">
    <h1 class="display-5 fw-bold text-white">SITE_NAME</h1>
     <!-- text -->
    <div class="col-lg-6 mx-auto">
      <a class="btn btn-outline-light" href="{% url 'contact:contact' %}">お問い合わせ</a>
    </div>
  </div>
</div>
{% endblock %}
```
