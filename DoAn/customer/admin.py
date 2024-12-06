from django.contrib import admin

# Register your models here.


from management.models import Hotel  # Import từ app management

admin.site.register(Hotel)  # Đăng ký model Hotel vào trang admin
