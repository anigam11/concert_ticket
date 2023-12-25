from django.contrib import admin

# Register your models here.

from tickets.models import *

# Register your models here.
class SeatTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', 'number_of_seats', 'price')
admin.site.register(SeatType ,SeatTypeAdmin)


    
admin.site.register(Veneu)

class ConcertAdmin(admin.ModelAdmin):
    list_display = ('name', 'seats_to_be_used', 'date')
    def get_form(self, request, obj=None, **kwargs):
        form = super(ConcertAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['seats_to_be_used'].max_value = '1000'
        return form
admin.site.register(Concert ,ConcertAdmin)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('no_of_seats', 'price_paid')

admin.site.register(Ticket ,TicketAdmin)   
