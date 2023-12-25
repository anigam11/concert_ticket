from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render,redirect

from .models import *
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method== 'POST':
        fullname= request.POST.get('name')
        username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('password')
        if User.objects.filter(username=username):
            return redirect('/register')
        user_obj= User(username=username, email=email, first_name= fullname) 
        user_obj.set_password(password)
        user_obj.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        
        return redirect('/')
    return render(request, 'user/signup.html')
def loginUser(request):
        if request.user.is_authenticated:
            return redirect('/')
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            try:
                user = User.objects.get(username=username)
            except:
                 return redirect('/login')
            if user:

                username = user.username
                user = authenticate(request, username=username, password=password) # check password

            if user is not None:
                login(request, user)
                return redirect('/')	
            
        return render(request,'user/login.html',)

def logoutUser(request):
        logout(request)
        return redirect('/')

def home(request):
    concert_obj = Concert.objects.all()
    print(concert_obj)
    context = {'concerts': concert_obj}
    return render(request, 'tickets/index.html', context)


def concert(request, concert_id):
    print('**********', concert_id)
    concert_obj = Concert.objects.get(id = concert_id)
    context = {'concert': concert_obj}
    return render(request, 'tickets/concert.html', context)

def book_ticket(request, concert_id):
    if request.method == 'POST':
        seat_type = request.POST.get('seat_type_selected')
        number_of_seats = request.POST.get('number_of_seats')
        card_number = request.POST.get('card_number')
        concert_obj = Concert.objects.get(id = concert_id)
        print(seat_type)
        print(card_number)
        print(number_of_seats)
        seat_type_obj = SeatType.objects.get(id=seat_type)
        total_price = float(seat_type_obj.price) * int(number_of_seats)
        ticket_obj = Ticket.objects.create(user = request.user, concert = concert_obj, seat_type = seat_type_obj, no_of_seats = number_of_seats , price_paid = total_price, card_number = card_number )
        context = {'message': 'Successfully Ticket booked'}
            
    return redirect('/', context)