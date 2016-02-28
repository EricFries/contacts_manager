from django.conf.urls import url

from . import views

app_name = 'contacts'

urlpatterns = [
	url(r'^create/', views.create, name='create'),
	url(r'^$', views.index, name='index'),
    url(r'^(?P<person_id>[0-9]+)/delete/', views.delete, name='delete'),
	url(r'^(?P<person_id>[0-9]+)/$', views.detail, name='detail')
]


r'^contacts/'
