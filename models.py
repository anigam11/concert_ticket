from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SeatType(models.Model):
    type_name = models.CharField(max_length=255)
    number_of_seats = models.IntegerField()
    price = models.IntegerField()
    def __str__(self) :
        return self.type_name
class Veneu(models.Model):
    name = models.CharField(max_length=255)
    seat_types = models.ManyToManyField(SeatType)
    def __str__(self) :
        return self.name
class Concert(models.Model):
    name = models.CharField(max_length=255)
    veneu = models.ForeignKey(Veneu, on_delete=models.CASCADE)
    seats_to_be_used = models.IntegerField()
    date = models.DateTimeField(null=True, blank=True)
    def __str__(self) :
        return self.name

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    seat_type = models.ForeignKey(SeatType, on_delete=models.CASCADE)
    no_of_seats = models.IntegerField()
    price_paid = models.IntegerField()
    card_number = models.CharField(max_length=255)
