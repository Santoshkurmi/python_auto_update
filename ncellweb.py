import requests
import json
token="";phone="";password="";
headerweb={
"Host": "webapi.ncell.axiata.com",
"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTY1NTA5NTQ5MywibmJmIjoxNjU1MDk1NDkzLCJleHAiOjE2NTUwOTkwOTMsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6Im5jZWxsX3B3YSJ9.FKbL7QEF1cpQBm8N8A1bGwfvnX1ako9scMbFX_sk7q8",
"Content-Type": "application/json;charset=UTF-8",
"Accept": "application/json, text/plain, */*"
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
    response=requests.get(url,headers=headerweb).json();
    return response["data"]

def postsend():
    url=host+"/v1/account/update-profile";
    data=json.dumps(getdata());
    response=requests.post(url,data=data,headers=headerweb).json()
    print()
    print(response["message"])
    print()

def weblogin():
    url=host + "/v1/account/login/request"
    phone=input("Enter the phone: ");
    if not  len(phone)==10:
        exit();
    password = input("Enter the password: " );
    data =json.dumps({
  "phoneNumber":phone,
  "password": password,
  "redirectTo": " ",
  "url":"/v1/account/login/request"
        })
    response =requests.post(url,headers=headerweb,data=data).json();
    print(response);


def printerweb():
    
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

weblogin()
while True:
    phone=input("Enter the phone: ");
    if len(phone)==10:
        postsend()
        printerweb()
    else:
        printerweb();
