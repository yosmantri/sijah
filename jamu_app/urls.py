from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	# url(r'^input', views.input, name='input'), # deprecated
	# url(r'^/get_list', views.get_list, name='get_list'),
	url(r'^search_ajax', views.search_ajax, name='search_ajax'),
	url(r'^search', views.search, name='search'),
]