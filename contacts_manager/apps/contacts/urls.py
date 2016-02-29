from django.conf.urls import url

from . import views

app_name = 'contacts'

urlpatterns = [
    url(r'^create/', views.create, name='create'),
    url(r'^(?P<person_id>[0-9]+)/delete/', views.delete, name='delete'),
    url(r'^(?P<person_id>[0-9]+)/edit/', views.edit, name='edit'),
    url(r'^(?P<person_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.index, name='index'),
    url(r'^new_organization/', views.new_organization, name='new_organization'),
    url(r'^organization/(?P<organization_id>[0-9]+)/$', views.detail_organization, name='detail_organization'),
]


r'^contacts/'
