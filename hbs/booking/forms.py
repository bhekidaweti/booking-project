# bookings/forms.py

from django import forms
from .models import Booking
from datetime import date

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'check_in', 'check_out', 'room_type', 'number_of_guests']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'check_in': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'min': date.today().isoformat()}),
            'check_out': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'min': date.today().isoformat()}),
            'room_type': forms.Select(attrs={'class': 'form-control'}),
            'number_of_guests': forms.NumberInput(attrs={'class': 'form-control'}),
        }