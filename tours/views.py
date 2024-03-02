from django.shortcuts import render, get_object_or_404
from .models import Trip , Destination

def index(request):
    # Fetch some data, e.g., latest trips
    # latest_trips = Trip.objects.order_by('-start_date')[:5]
    latest_trips = Trip.objects.order_by('-id')[:5]
    context = {
        'latest_trips': latest_trips
    }
    return render(request, 'tours/index.html', context)

def trip_list(request):
    trips = Trip.objects.all()
    return render(request, 'tours/trip_list.html', {'trips': trips})


def destination_detail(request, destination_id):
    destination = get_object_or_404(Destination, pk=destination_id)
    context = {'destination': destination}
    return render(request, 'tours/destination_detail.html', context)




def trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    return render(request, 'tours/trip_detail.html', {'trip': trip})

def new_trip(request):
    # Logic for creating a new trip
    return render(request, 'tours/new_trip.html')
