import requests
import json
token="";phone="";password="";
header={
"Host": "webapi.ncell.axiata.com",
"Authorization": "Bearer 1463|M3mPt30dHTHhdJODOgcMOpdzC7alZbykhHHumkTf",
        }
host="https://webapi.ncell.axiata.com";

def getbody(key):
    body={
        "login":
        {
  "phoneNumber": "9824486107",
  "password": "Duffer123",
  "redirectTo": Null,
  "url":"/v1/account/login/request"
        },
            }
def getdata():
    global phone

    data={
        "email":"susma@gmail.com",
        "first_name":"Susma",
        "last_name":"susma",
        "date_of_birth":"12/10/2022",
        "phone_number":phone
        }
    return data

def getsend():
    url=host+"/v1/account/dashboard";
    response=requests.get(url,headers=header).json();
    return response["data"]
def postsend():
    url=host+"/v1/account/update-profile";
    data=json.dumps(getdata());
    response=requests.post(url,data=data,headers=header).json()
    print()
    print(response["message"])
    print()

def printer():
    
    response=getsend()
    balance= response["balanceInfo"]["currentBalance"]
    counter=2
    print(f"\n1. Balance: {balance}\n") 
    for key in response["packInfo"]:
        types=gettype(key)
        for json in response["packInfo"][key]:
            print(f"{counter}. {json['title_en']}"  )
            if key=="voicePack":
                print(f"Remaining: {json['remaining']/60}/{json['total']/60} {types}" )
            else:
                print(f"Remaining: {json['remaining']}/{json['total']} {types}" )
            print(f"Validity:{ json['validity']}\n")
            counter+=1

def gettype(key):
    types={"dataPack":"MB","voicePack":"Min","smsPack":"SMS"}
    return types[key]
while True:
    phone=input("Enter the phone: ");
    if len(phone)==10:
        postsend()
        printer()
    else:
        printer();
