from django.conf.urls import patterns, url
 
from chat import views
 
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(\d+)/$', views.chat_room, name='chat_room'),
	url(r'^chat*', views.chat_room, name='chat_room'),
]
