from django.conf.urls import url

from prototype.views import prototype

urlpatterns = [
    url(r'^$', prototype, {'path': ''}, name='prototype'),
    url(r'^(?P<path>.*?)/$', prototype, name='prototype'),
]
