from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.store_list, name='store_list'),
    re_path(r'^(?P<pk>\d+)/$', views.store_detail, name='store_detail'),
    re_path(r'^new/$', views.store_create, name='store_create'),
    re_path(r'^(?P<pk>\d+)/update/$', views.store_update, name='store_update'),
    re_path(r'^(?P<pk>\d+)/delete/$', views.store_delete, name='store_delete'),
]