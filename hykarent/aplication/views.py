from django.shortcuts import render, redirect
from .models import *  
from django.core.paginator import Paginator 
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Rezerv, Reservation  # assuming Reservation is your reservation model
from .forms import ReservationForm



def home(request):
    rent= Rezerv.objects.all()
    carousel_images = CarouselImage.objects.all()  
    arrivals = Rezerv.objects.filter(is_arrival=True)
    context = {
        'rent': rent,
        'carousel_images': carousel_images,
        'arrivals': arrivals, 
    }
    return render(request, 'home.html', context)

def rezervpage(request, id):
    # Get sort parameter from GET request
    sort_order = request.GET.get('sort', 'default')

    if sort_order == 'price_asc':
        rent = Rezerv.objects.all().order_by('price')  # Assuming 'price' is your field
    elif sort_order == 'price_desc':
        rent = Rezerv.objects.all().order_by('-price')
    else:
        rent = Rezerv.objects.all()  # Default order

    paginator = Paginator(rent, 8)  # Show 8 cars per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'sort_order': sort_order,  # So the template knows which option is selected
    }
    return render(request, 'rezervo.html', context)

def rezervpage_detail(request, pk):
    detailItem = get_object_or_404(Rezerv, pk=pk)
    form = ReservationForm()
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Check for overlapping reservations for this car
            overlapping = Reservation.objects.filter(
                car=detailItem,
                start_date__lte=end_date,
                end_date__gte=start_date
            )
            if overlapping.exists():
                messages.error(request, "This car is already reserved for the selected dates.")
            else:
                reservation = form.save(commit=False)
                reservation.car = detailItem
                reservation.save()
                messages.success(request, "Your reservation has been placed successfully!")
                return redirect('home')  # or wherever you want to redirect after booking
    
    context = {
        'detailItem': detailItem,
        'form': form
    }
    return render(request, 'rezervodetail.html', context)


def carousel_images(request):
    carousel_images = CarouselImage.objects.get()
    return render(request, 'home.html', {'carousel_images': carousel_images})



def contact(request):
    if request.method == "POST":
        first_name = request.POST.get("emri")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("sms")

        # Validate phone (le të pranojmë edhe numra me + dhe hapësira, nëse dëshiron, mund ta zgjerosh)
        if not phone or not phone.isdigit():
            messages.error(request, "Vendosni një numër telefoni të vlefshëm!")
            return render(request, "contactus.html", {
                "emri": first_name,
                "lastname": last_name,
                "email": email,
                "phone": phone,
                "sms": message
            })

        # Save contact
        Contact.objects.create(
            contact_name=first_name,
            contact_lastname=last_name,
            contact_email=email,
            contact_phone=phone,
            contact_sms=message
        )

        messages.success(request, "Mesazhi juaj u dërgua! Faleminderit për kontaktin!")
        return redirect('contactpage')  # redirect te faqja e kontaktit për të shmangur ridërgimin

    return render(request, "contactus.html")