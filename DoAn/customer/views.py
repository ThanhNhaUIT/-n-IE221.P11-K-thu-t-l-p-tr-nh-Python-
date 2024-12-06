from django.shortcuts import render

# Create your views here.

# Này để thêm 
from management.models import Hotel  # Import từ app management

def hotel_list(request):
    hotels = Hotel.objects.all().values('hotel_name', 'address', 'phone_number', 'email')
    return render(request, 'hotel_list.html', {'hotels': hotels})
