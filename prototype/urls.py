from django.conf.urls import url

from prototype.views import prototype
from prototype.helpers import get_urls


urlpatterns = [
    url(r'^$', prototype, {'path': ''}, name='prototype'),
    url(r'^(?P<path>.*?)/$', prototype, name='prototype'),
] + get_urls(prototype)
