from django.db import models
from django.contrib.auth.models import User


class Contry(models.Model):
    country_name = models.CharField(max_length=255)
    contry_image = models.FileField(upload_to="Contry_image")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.country_name


class Destination(models.Model):
    destination_name = models.CharField(max_length=255)
    key_words = models.CharField(max_length=255)
    image = models.FileField(upload_to="destination_image")
    place = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    contry = models.ForeignKey(Contry, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    attractions = models.CharField(max_length=1000)
    address = models.TextField(max_length=1000)
    postel_code = models.IntegerField()

    def __str__(self):
        return self.destination_name

class Packages(models.Model):
    destination = models.ForeignKey(Destination, on_delete = models.CASCADE)
    key_words = models.CharField(max_length=255)
    image = models.FileField(upload_to="package_image")
    number_of_days = models.IntegerField()
    number_of_nights = models.IntegerField()
    number_of_persons = models.IntegerField()
    amount = models.FloatField()
    description = models.CharField(max_length=1000)
    raings = models.IntegerField(null=True,blank=True)
    number_of_rators = models.IntegerField(null=True,blank=True)


class Journey(models.Model):
    options = (("air","air"),("train","train"),("bus","bus"),("other","other"))
    staring_from = models.CharField(max_length=255)
    straing_time = models.TimeField()
    destination = models.CharField(max_length=255)
    destination_include = models.ForeignKey(Destination, on_delete=models.SET_NULL,null=True,blank=True)
    ending_time = models.TimeField()
    Time_Taken_toTravel_in_Hours = models.FloatField()
    mode_of_travel = models.CharField(max_length=255, choices=options)
    cost = models.IntegerField()
    total_Kilomeaters = models.FloatField()


class Hotels(models.Model):

    options = (("single","single"),("double","double"),("suite","suite"),("dormetory","dormetory"))
    Hotel_Name = models.CharField(max_length=255)
    Room_Category = models.CharField(max_length=255,choices=options)
    Address = models.CharField(max_length=255)
    Destination_Near = models.ForeignKey(Destination, on_delete=models.SET_NULL,null=True,blank=True)
    Aminities = models.CharField(max_length=255)
    Price = models.FloatField()
    Hotel_pic = models.FileField(upload_to="Rest_pic") 
    availability = models.BooleanField(default=True)


class Restaurants(models.Model):
    Restaurants_Name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Destination_Near = models.ForeignKey(Destination, on_delete=models.SET_NULL,null=True,blank=True)
    Diat_and_menu = models.CharField(max_length=1000)
    Restaurent_pic = models.FileField(upload_to="Rest_pic") 

class TourGuids(models.Model):
    Guid_Name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    Phone = models.IntegerField()
    Destination_Near = models.ForeignKey(Destination, on_delete=models.SET_NULL,null=True,blank=True)
    Service = models.CharField(max_length=1000)
    Guide_pic = models.FileField(upload_to="Guide_pic") 



class PackageBooking(models.Model):
    package = models.ForeignKey(Packages, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    booker_Name = models.CharField(max_length=255,null=True)
    booker_phone = models.CharField(max_length=255,null=True)
    booker_address = models.CharField(max_length=255,null=True)
    booking_date = models.DateField(auto_now_add=False,null=True)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=255)

class TourGuideBooking(models.Model):
    guide = models.ForeignKey(TourGuids, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    booker_Name = models.CharField(max_length=255,null=True)
    booker_phone = models.CharField(max_length=255,null=True)
    booker_address = models.CharField(max_length=255,null=True)
    booking_date = models.DateField(auto_now_add=False,null=True)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=255)

class JournyBooking(models.Model):
    journy = models.ForeignKey(Journey, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    booker_Name = models.CharField(max_length=255,null=True)
    booker_phone = models.CharField(max_length=255,null=True)
    booker_address = models.CharField(max_length=255,null=True)
    booking_date = models.DateField(auto_now_add=False,null=True)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=255)



class HotelBooking(models.Model):
    Hotel = models.ForeignKey(Hotels, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    booker_Name = models.CharField(max_length=255)
    booker_phone = models.CharField(max_length=255)
    booker_address = models.CharField(max_length=255)
    booking_date = models.DateField(auto_now_add=False)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=255)





    