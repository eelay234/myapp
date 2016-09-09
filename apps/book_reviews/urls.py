from django.conf.urls import include, url
from login.views import *
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^show_users/$', views.show_users, name="show_users"),
    url(r'^register/$', views.register),
    url(r'^login/$', views.login),
    url(r'^index_forms/$', views.index_forms),
    url(r'^register_success/$', views.register_success)
]
