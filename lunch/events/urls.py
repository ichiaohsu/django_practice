from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^new/$', views.EventCreateView.as_view(), name='event_create'),
    re_path(r'^(?P<pk>\d+)/$', views.EventDetailView.as_view(), name='event_detail'),
]