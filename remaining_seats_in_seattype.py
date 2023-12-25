from django import template
from tickets.models import *
register= template.Library()
@register.filter(name='remaining_seats_in_seattype')
def remaining_seats_in_seattype(seattype_id, concert_id):
    concert = Concert.objects.get(id =  concert_id)
    seat_type_obj = SeatType.objects.get(id = seattype_id)
    
    number_of_seat_type = 0
    for seat_type in concert.veneu.seat_types.all():
        number_of_seat_type += 1
    Ticket_obj = Ticket.objects.filter(concert = concert,seat_type = seat_type_obj )
    booked_seats = 0
    for ticket in Ticket_obj:
        booked_seats += ticket.no_of_seats
    useable_seats = int(concert.seats_to_be_used) / int(number_of_seat_type)
    return (int(useable_seats - booked_seats))