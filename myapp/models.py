from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.

class signup(models.Model):
    username = models.CharField(max_length=122, unique=True)
    password = models.CharField(max_length=255)
    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):  # Avoid rehashing
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    
class Booking(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    aadhaar = models.CharField(max_length=12, unique=True)  # Ensure unique Aadhaar
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    travel_date = models.DateField()
    destination = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.destination}"