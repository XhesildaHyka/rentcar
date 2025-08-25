from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import * 

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return ['home', 'about', 'contact']  # your static views names

    def location(self, item):
        return reverse(item)

class CarSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Rezerv.objects.all()

    def lastmod(self, obj):
        return obj.updated_at  # if you have a timestamp field
