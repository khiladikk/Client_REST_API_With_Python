#Objective:-Learn to use a RESTful API

#we are using python inbuild module
import requests

#Here is the Given API 
url = 'http://13.127.155.43/api_v0.1/sending'

#Data that we want to send and receive
data = {
        "Name": "Akshay Kumar",
        
        "Phone_Number": "123456",
        
        "College_Name": "forsk company",
        "Branch" : "CSE"
        }


response = requests.post(url, json=data)


print(response.text)

#to extract the detail from response

import requests

api_url = 'http://13.127.155.43/api_v0.1/receiving'

par = {"Phone_Number":"123456"}

resp = requests.get(api_url,params=par)

data = resp.json()

for k,v in data.items():
    print k+" : "+v