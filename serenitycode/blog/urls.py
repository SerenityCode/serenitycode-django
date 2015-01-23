from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^(?P<post_id>\d+)/$', views.post, name="view_post"),
)
