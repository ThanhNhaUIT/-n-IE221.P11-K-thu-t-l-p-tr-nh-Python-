from django import forms
from .models import Booking, Invoice

class BookingForm(forms.ModelForm):
    booking_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    day_stay = forms.IntegerField(min_value=1)

    class Meta:
        model = Booking
        fields = ['booking_date', 'day_stay']

class InvoiceForm(forms.ModelForm):
    method = forms.CharField(max_length=100)

    class Meta:
        model = Invoice
        fields = ['method']
