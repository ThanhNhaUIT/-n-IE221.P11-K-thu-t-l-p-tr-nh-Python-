from django.shortcuts import render

# Create your views here.


from .models import *  # Import từ app management

def hotel_list(request):
    hotels = Hotel.objects.all()
    context = {'hotels': hotels}
    return render(request, 'hotel_list.html', context)



def home(request):
    return render(request, 'home.html')

def policy(request):
    return render(request, 'policy.html')

def about(request):
    return render(request, 'about.html')

# def booking_list(request):
#     bookings = Booking.objects.filter(user=request.user)
#     return render(request, 'customer/booking_list.html', {'bookings': bookings})

def booking_list(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        bookings = Booking.objects.filter(customer=customer)  # Fetch all active bookings for the customer
        context = {'bookings': bookings}
    else:
        context = {'bookings': []}  # If the user is not authenticated, show an empty list

    return render(request, 'booking_list.html', context)

# DoAn/customer/views.py
from django.contrib.auth import views as auth_views

def login_view(request):
    return auth_views.LoginView.as_view(template_name='login.html')(request)

def register(request):
    return render(request, 'register.html')


from django.shortcuts import render, get_object_or_404
from .models import Hotel, Room
def room_list(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)  # Fetch the selected hotel
    rooms = Room.objects.filter(hotel=hotel)  # Filter rooms by hotel
    context = {
        'hotel': hotel,
        'rooms': rooms,
    }
    return render(request, 'room_list.html', context)


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Booking, Invoice, Room
from .forms import BookingForm, InvoiceForm
from django.utils import timezone

@login_required
def book_room(request, room_id):
    room = Room.objects.get(id=room_id)

    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        invoice_form = InvoiceForm(request.POST)

        if booking_form.is_valid() and invoice_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.customer = request.user.customer
            booking.room_number = room
            booking.hotel_name = room.hotel  # Save the hotel's name with the booking
            booking.booking_date = timezone.now()
            booking.day_stay = booking_form.cleaned_data['day_stay']

            # Calculate total amount
            total_amount = booking.day_stay * room.price_per_night

            invoice = invoice_form.save(commit=False)
            invoice.booking = booking
            invoice.total_amount = total_amount
            invoice.invoice_date = timezone.now()  # Automatically set the invoice date

            # Save both the booking and the invoice
            booking.save()
            invoice.save()

            return redirect('customer:booking_list')  # Redirect to the booking list after successful booking

    else:
        booking_form = BookingForm()
        invoice_form = InvoiceForm()

    return render(request, 'book_room.html', {
        'room': room,
        'booking_form': booking_form,
        'invoice_form': invoice_form
    })
