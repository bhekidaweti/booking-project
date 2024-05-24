from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking
from .forms import BookingForm



def index(request):
    return render(request, 'booking/index.html',{})

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking/booking_list.html', {'bookings': bookings})


def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your booking was successful!')
            return redirect('index')
    else:
        form = BookingForm()
    return render(request, 'booking/form_template.html', {'form': form})
