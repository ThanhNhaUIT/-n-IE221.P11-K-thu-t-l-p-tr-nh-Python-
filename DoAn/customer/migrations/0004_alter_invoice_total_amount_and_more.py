# Generated by Django 5.0.10 on 2024-12-09 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_hotel_hotel_image_room_room_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='total_amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='price_per_night',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('Phòng đơn', 'Phòng đơn'), ('Phòng đôi', 'Phòng đôi'), ('Phòng VIP', 'Phòng VIP')], max_length=50),
        ),
        migrations.AlterField(
            model_name='room',
            name='status',
            field=models.CharField(choices=[('Đã đặt', 'Đã đặt'), ('Trống', 'Trống')], max_length=50),
        ),
    ]
