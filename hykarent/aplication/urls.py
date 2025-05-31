from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rezervpage/<int:id>/', views.rezervpage, name='rezervpage'),
    path('rezervpage_detail/<int:pk>/', views.rezervpage_detail, name='detailItem'),
    # path('adminpage/', views.admin_page, name='admin_page'),
     path("carousel_images/", views.carousel_images, name="carousel_images"),
    path("contact/", views.contact, name="contactpage"),
]
