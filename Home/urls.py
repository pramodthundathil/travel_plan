from django.urls import path 
from .import views  

urlpatterns = [

    path("",views.Index,name="Index"),
    path("SignUp",views.SignUp,name="SignUp"),
    path("SignIn",views.SignIn,name="SignIn"),
    path("SignOut",views.SignOut,name="SignOut"),
    path("AdminHome",views.AdminHome,name="AdminHome"),
    path("OnContryClick/<int:pk>",views.OnContryClick,name="OnContryClick"),
    path("OnDestinationClick/<int:pk>",views.OnDestinationClick,name="OnDestinationClick"),

]
