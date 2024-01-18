from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import UserAddForm
from django.contrib.auth.models import User,Group
from .decorators import admin_only,NullGroup
from Destinations.models import Destination, Contry, Packages, Journey, Hotels, TourGuids, Restaurants

from .decorators import admin_only

#homepage functions  

@admin_only
def Index(request):
    desti = Destination.objects.all()
    contry = Contry.objects.all()
    paki = Packages.objects.all()
    jour = Journey.objects.all()
    guids = TourGuids.objects.all()



    context = {
        "desti":desti[:6],
        "contry":contry[:7],
        "paki":paki,
        "lenjour":len(jour),
        "guids":guids

    }
    return render(request,"index.html",context)

@admin_only
def IndexOne(request):
    return render(request,"indexone.html")


def AdminHome(request):
    desti = Destination.objects.all()
    paki = Packages.objects.all()
    jour = Journey.objects.all()



    context = {
        "desti":desti[:6],
        "noofdesti":len(desti),
        "lenpaki":len(paki),
        "paki":paki[:6],
        "lenjour":len(jour),


    }
    return render(request,"adminindex.html",context)


# Authetication functions 

def SignIn(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pswd']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            
            request.session['username'] = username
            request.session['password'] = password
            login(request, user1)
            return redirect('IndexOne')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('SignIn')
    return render(request,"login.html")

def SignUp(request):
    form = UserAddForm()
    if request.method == "POST":
        fname = request.POST["fname"]
        email = request.POST["email"]
        uname = request.POST["uname"]
        pswd = request.POST["pswd"]
        pswd1 = request.POST["pswd1"]

        if pswd != pswd1:
            messages.info(request,"Password Do not Matches..")
            return redirect("SignUp")
        if User.objects.filter(username = uname).exists():
            messages.info(request,"Username alredy exists user another username")
            return redirect("SignUp")
        if User.objects.filter(email = email).exists():
            messages.info(request,"Email alredy exists user another email")
            return redirect("SignUp")
        else:
            user = User.objects.create_user(first_name=fname, email=email, username=uname, password = pswd)
            user.save()
            group = Group.objects.get(name='user')
            user.groups.add(group)
            messages.success(request,"User Created.. Please Login....")
            return redirect("SignIn")




        # form = UserAddForm(request.POST)
        # if form.is_valid():
        #     username = form.cleaned_data.get('username')
        #     email = form.cleaned_data.get("email")
        #     if User.objects.filter(username = username).exists():
        #         messages.info(request,"Username Exists")
        #         return redirect('SignUp')
        #     if User.objects.filter(email = email).exists():
        #         messages.info(request,"Email Exists")
        #         return redirect('SignUp')
        #     else:
        #         new_user = form.save()
        #         new_user.save()
                
                # group = Group.objects.get(name='user')
                # new_user.groups.add(group) 
                
                
            
    return render(request,"register.html",{"form":form})



def SignOut(request):
    logout(request)
    return redirect('IndexOne')



# Home Designs


def OnContryClick(request,pk):
    contry = Contry.objects.get(id=pk)
    desti = Destination.objects.filter(contry = contry)
    paki = []
    for i in desti:
        p = Packages.objects.filter(destination = i)
        for j in p: 
            paki.append(j)
        


    context = {
        "desti":desti,
        "paki":paki
    }
    
    return render(request, "oncontryclick.html",context)

def OnDestinationClick(request,pk):
    try:
        desti = Destination.objects.get(id = pk)
    except:
        desti = [] 
    try:
        paki = Packages.objects.filter(destination = desti) 
    except:
        paki = []
    try:
        route = Journey.objects.filter(destination_include = desti) 
    except:
        route = []
    try:
        guide = TourGuids.objects.filter(Destination_Near = desti) 
    except:
        guide = []
    try:
        hotels = Hotels.objects.filter(Destination_Near = desti)
    except:
        hotels = []
    try:
        rest = Restaurants.objects.filter(Destination_Near = desti)
    except:
        rest = []

    context = {
        "desti":desti,
        "paki":paki,
        "route":route,
        "guide":guide,
        "hotels":hotels,
        "rest":rest,

    }


    return render(request,"destinationforuser.html",context)
    



