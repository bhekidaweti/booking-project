from django.db import models

# Create your models here.
 
class Booking(models.Model):
    ROOM_TYPE_CHOICES = [
        ('suite', 'Suite'),
        ('junior', 'Junior Suite'),
        ('deluxe', 'Deluxe Room'),
        ('standard', 'Standard Room'),
        ('villa', 'Villa'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    check_in = models.DateField()
    check_out = models.DateField()
    room_type = models.CharField(max_length=10, choices=ROOM_TYPE_CHOICES)
    number_of_guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.room_type} from {self.check_in} to {self.check_out}"