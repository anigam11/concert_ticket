from django.urls import path,  include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('concert/<str:concert_id>/', views.concert, name='concert'),
    path('bookticket/<str:concert_id>/', views.book_ticket, name='book_ticket'),

]