from django.conf.urls import url
from django.contrib.staticfiles import views

from prototype.views import prototype
from prototype.helpers import get_urls


urlpatterns = [
    url(r'^$', prototype, {'path': ''}, name='prototype'),
    url(r'^(?P<path>.*?)/$', prototype, name='prototype'),
    url(r'^static/(?P<path>.*)$', views.serve),
] + get_urls(prototype)
