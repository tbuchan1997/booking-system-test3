from django.db import models

# Create your models here.

class Slot(models.Model):
    date = models.DateField()
    time = models.TimeField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date} at {self.time}"

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    slot = models.OneToOneField(Slot, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking by {self.name} for {self.slot}"