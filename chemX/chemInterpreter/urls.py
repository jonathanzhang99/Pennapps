from django.conf.urls import patterns, url

from chemInterpreter import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name="index"),
	)