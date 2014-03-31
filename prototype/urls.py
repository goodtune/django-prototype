from django.conf.urls import patterns, url

urlpatterns = patterns('prototype.views',
    url(r'^$', 'prototype', {'path': ''}, name='index'),
    url(r'^(?P<path>.+?)/$', 'prototype', name='prototype'),
)
