from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rezervpage/<int:id>/', views.rezervpage, name='rezervpage'),
    path('rezervpage_detail/<int:pk>/', views.rezervpage_detail, name='detailItem'),
    # path('adminpage/', views.admin_page, name='admin_page'),
    path("carousel_images/", views.carousel_images, name="carousel_images"),
    path("contact/", views.contact, name="contactpage"),
    path('search/', views.search, name='search'),
    path('rezervimi-sukses/<int:reservation_id>/', views.reservation_success, name='reservation_success'),
    path("detail/<int:id>", views.detail, name="detailpage"),
    path("audi/", views.audi, name="audi"),
    path("mercedes/", views.mercedes, name="mercedes"), 
    path("bmv/", views.bmv, name="bmv"),
    path("suv/", views.suv, name="suv"),
    # path("compact/", views.compact, name="compact"),
    path("economy/", views.economy, name="economy"),
    path("luxury/", views.luxury, name="luxury"),
    path("about/", views.about, name="about"),
    
]
