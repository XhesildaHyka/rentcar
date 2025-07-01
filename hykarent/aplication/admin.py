from django.contrib import admin
from .models import *


# Register your models here.
# admin.site.register(Rezerv)
admin.site.register(CarouselImage)
admin.site.register(Contact)
admin.site.register(Reservation)


class CarPhotoInline(admin.TabularInline):
    model = CarPhoto
    extra = 6
    max_num = 6

# class CarOptionInline(admin.TabularInline):
#     model = CarOption
#     extra = 1

class InsuranceOptionInline(admin.TabularInline):
    model = InsuranceOption
    extra = 1

class DeliveryLocationInline(admin.TabularInline):
    model = DeliveryLocation
    extra = 1

@admin.register(Rezerv)
class CarAdmin(admin.ModelAdmin):
    inlines = [CarPhotoInline, InsuranceOptionInline, DeliveryLocationInline]
    list_display = ['name', 'price', 'year']
