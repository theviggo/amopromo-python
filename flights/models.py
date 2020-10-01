from django.db import models


class Flights(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.TextField(null=False)
    lowest_price = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    distance = models.DecimalField(max_digits=9, decimal_places=3, null=False)
    aircraft_model = models.CharField(max_length=100, null=False)
    aircraft_manufacturer = models.CharField(max_length=100, null=False)
    price_per_km = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    departure_iata = models.CharField(max_length=3, null=False)
    arrival_iata = models.CharField(max_length=3, null=False)
    average_speed = models.FloatField(null=False)
    flight_duration = models.IntegerField(null=False)