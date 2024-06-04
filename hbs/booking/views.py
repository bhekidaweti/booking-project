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
            subject = 'New Booking Created'
            message = f'A new booking has been made by {booking.name}.\n\n' \
                      f'Details:\n' \
                      f'Name: {booking.name}\n' \
                      f'Email: {booking.email}\n' \
                      f'Phone: {booking.phone_number}\n' \
                      f'Check-in: {booking.check_in}\n' \
                      f'Check-out: {booking.check_out}\n' \
                      f'Room type: {booking.room_type}\n' \
                      f'Number of guests: {booking.number_of_guests}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['admin_email@example.com']
            send_mail(subject, message, email_from, recipient_list)

            return redirect('index')
    else:
        form = BookingForm()
    return render(request, 'booking/form_template.html', {'form': form})