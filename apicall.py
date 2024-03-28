import requests
import json

#### post
incoming_data_url="http://127.0.0.1:8000/server/incoming_data/"

account_create_or_listview="http://127.0.0.1:8000/AccountListCreateView"

account_retrive_or_updateview_delete='http://127.0.0.1:8000/AccountRetriveUpdateView/'

destinationcrud="http://127.0.0.1:8000/DestinationView/"  #### for retive or update need to pass pk

retriveaccountdetailswithdestination="http://127.0.0.1:8000/getdestinations/"



######account_create_or_listview

response=requests.post(url=account_create_or_listview,data={"email_id":"smsamimasthan@gmail.com","account_id":"2","account_name":"masthan","Website":""}) 


print(response.json())


##### destination crud
response= requests.post(url=destinationcrud, json=
  { "url": "https://webhook.site/0faa70f9-8035-477f-b3d9-1ed928b1bdc6",
        "http_method": "POST",
        "header": {
            "APP_ID": "1234APPI2331234",
            "APP_SECTET": "enwdj3bsh32wer43bjhjs9ereuinkjcnsiurew8s",
            "ACTION": "user.update",
            "Content-Type": "application/json",
            "Accept": "*"
        },
        "account": 2})

print(response)



##### retrive account details withits all destinations

response=requests.get(url=f'{retriveaccountdetailswithdestination}{2}') 

print(response.json())






####post incoming url
response=requests.post(url=incoming_data_url,data={"employeeName":"samiullah","password":"Sami@16071994"},headers={"CL-X-TOKEN":"8Rc9GzaK0Ce9h3hlWu0AhT3iLTfUuHf6"}) 


print(response.json())




#### acount delete it will delete according to its destination

response=requests.delete(url=f'{account_retrive_or_updateview_delete}{3}') 

print(response,'response')
