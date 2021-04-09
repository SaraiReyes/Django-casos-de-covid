from django.shortcuts import render

import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "cfd5cfefbamshfc97201376bac03p1784f2jsnd1f9137689e5",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response =requests.request("GET", url, headers=headers).json()

pythonDictionary = {'name':'Bob', 'age':44, 'isEmployed':True}
dictionaryToJson = json.dumps(pythonDictionary)





# Create your views here.
def helloworldview(request):
    noofresults=int(response['results'])
    mylist=[]
    print(noofresults)

    for x in range(noofresults):        
        mylist.append(response['response'][x]['country'])
    
    context={'mylist': mylist}
    
    return render(request,'helloworld.html',context)
