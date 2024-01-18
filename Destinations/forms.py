from django.forms import ModelForm
from .models import Destination, Contry, Packages, Journey, Hotels, Restaurants, TourGuids
from django.forms import TextInput,PasswordInput, Select, Textarea





class DestinationAddForm(ModelForm):

    class Meta:
        model = Destination
        fields = "__all__"

        widgets = {
            'destination_name': TextInput(attrs={'class': 'form-control p','placeholder':'Destination Name'}),
            'key_words': TextInput(attrs={'class': 'form-control','placeholder':'Key Words'}),
            'place': TextInput(attrs={'class': 'form-control','placeholder':'Area'}),
            'district': TextInput(attrs={'class': 'form-control','placeholder':'district'}),
            "contry": Select(attrs={'class': 'form-control','placeholder':'Contry'}),
            'attractions': TextInput(attrs={'class': 'form-control','placeholder':'Tourist Attractions'}),
            'district': TextInput(attrs={'class': 'form-control','placeholder':'district'}),
            "address": Textarea(attrs={'class': 'form-control','placeholder':'Address'}),
            'postel_code': TextInput(attrs={'class': 'form-control','placeholder':'Postel Code',"type":"number"})

        }

class ContryAddForm(ModelForm):

    class Meta:
        model = Contry
        fields = "__all__"

        widgets = {
            'country_name': TextInput(attrs={'class': 'form-control','placeholder':'Contry Name'}),
            # 'contry_image': TextInput(attrs={'class': 'form-control',"type":"file"}),
        }

class PackageAddForm(ModelForm):

    class Meta:
        model = Packages
        fields = ["destination","key_words","image","number_of_days","number_of_nights","number_of_persons","amount","description"]

        widgets = {
            'number_of_days': TextInput(attrs={'class': 'form-control p','placeholder':'Number of Days',"type":"number"}),
            'number_of_nights': TextInput(attrs={'class': 'form-control p','placeholder':'Number of Nights',"type":"number"}),
            'number_of_persons': TextInput(attrs={'class': 'form-control p','placeholder':'Number of Persons',"type":"number"}),
            'key_words': TextInput(attrs={'class': 'form-control','placeholder':'Key Words'}),
            'amount': TextInput(attrs={'class': 'form-control','placeholder':'Amount', "type":"number"}),
            "destination": Select(attrs={'class': 'form-control','placeholder':'Destination'}),
            "description": Textarea(attrs={'class': 'form-control','placeholder':'Description'}),

        }

class JournyAddForm(ModelForm):

    class Meta:
        model = Journey
        fields = ["destination_include",]

        widgets = {
            
            "destination_include": Select(attrs={'class': 'form-control','placeholder':'Mode Of travel'}),
               

        }


class HotelAddForm(ModelForm):

    class Meta:
        model = Hotels
        fields = "__all__"
class RestaurentAddForm(ModelForm):

    class Meta:
        model = Restaurants
        fields = "__all__"

class GuideAddForm(ModelForm):

    class Meta:
        model = TourGuids
        fields = "__all__"      

