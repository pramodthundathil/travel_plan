from django.urls import path 
from .import views  

urlpatterns = [
        path("RouteAdd",views.RouteAdd,name="RouteAdd")

]