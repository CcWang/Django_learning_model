from django.conf.urls import patterns, url
from . import views
# from app.interests import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^interests/$',views.show,name = 'show'),
    url(r'^(?P<user_id>[0-9]+)/$',views.user, name='user')
]
