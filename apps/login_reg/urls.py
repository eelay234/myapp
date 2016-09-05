from django.conf.urls import include, url
from login.views import *
from . import views

urlpatterns = [
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^article/(?P<pk>\d+)/comment/$', views.add_comment_to_article, name='add_comment_to_article'),
    url(r'^articles/like/(?P<article_id>\d+)/$', views.like_article),
    url(r'^articles/create/$', views.create),
    url(r'^articles/all/$', views.articles),
    url(r'^get/(?P<article_id>\d+)/$', views.article),
    url(r'^language/(?P<language>[a-z\-]+)/$', views.language),
    url(r'^hello/$', views.hello),
    url(r'^hello_template/$', views.hello_template),
    url(r'^hello_template_simple/$', views.hello_template_simple),
    url(r'^$', views.login),
    url(r'^accounts/logout/$', views.logout),
    url(r'^accounts/login/$', views.login), # If user is not login it will redirect to login page
    url(r'^accounts/auth/$', views.auth_view),
    url(r'^accounts/loggedin/$', views.loggedin),
    url(r'^accounts/invalid/$', views.invalid_login),
    url(r'^accounts/register/$', views.register_user),
    url(r'^accounts/register_success/$', views.register_success),
]
