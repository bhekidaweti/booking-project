from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Booking
from .forms import BookingForm
from django.conf import settings

def index(request):
    return render(request, 'booking/index.html', {})

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            messages.success(request, 'Your booking was successful!')

            # Send email to admin
            send_mail(
                'New booking', 
                'You have a new booking',
                settings.DEFAULT_FROM_EMAIL,
                ['bheki.daweti@gmail.com'],
                fail_silently=False,
            )

            return redirect('index')
    else:
        form = BookingForm()
    return render(request, 'booking/form_template.html', {'form': form})