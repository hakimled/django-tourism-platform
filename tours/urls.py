from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trips/', views.trip_list, name='trip_list'),
    path('destinations/<int:destination_id>/', views.destination_detail, name='destination_detail'),
    path('trip/<int:trip_id>/', views.trip_detail, name='trip_detail'),
    path('trip/new/', views.new_trip, name='new_trip'),
    # Add more URL patterns as needed
]
