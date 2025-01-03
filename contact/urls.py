from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),

    # Contact: CRUD
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/', views.single_contact, name='read'),
    path('contact/<int:contact_id>/update/', views.single_contact, name='update'),
    path('contact/<int:contact_id>/delete/', views.single_contact, name='delete'),
]
