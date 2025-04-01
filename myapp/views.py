from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.hashers import make_password, check_password
from myapp.models import Booking
from django.contrib import messages
from .models import signup

# Create your views here.
def contact(request):
    return render(request,'contact.html')

def booking(request):
    return render(request,'booking.html')

def entertainment(request):
    return render(request,'entertainment.html')

def food(request):
    return render(request,'food.html')

def visiting(request):
    return render(request,'visiting.html')

def hotels(request):
    return render(request,'hotels.html')

def home(request):
    if not request.session.get('username'):  # Check if user is logged in
        return redirect("/index/")
    return render(request, 'home.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = signup.objects.filter(username=username).first()  # Get user by username only

        if user and check_password(password, user.password):  # Check password securely
            request.session['username'] = user.username  # Store session
            messages.success(request, "Login successful!")
            return redirect("/home/")
        else:
            messages.error(request, "Invalid username or password!")  # Show error
            return redirect("/index/")

    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if signup.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect("/index")

        hashed_password = make_password(password)  # Hash the password
        new_user = signup(username=username, password=make_password(password)) 
        new_user.save()
        
        messages.success(request, "Account created successfully! Please log in.")
        return redirect("/index/")

    return render(request, 'index.html')

def logout_view(request):
    request.session.flush()  # Clear session
    return redirect("/index/")

def booking(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        aadhaar = request.POST.get('aadhaar')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        travel_date = request.POST.get('date')
        destination = request.POST.get('destination')
        payment_method = request.POST.get('peyment')  # Corrected spelling

        # Save the data in the database
        Booking.objects.create(
            name=name,
            age=age,
            aadhaar=aadhaar,
            phone=phone,
            email=email,
            travel_date=travel_date,
            destination=destination,
            payment_method=payment_method
        )

        messages.success(request, "Your booking has been submitted successfully!")
        return redirect('/booking/')

    return render(request, 'booking.html')
