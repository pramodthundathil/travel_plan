from django.contrib import admin

from .models import Destination, Packages, Journey, Contry

admin.site.register(Destination)
admin.site.register(Packages)
admin.site.register(Journey)
admin.site.register(Contry)
