from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  #for the home page
    path('events/', views.event_list, name='event_list'),
    path('create/', views.create_event, name='create_event'),
    # path('event/<int:event_id>/', views.view_event, name='view_event'),
    path('register/<int:event_id>/', views.register_event, name='register_event'),
    path('cancel/<int:event_id>/', views.cancel_registration, name='cancel_registration'),
    path('calendar/', views.view_calendar, name='view_calendar'),
    path('about/', views.about, name='about'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
]
