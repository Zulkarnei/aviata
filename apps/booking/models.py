from django.db import models


class Booking(models.Model):
    refundable = models.BooleanField(blank=True, null=True)
    validating_airline = models.CharField(max_length=255, blank=True, null=True)


class Flight(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)


class Segment(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, blank=True, null=True)
    operating_airline = models.CharField(max_length=255, blank=True, null=True)
    marketing_airline = models.CharField(max_length=255, blank=True, null=True)
    flight_number = models.IntegerField(blank=True, null=True)
    equipment = models.CharField(max_length=255, blank=True, null=True)
    dep = models.JSONField(encoder=None, decoder=None)
    arr = models.JSONField(encoder=None, decoder=None)
    baggage = models.CharField(max_length=255, blank=True, null=True)


class Price(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, blank=True, null=True) # solve throug
    total = models.FloatField(blank=True, null=True)
    base = models.FloatField(blank=True, null=True)
    taxes = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=255, blank=True, null=True)
