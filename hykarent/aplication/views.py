from django.shortcuts import render, redirect
from .models import *  
from django.core.paginator import Paginator 
from django.contrib import messages




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

def rezervpage(request,id):
    rent = Rezerv.objects.get(pk=id) 
    rent= Rezerv.objects.all()  # Merr të gjitha makinat
    paginator = Paginator(rent, 8)  # Show 8 cars per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'rezervo.html', context)


def rezervpage_detail(request, pk):
    detailItem = Rezerv.objects.get(pk=pk)
    context = {
        'detailItem': detailItem,
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