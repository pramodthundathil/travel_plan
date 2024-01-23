from django.contrib import admin

from .models import Destination, Packages, Journey, Contry, TourGuids, TourGuideBooking, HotelBooking, PackageBooking, JournyBooking

admin.site.register(Destination)
admin.site.register(Packages)
admin.site.register(Journey)
admin.site.register(Contry)
admin.site.register(TourGuids)
admin.site.register(TourGuideBooking)
admin.site.register(HotelBooking)
admin.site.register(PackageBooking)
admin.site.register(JournyBooking)

