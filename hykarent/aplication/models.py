from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

def default_image():
    return 'default.jpg'  

class Rezerv(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='rezervpage/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_arrival = models.BooleanField(default=False,null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
class CarouselImage(models.Model):
    image1 = models.ImageField(upload_to='carousel_images/', blank=True, null=True, default=default_image)
    image = models.ImageField(upload_to='carousel_images/', blank=True, null=True, default=default_image)
    image3 = models.ImageField(upload_to='carousel_images/', blank=True, null=True, default=default_image)


class Reservation(models.Model):
    car = models.ForeignKey(Rezerv, on_delete=models.CASCADE, related_name='reservations')
    name = models.CharField(max_length=100)  # User name or can be linked to User model
    phone = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation for {self.car.name} by {self.name} from {self.start_date} to {self.end_date}"

class Contact(models.Model):
    contact_name = models.CharField(max_length=50,null=True, blank=True)
    contact_lastname = models.CharField(max_length=50,null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_sms= models.TextField(max_length=500, null=True, blank=True)
    # contact_phone = models.IntegerField(max_length=50,null=True, blank=True)
    contact_phone = PhoneNumberField(null=True, blank=True)
    
    def __str__(self):
            return f"{self.contact_name} {self.contact_lastname}"