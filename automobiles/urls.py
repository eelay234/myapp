from django.conf.urls import include, url
from login.views import *
from . import views

urlpatterns = [
    url(r'^$', views.index),
]
