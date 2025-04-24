from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This should be for the home page
    path('events/', views.event_list, name='event_list'),  # Changed to avoid conflict
    path('create/', views.create_event, name='create_event'),
    path('event/<int:event_id>/', views.view_event, name='view_event'),
    path('register/<int:event_id>/', views.register_event, name='register_event'),
    path('cancel/<int:event_id>/', views.cancel_registration, name='cancel_registration'),
    path('calendar/', views.view_calendar, name='view_calendar'),
]
