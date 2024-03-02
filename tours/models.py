from django.db import models
from django.contrib.auth.models import User

class TouristCompany(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='destination_images/')  # Path to upload destination images

    def __str__(self):
        return self.name

class Trip(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    tourist_company = models.ForeignKey(TouristCompany, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='trip_images/') 
    def __str__(self):
        return self.title

class Package(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.trip.title}"
