"""pantheon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.render_country_list, name='countries'),
    url(r'^country/(?P<country_code>\w*)$', views.render_industry_list_for_country, name='industries'),
    url(r'^country/(?P<country_code>\w*)/industry/(?P<industry>.*)$', views.render_person_list_for_country_industry, name='people'),
    url(r'^persons/(?P<person_id>[0-9]+)$', views.render_person, name='person'),
]
