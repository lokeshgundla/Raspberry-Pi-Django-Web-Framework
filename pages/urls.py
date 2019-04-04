from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
	path('contact_lg/', views.contact_lg, name='contact_lg'),
	path('contact_lb/', views.contact_lb, name='contact_lb'),
	path('contact_n/', views.contact_n, name='contact_n'),




    
]
