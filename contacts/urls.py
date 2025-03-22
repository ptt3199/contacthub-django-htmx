from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/search/', views.search_contacts, name='search-contact'),
    path('contact/', views.create_contact, name='create-contact')
]
