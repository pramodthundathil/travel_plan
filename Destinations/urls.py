from django.urls import path 
from .import views  

urlpatterns = [

    path("DestinationHome",views.DestinationHome,name="DestinationHome"),
    path("HotelAdd",views.HotelAdd,name="HotelAdd"),
    path("RestaurentAdd",views.RestaurentAdd,name="RestaurentAdd"),
    path("GuideAdd",views.GuideAdd,name="GuideAdd"),
    path("AddContry",views.AddContry,name="AddContry"),
    path("Services",views.Services,name="Services"),
    path("PackageHome",views.PackageHome,name="PackageHome"),
    path("RouteHome",views.RouteHome,name="RouteHome"),
    path("DeleteRoute/<int:pk>",views.DeleteRoute,name="DeleteRoute"),
    path("DeleteDestination/<int:pk>",views.DeleteDestination,name="DeleteDestination"),
    path("DeletePackage/<int:pk>",views.DeletePackage,name="DeletePackage"),
    path("DeleteHotel/<int:pk>",views.DeleteHotel,name="DeleteHotel"),
    path("DeleteGuide/<int:pk>",views.DeleteGuide,name="DeleteGuide"),
    path("DeleteRestarent/<int:pk>",views.DeleteRestarent,name="DeleteRestarent"),

]