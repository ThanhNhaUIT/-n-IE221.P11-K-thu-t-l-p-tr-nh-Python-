from django.db import models

# Create your models here.

# Model cho Hotel
# class Hotel(models.Model):
#     hotel_id = models.IntegerField(primary_key=True)  # Đặt hotel_id là khóa chính
#     hotel_name = models.CharField(max_length=200)
#     address = models.CharField(max_length=300)
#     phone_number = models.CharField(max_length=20)
#     email = models.EmailField()

#     class Meta:
#         db_table = 'Hotel'  # Tên bảng trong cơ sở dữ liệu
#         managed = False  # Django không quản lý bảng này

#     def __str__(self):
#         return self.hotel_name

# Model cho Room
# class Room(models.Model):
#     hotel = models.ForeignKey('management.Hotel', on_delete=models.CASCADE)
#     room_number = models.CharField(max_length=10)
#     room_type = models.CharField(max_length=50)
#     price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
#     capacity = models.IntegerField()
#     status = models.CharField(max_length=50)

#     def __str__(self):
#         return f"{self.room_type} - {self.room_number}"

# # Model cho Invoice
# class Invoice(models.Model):
#     booking = models.ForeignKey('customer.Booking', on_delete=models.CASCADE)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     invoice_date = models.DateField()

#     def __str__(self):
#         return f"Invoice #{self.id} - {self.booking}"

# # Model cho Payment
# class Payment(models.Model):
#     invoice = models.ForeignKey('management.Invoice', on_delete=models.CASCADE)
#     payment_date = models.DateField()
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     method = models.CharField(max_length=50)
#     payment_status = models.CharField(max_length=50)

#     def __str__(self):
#         return f"Payment for Invoice #{self.invoice.id}"