from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^resume/', views.resume, name='resume'),
    url(r'^transcript/', views.transcript, name='transcript'),
    url(r'^thesis/', views.thesis, name='thesis'),

    url('career/', views.career, name='career'),
    url('projects/', views.projects, name='projects'),
    url('contacts/', views.contacts, name='contacts'),
	url(r'^send_email/$', views.send_email, name='send_email'),
	url('email_sent/', views.email_sent, name='email_sent'),
	url('email_unsuccessful/', views.email_unsuccessful, name='email_unsuccessful'),
]