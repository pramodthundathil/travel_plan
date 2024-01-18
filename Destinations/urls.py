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
    path("BookJourny/<int:pk>",views.BookJourny,name="BookJourny"),
    path("BookGuide/<int:pk>",views.BookGuide,name="BookGuide"),
    path("BookPackage/<int:pk>",views.BookPackage,name="BookPackage"),
    path("BookHotel/<int:pk>",views.BookHotel,name="BookHotel"),
    path("BookingConfirm",views.BookingConfirm,name="BookingConfirm"),
    path("Mybookings",views.Mybookings,name="Mybookings"),
    path("Bookings",views.Bookings,name="Bookings"),
    path("deletePackageBooking/<int:pk>",views.deletePackageBooking,name="deletePackageBooking"),
    path("deleteJournyBooking/<int:pk>",views.deleteJournyBooking,name="deleteJournyBooking"),
    path("deleteGuideBooking/<int:pk>",views.deleteGuideBooking,name="deleteGuideBooking"),
    path("deleteHotelBooking/<int:pk>",views.deleteHotelBooking,name="deleteHotelBooking"),
    path("Search",views.Search,name="Search"),
    path("RouteSearch",views.RouteSearch,name="RouteSearch"),
    path("RouteSearch1",views.RouteSearch1,name="RouteSearch1"),


]     