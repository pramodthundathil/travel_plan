from django.shortcuts import render, redirect

import json
import pandas as pd
import requests

def RouteAdd(request):

    response1 = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=32d8341ec1da4e57aba06d2b9b004c50")
    val = json.loads(response1.content)
    pincode = val["postal_code"]
    resp2 = requests.get("https://api.data.gov.in/resource/6176ee09-3d56-4a3b-8115-21841576b2f6?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json&filters%5Bpincode%5D={}".format(pincode))
    val2 = json.loads(resp2.content)


    # pincode = val["postal_code"]
    # data = pd.read_csv('journy/Pincode_india.csv',sep=",", encoding='ISO-8859-1')
    # array = data.values
    # listdata = data[data["Pincode"] == int(pincode)]
    # district = listdata.values
    
    # print(district,"=============================")
    print(val2["records"][0]["officename"])

    return render(request,'routesdisplay.html')


