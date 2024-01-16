from django.shortcuts import render,redirect
from .models import Destination, Contry, Packages, Journey, TourGuids, Restaurants, Hotels
from .forms import DestinationAddForm, ContryAddForm, PackageAddForm, PackageAddForm, JournyAddForm, GuideAddForm, HotelAddForm, RestaurentAddForm
from django.contrib import messages


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


    

