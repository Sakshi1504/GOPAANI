from typing import Container
from django.conf.urls import url
from django.shortcuts import render
import requests
import json
from .models import GoPaani
# Create your views here.

#def main(request):
#    print("hi")
#    return render(request, "index.html")

def search(request):
    context={}
    if request.method=="POST":
        #print("inside search post")
        key=request.POST.get("search")
        print(f"Value of key is : {key}")
        if key is not '':
            murl="https://itunes.apple.com/lookup?id="+key
            #https://itunes.apple.com/lookup?id=284910350
            urlop=requests.get(murl)
            print(f"urlop: {urlop}") #<Response [200]>
            if urlop.status_code==200:
                jsonop=urlop.json()
                #print(f"json op : {jsonop}")
                #print(f"output : {jsonop.get('results')}")
                results=jsonop.get('results')
                print(type(results))
                print(f"output : {results[0].get('artistName')}")
                print(f"output : {results[0].get('price')}")
                print(f"output : {results[0].get('version')}")
                print(f"output : {results[0].get('primaryGenreName')}")
                context['key']=key
                context['artistName']=results[0].get('artistName')
                context['price']=results[0].get('price')
                context['version']=results[0].get('version')
                context['primaryGenreName']=results[0].get('primaryGenreName')
                artistName=results[0].get('artistName')
                price=results[0].get('price')
                version=results[0].get('version')
                primaryGenreName=results[0].get('primaryGenreName')
                createobj=GoPaani.objects.create(lookupkey=key, price=price, artistName=artistName, version=version,primaryGenreName=primaryGenreName)
                gopaniobj=GoPaani.objects.all()
                print(f"gopaniobj {gopaniobj}")
            else:
                context['error']="Data does not exist for provided key. Please enter proper lookup key."
                return render(request, "index.html", context)
        else:
                context['error']="Data does not exist for provided key. Please enter proper lookup key."
                return render(request, "index.html", context)

    return render(request, "index.html", context)
