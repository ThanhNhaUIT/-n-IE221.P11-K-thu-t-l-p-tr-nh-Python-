from django.db import models

# Create your models here.

# Model cho Customer
class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.customer_name

# Model cho Booking
class Booking(models.Model):
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    hotel_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    booking_date = models.DateField()
    checkin_date = models.DateField()
    day_stay = models.IntegerField()

    def __str__(self):
        return f"Booking for {self.customer.customer_name} - {self.hotel_name}"