from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

def default_image():
    return 'default.jpg'  

# class Rezerv(models.Model):
#     name = models.CharField(max_length=100, blank=True, null=True)
#     image = models.ImageField(upload_to='rezervpage/', blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     is_arrival = models.BooleanField(default=False,null=True, blank=True)

#     def __str__(self):
#         return f"{self.name}"
    


class Rezerv(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='rezervpage/', blank=True, null=True, default=default_image)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    guarantee_low_season = models.DecimalField(max_digits=6, decimal_places=2,blank=True, null=True)
    guarantee_high_season = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    seats = models.IntegerField(blank=True, null=True)
    transmission = models.CharField(max_length=50, blank=True, null=True)
    big_suitcases = models.IntegerField(blank=True, null=True)
    small_suitcases = models.IntegerField(blank=True, null=True)
    fuel_type = models.CharField(max_length=50,blank=True, null=True)
    engine_capacity = models.FloatField(blank=True, null=True)
    cancel_before_days = models.IntegerField(blank=True, null=True)
    min_days_low = models.IntegerField(blank=True, null=True)
    min_days_high = models.IntegerField(blank=True, null=True)
    notice_period = models.IntegerField(blank=True, null=True)
    deposit_required = models.BooleanField(default=False,blank=True, null=True)
    fuel_policy = models.CharField(max_length=100,blank=True, null=True)
    working_hours = models.CharField(max_length=100, blank=True, null=True)
    delivery_outside_hours = models.BooleanField(default=False,blank=True, null=True)
    cross_border_allowed = models.BooleanField(default=False,blank=True, null=True)
    cross_border_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0,blank=True, null=True)
    cross_border_km_limit = models.IntegerField(default=1000,blank=True, null=True)
    cross_border_assistance = models.BooleanField(default=False,blank=True, null=True)
    cross_border_assistance_fee = models.DecimalField(max_digits=6, decimal_places=2, default=0,blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_arrival = models.BooleanField(default=False,null=True, blank=True)
    # is_compact = models.BooleanField(default=False, null=True, blank=True)
    is_economy = models.BooleanField(default=False, null=True, blank=True)
    is_luxury = models.BooleanField(default=False, null=True, blank=True)
    is_suv = models.BooleanField(default=False, null=True, blank=True)
    is_bmv = models.BooleanField(default=False, null=True, blank=True)
    is_mercedes = models.BooleanField(default=False, null=True, blank=True)
    is_audi = models.BooleanField(default=False, null=True, blank=True)

    
    def __str__(self):
        return self.name

class CarPhoto(models.Model):
    car = models.ForeignKey(Rezerv, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_photos/',blank=False, null=False, default=default_image)

    def __str__(self):
        return f"Photo for {self.car.name}"

class CarOption(models.Model):
    car = models.ForeignKey(Rezerv, related_name='options', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price_per_day = models.DecimalField(max_digits=6, decimal_places=2, default=0)

class InsuranceOption(models.Model):
    car = models.ForeignKey(Rezerv, related_name='insurance_options', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price_per_day = models.DecimalField(max_digits=6, decimal_places=2)

# class DeliveryLocation(models.Model):
#     car = models.ForeignKey(Rezerv, related_name='delivery_locations', on_delete=models.CASCADE)
#     location = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=6, decimal_places=2)

class CarouselImage(models.Model):
    image1 = models.ImageField(upload_to='carousel_images/', blank=True, null=True, default=default_image)
    image = models.ImageField(upload_to='carousel_images/', blank=True, null=True, default=default_image)
    image3 = models.ImageField(upload_to='carousel_images/', blank=True, null=True, default=default_image)


class Reservation(models.Model):
    car = models.ForeignKey(Rezerv, on_delete=models.CASCADE, related_name='reservations')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    pickup_location = models.CharField(max_length=255, blank=True, null=True)
    dropoff_location = models.CharField(max_length=255, blank=True, null=True)
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
