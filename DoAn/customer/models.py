from django.db import models

# Create your models here.
    
from django.contrib.auth.models import User
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.SET_NULL, null=True, blank= False)
    customer_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, null =True)

    def __str__(self):
        return self.customer_name


class Hotel(models.Model):
    hotel_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    hotel_image = models.ImageField(null=True,blank=False)
    
    def __str__(self):
        return self.hotel_name
    
    # Trả về url của hình nếu đc, không thì trả về rỗng
    @property
    def ImageURL(self):
        try:
            url = self.hotel_image.url
        except :
            url = ''
        return url

class Room(models.Model):
    # Các loại phòng cố định (ví dụ: Phòng đơn, Phòng đôi, Phòng VIP)
    ROOM_TYPES = [
        ('Phòng đơn', 'Phòng đơn'),
        ('Phòng đôi', 'Phòng đôi'),
        ('Phòng VIP', 'Phòng VIP'),
    ]

    # Trạng thái của phòng (Đã đặt hoặc Trống)
    ROOM_STATUSES = [
        ('Đã đặt', 'Đã đặt'),
        ('Trống', 'Trống'),
    ]

    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, blank=False)
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)
    price_per_night = models.IntegerField()
    capacity = models.IntegerField()
    status = models.CharField(max_length=50, choices=ROOM_STATUSES)
    room_image = models.ImageField(null=True, blank=False)

    def __str__(self):
        return f"{self.room_type} - {self.room_number}"

    @property
    def ImageURL(self):
        try:
            url = self.room_image.url
        except :
            url = ''
        return url
    def is_booked(self):
        return Booking.objects.filter(room_number=self, complete=False).exists()
class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,  null=True, blank= False)
    hotel_name = models.ForeignKey(Hotel, on_delete=models.SET_NULL,  null=True, blank= False)
    room_number = models.ForeignKey(Room, on_delete=models.SET_NULL,  null=True, blank= False)
    booking_date = models.DateField()
    day_stay = models.IntegerField()

class Invoice(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL,  null=True, blank= False)
    total_amount = models.IntegerField()
    invoice_date = models.DateField()
    method = models.CharField(max_length=100)
    status = models.CharField( max_length=100)

    def __str__(self):
        return f"Invoice #{self.id} - {self.booking}"

