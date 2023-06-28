from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
import numpy as np
import pickle

pickle_in=open("./savedmodels/model.pkl","rb")
reg=pickle.load(pickle_in)

# <!-- aarsh saxena 21bec001 -->

def index(request):
    try:
        columns = ['Area', 'BHK', 'Bathroom', 'Furnishing', 'Parking', 'Status','Transaction', 'Type', 'Chittaranjan Park','Kailash Colony, Greater Kailash', 'Lajpat Nagar 2', 'Lajpat Nagar 3','Laxmi Nagar', 'Mehrauli', 'Rohini Sector 24', 'Safdarjung Enclave','Saket', 'Yamuna Vihar, Shahdara']

        localities = ['Alaknanda', 'Chittaranjan Park','Kailash Colony, Greater Kailash', 'Lajpat Nagar 2', 'Lajpat Nagar 3','Laxmi Nagar', 'Mehrauli', 'Rohini Sector 24', 'Safdarjung Enclave','Saket', 'Yamuna Vihar, Shahdara']
    
        if request.method == "POST":
            area = int(request.POST.get('area'))
            area_unit = request.POST.get('area_unit')
            locality = request.POST.get('locality')
            bhk = int(request.POST.get('bhk'))
            bathroom = int(request.POST.get('bathroom'))
            parking = int(request.POST.get('parking'))
            type1 = int(request.POST.get('type'))
            transaction = int(request.POST.get('transaction'))
            furnished = int(request.POST.get('furnished'))
            status = int(request.POST.get('status'))
            if area_unit == "sqmt":
                area = int(area*10)

            # prediction
            from warnings import simplefilter
            # ignore all warnings
            simplefilter(action='ignore')
            arr = list(np.zeros(len(columns)))
            # print(locality)
            try:
                locality_index= columns.index(locality)
            except:
                locality_index=-1
            print(locality_index)
            arr[0]=area
            arr[1]=bhk
            arr[2]=bathroom
            arr[3]=furnished
            arr[4]=parking
            arr[5]=status
            arr[6]=transaction
            arr[7]=type1

            if locality_index>=0:
                arr[locality_index]=1

            # print(arr)
            price = reg.predict([arr])
            price=price[0]
            price=float(price/100000.00)
            price=round((price),2)

            data = {
                'check': True,
                'price': price,
                #     'area':area,
                #     'area_unit':area_unit,
                #    'locality':locality,
                #     'bhk':bhk,
                #     'bathroom':bathroom,
                #     'parking':parking,
                #     'type1':type1,
                #     'transaction':transaction,
                #     'furnished':furnished,
                #     'status':status
            }

            return render(request, "index.html", data)
        

        data = {'localities': localities}
        return render(request, "index.html", data)
    
    except:
        messages.error(request, "Something went wrong. Try after some time.")
        data = {'localities': localities}
        return render(request, "index.html", data)
    
    
    
# <!-- aarsh saxena 21bec001 -->
def error_404(request,exception):
    return render(request,"404.html")