from django import template
from tickets.models import *
register= template.Library()
@register.filter(name='seats_remaining')
def seats_remaining(value):
    concert = Concert.objects.get(id =  value)
    seats = 0
    for seat_type in concert.veneu.seat_types.all():
        seats += seat_type.number_of_seats
    Ticket_obj = Ticket.objects.filter(concert = concert)
    booked_seats = 0
    for ticket in Ticket_obj:
        booked_seats += ticket.no_of_seats
    total_seats_remain_unused = seats - concert.seats_to_be_used
    
    return (concert.seats_to_be_used - booked_seats)