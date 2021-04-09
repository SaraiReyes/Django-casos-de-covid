from django.shortcuts import render

import requests
import json

##inserta aqui tu key api

response =requests.request("GET", url, headers=headers).json()







# Create your views here.
def helloworldview(request):
    
    mylist=[]
    
    noofresults=int(response['results'])
    for x in range(noofresults):        
        mylist.append(response['response'][x]['country'])
    
    context={'mylist': mylist}
    


    if request.method=="POST":
        selectedcountry=request.POST['selectedcountry']
        noofresults=int(response['results'])
        for x in range(0,noofresults):    
            if(selectedcountry==response['response'][x]['country']):
                print(selectedcountry)
                new=response['response'][x]['cases']['new']
                active=response['response'][x]['cases']['active']
                critical=response['response'][x]['cases']['critical']
                recovered=response['response'][x]['cases']['recovered']
                total=response['response'][x]['cases']['total']
                deaths=int(total)-int(active)-int(recovered)
                print(response['response'][x]['cases']['new'])
        context={'mylist': mylist,'selectedcountry': selectedcountry,'new': new,'active': active,'critical': critical,'recovered': recovered,'total': total,'deaths': deaths }
        return render(request,'helloworld.html',context)

    mylist=[]
    
    noofresults=int(response['results'])
    for x in range(noofresults):        
        mylist.append(response['response'][x]['country'])
    
    context={'mylist': mylist}
    
    return render(request,'helloworld.html',context)
