from django.contrib import admin
from .models import TouristCompany, Destination, Trip, Package

@admin.register(TouristCompany)
class TouristCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'destination', 'start_date', 'end_date', 'tourist_company')
    list_filter = ('destination', 'start_date', 'end_date', 'tourist_company')
    search_fields = ('title', 'description')

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'trip', 'price')
    list_filter = ('trip',)
