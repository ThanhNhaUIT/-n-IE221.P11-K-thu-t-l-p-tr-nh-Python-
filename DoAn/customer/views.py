from django.shortcuts import render

# Create your views here.


from management.models import Hotel  # Import từ app management

def hotel_list(request):
    hotels = Hotel.objects.all().values('hotel_name', 'address', 'phone_number', 'email')
    return render(request, 'hotel_list.html', {'hotels': hotels})



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
    return render(request, 'booking_list.html')

# DoAn/customer/views.py
from django.contrib.auth import views as auth_views

def login_view(request):
    return auth_views.LoginView.as_view(template_name='login.html')(request)


# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.http import HttpResponse

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         birthdate = request.POST['birthdate']
#         phone_number = request.POST['phone_number']
#         email = request.POST['email']
#         password = request.POST['password']
        
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('customer:home')
#         else:
#             return HttpResponse('Lỗi đăng nhập, vui lòng thử lại.')
#     else:
#         return render(request, 'login.html')


# customer/views.py

# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib import messages

# def register(request):
#     if request.method == "POST":
#         name = request.POST['name']
#         dob = request.POST['dob']
#         phone_number = request.POST['phone_number']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']
        
#         if password == confirm_password:
#             # Tạo người dùng mới
#             user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
#             user.save()
#             messages.success(request, 'Đăng ký thành công!')
#             return redirect('login')
#         else:
#             messages.error(request, 'Mật khẩu xác nhận không đúng.')
    
#     return render(request, 'register.html')

def register(request):
    return render(request, 'register.html')
