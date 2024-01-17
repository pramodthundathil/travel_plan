from django.shortcuts import render,redirect
from .models import Destination, Contry, Packages, Journey, TourGuids, Restaurants, Hotels, PackageBooking, JournyBooking, TourGuideBooking, HotelBooking
from .forms import DestinationAddForm, ContryAddForm, PackageAddForm, PackageAddForm, JournyAddForm, GuideAddForm, HotelAddForm, RestaurentAddForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def DestinationHome(request):
    desti = Destination.objects.all()
    paki = Packages.objects.all()
    jour = Journey.objects.all()


    form = DestinationAddForm()
    form2 = ContryAddForm()
    if request.method == "POST":
        form = DestinationAddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Destination Saved")
            return redirect("DestinationHome")
        else:
            messages.info(request,"Form Data not valid")
            return redirect("DestinationHome")

    context = {
        "form":form,
        "form2":form2,
        "desti":desti,
        "lenpaki":len(paki),
        "noofdesti":len(desti),
        "lenjour":len(jour),

    }
    return render(request, "destinations.html",context)

def AddContry(request):
    if request.method == "POST":
        form = ContryAddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Contry Saved")
            return redirect("DestinationHome")
        else:
            messages.info(request,"Form Data not valid")
            return redirect("DestinationHome")


    return redirect("DestinationHome")


def PackageHome(request):
    desti = Destination.objects.all()
    paki = Packages.objects.all()
    jour = Journey.objects.all()


    form = PackageAddForm()
    if request.method == "POST":
        form = PackageAddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Package is Saved")
            return redirect("PackageHome")
        else:
            messages.info(request,"Form Data not valid")
            return redirect("PackageHome")
        
    context = {
        "noofdesti":len(desti),
        "form":PackageAddForm(),
        "lenpaki":len(paki),
        "paki":paki,
        "lenjour":len(jour),

    }
    return render(request,"tourpackages.html",context)

def RouteHome(request):
    desti = Destination.objects.all()
    paki = Packages.objects.all()
    form = JournyAddForm()
    jour = Journey.objects.all()

    if request.method == "POST":
        form = JournyAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Route is Saved")
            return redirect("RouteHome")
        else:
            messages.info(request,"Form Data not valid")
            return redirect("RouteHome")

    context = {
        "noofdesti":len(desti),
        "lenpaki":len(paki),
        "jour":jour,
        "lenjour":len(jour),
        "form":form,
    }
    return render(request, "routes.html",context)

def DeleteRoute(request,pk):
    Journey.objects.get(id = pk).delete()
    messages.info(request,"Route Deleted")

    return redirect("RouteHome")

def DeleteDestination(request,pk):
    Destination.objects.get(id = pk).delete()
    messages.info(request,"destination Deleted")

    return redirect("DestinationHome")


def DeletePackage(request,pk):
    Packages().objects.get(id = pk).delete()
    messages.info(request,"package Deleted")

    return redirect("PackageHome")

def Services(request):
    form = GuideAddForm()
    form2 = HotelAddForm()
    form3 = RestaurentAddForm()
    desti = Destination.objects.all()
    paki = Packages.objects.all()
    jour = Journey.objects.all()
    guids = TourGuids.objects.all()
    rest = Restaurants.objects.all()
    hotel = Hotels.objects.all()
    context = {
        "form":form,
        "form2":form2,
        "form3":form3,
        "noofdesti":len(desti),
        "lenpaki":len(paki),
        "lenjour":len(jour),
        "guids":guids,
        "rest":rest,
        "hotel":hotel
    }
    return render(request, "services.html",context)

def HotelAdd(request):
    if request.method == "POST":
        form = HotelAddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"Hotel Addedd")
            return redirect("Services")
    return redirect("Services")


def RestaurentAdd(request):
    if request.method == "POST":
        form = RestaurentAddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"Restaurent Addedd")
            return redirect("Services")
    return redirect("Services")



def GuideAdd(request):
    if request.method == "POST":
        form = GuideAddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request,"Guide Addedd")
            return redirect("Services")
    return redirect("Services")
    

def DeleteHotel(request,pk):
    Hotels.objects.get(id = pk).delete()
    messages.info(request,"Hotel Deleted")

    return redirect("Services")


def DeleteGuide(request,pk):
    TourGuids.objects.get(id = pk).delete()
    messages.info(request,"Guide Deleted")

    return redirect("Services")


def DeleteRestarent(request,pk):
    Restaurants.objects.get(id = pk).delete()
    messages.info(request,"Restaurent Deleted")

    return redirect("Services")



# bookings 
def BookingConfirm(request):
    return render(request, "bookingconfirm.html")

@login_required(login_url="SignIn")
def BookPackage(request,pk):
    package = Packages.objects.get(id = pk)
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        date = request.POST["date"]
        booking = PackageBooking.objects.create(package = package,user = request.user,booker_Name = name, booker_phone = phone, booker_address = address, booking_date = date, status = "Package Booked" )
        booking.save()
        return redirect("BookingConfirm")
    context = {
        "package":package
    }

    return render(request, "bookpackage.html",context)

@login_required(login_url="SignIn")
def BookGuide(request,pk):
    guide = TourGuids.objects.get(id = pk)

    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        date = request.POST["date"]
        booking = TourGuideBooking.objects.create(guide = guide,user = request.user,booker_Name = name, booker_phone = phone, booker_address = address, booking_date = date, status = "Guide Booked" )
        booking.save()
        return redirect("BookingConfirm")

    context = {
        "guide":guide
    }
    return render(request, "bookguide.html",context)


@login_required(login_url="SignIn")
def BookJourny(request,pk):
    journy = Journey.objects.get(id = pk)

    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        date = request.POST["date"]
        booking = JournyBooking.objects.create(journy = journy,user = request.user,booker_Name = name, booker_phone = phone, booker_address = address, booking_date = date, status = "Guide Booked" )
        booking.save()
        return redirect("BookingConfirm")

    context = {
        "journy":journy
    }
    
    return render(request, "booktransportation.html",context)
    

@login_required(login_url="SignIn")
def BookHotel(request,pk):
    hotel = Hotels.objects.get(id= pk)

    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        date = request.POST["date"]
        booking = HotelBooking.objects.create(Hotel = hotel,user = request.user,booker_Name = name, booker_phone = phone, booker_address = address, booking_date = date, status = "Hotel Booked" )
        booking.save()
        return redirect("BookingConfirm")

    context = {
        "hotel":hotel
    }
    
    return render(request, "bookhotel.html",context)


@login_required(login_url="SignIn")
def Mybookings(request):
    hotel = HotelBooking.objects.filter(user = request.user)
    package = PackageBooking.objects.filter(user = request.user)
    guid =  TourGuideBooking.objects.filter(user = request.user)
    route = JournyBooking.objects.filter(user = request.user)

    context = {
        "hotel":hotel,
        "package":package,
        "guid":guid,
        "route":route
    }

    return render(request, "mybookins.html",context)


@login_required(login_url="SignIn")
def Bookings(request):
    hotel = HotelBooking.objects.all()
    package = PackageBooking.objects.all()
    guid =  TourGuideBooking.objects.all()
    route = JournyBooking.objects.all()

    context = {
        "hotel":hotel,
        "package":package,
        "guid":guid,
        "route":route
    }

    return render(request, "bookings.html",context)


def deleteHotelBooking(request,pk):
    HotelBooking.objects.get(id = pk).delete()
    return redirect("Index")

def deleteGuideBooking(request,pk):
    TourGuideBooking.objects.get(id = pk).delete()
    return redirect("Index")

def deleteJournyBooking(request,pk):
    JournyBooking.objects.get(id = pk).delete()
    return redirect("Index")

def deletePackageBooking(request,pk):
    PackageBooking.objects.get(id = pk).delete()
    return redirect("Index")


def Search(request):
    if request.method == "POST":
        search = request.POST["search"]
        desti = Destination.objects.filter(destination_name__contains = search)

        context = {
            "desti":desti
        }

        return render(request,"search.html",context)



    
