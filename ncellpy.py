#version 20220711.6
#change ncellapp to ncell_app 1.3
#auto update every day 1.4
#finally done some fixes and update goes to 2 days every
#remove update button
from datetime import datetime
time=int( datetime.now().hour)
import subprocess
if (time <13):
    print("\033[91mHello🙃 Good morning🌄")
elif time <20:
    print("\033[92mHello😳 Good afternoon💫")
elif time<25:
    print("\033[93mHello🥺 Good evening🌌")

func_wow=""
import json 
import re
import hashlib
import requests 
import os 
import sys
import random
import datetime
import time

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
repo="https://github.com/Santoshkurmi/python_auto_update"

def update(repo,filename,tempdir=".temp",dust=0):
    version1="";version2="";latest="";current="";
    if os.path.exists(tempdir):
        os.system(f"rm {tempdir} -rf");

    if not os.system(f"git clone {repo} {tempdir} && clear"):
        file = open(f"{tempdir}/{filename}.py");
        latest=float(file.readline().replace("#version",""));
        file.close()
    else:
        print("Please install git\n");
        os.system("apt install git -y");
    
    if os.path.exists(f"{filename}.py"):
        current=float(open(f"{filename}.py").readline().replace("#version",""));
    if dust==0:
        if current>=1 and latest>=1:
            if current<latest:
                time1=time.time();
                print("\n_____________________\nUpdate is available,updating\n");
                if not os.path.exists(".hehe"):
                    os.system(f"mkdir .hehe");
                if not os.system(f"cp {filename}.py .hehe/.{filename}_{time1}"):
                    if not os.system(f"cp {tempdir}/{filename}.py ."):
                        print("Successfully updated the program\n_____________________\n");
                        set_update_time()
                        print(f"\n{c()}Please restart the program")
                        exit();
                if os.path.exists(tempdir):
                    os.system(f"rm {tempdir} -rf");

                    
                
            else:
                print("Everything is upto date");
                set_update_time()
        else:
            print("Something went wrong in the server")
    elif dust==1:
        
                time1=time.time();
                print("\n_____________________\nUpdate is available,updating\n");
                if not os.path.exists(".hehe"):
                    os.system(f"mkdir .hehe");
                if not os.system(f"cp {filename}.py .hehe/.{filename}_{time1}"):
                    if not os.system(f"cp {tempdir}/{filename}.py ."):
                        print("Successfully updated the program\n_____________________\n");
                        set_update_time()
                        print(f"\n{c()}Please restart the program")
                        exit();
                if os.path.exists(tempdir):
                    os.system(f"rm {tempdir} -rf");

                
            
            
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
            if dif >=86400*2:
            
                return True
            else:
                return False

def set_update_time():
    with open(".time.txt","w") as file:
        file.write(str(int(time.time())))



if func_wow==0 and check_update_time():
    update(repo,"ncellpy");


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
            
            if text=="e":exit();
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
                    print(phone1)

                    ###################################
                    if not len(phone1)>=10:dialog("spinner","The phone number is not correct😭","Please try again");exit()
                    phone= re.sub("[\W_]","",phone1)[-10:]
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
            if len(phone1)>=0 and len(phone1)<10:print("Wrong phone1 number..");return
            phone1= re.sub("[\W_]","",phone1)[-10:]
            
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
        if text=="I am machine.":
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
                print(f"{counter}. {json['ncellName']}")
                print(f"Usage: {json['balance']}{json['uom']}")
                print(f"Expiry: {json['expDate']}\n\n")
                counter +=1;

    for json in data["voiceBalanceList"]:
                if counter<4:
                    comb+=str(counter)+ ". "+ json['ncellName']+"\nUsage: "+ str(json['freeTalkTime']) + "Min" + "\nExpiry: "+json['expDate']+"\n\n"
                else:

                    comb2+=str(counter)+ ". "+ json['ncellName']+"\nUsage: "+ str(json['freeTalkTime']) + "Min" + "\nExpiry: "+json['expDate']+"\n\n"
                print(f"{counter}. {json['ncellName']}")
                print(f"Usage: {json['freeTalkTime']} Min")
                print(f"Expiry: {json['expDate']}\n\n") 
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

    f=open("#all "+ff+".txt" ,"a");
    call=open("#callMsg "+ff+".txt" ,"a");
    
    topup=open("#topup "+ff+".txt" ,"a");
    data=open("#internet "+ff+".txt" ,"a");
    
    
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
        phone2=input("Enter the phone: ");
        if not  len(phone2)>=10:
            exit();
        phone2= re.sub("[\W_]","",phone2)[-10:]
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

    in_number= input("Enter the number: ");
    if in_number=="b":return;
    elif in_number=="e":exit();
    elif len(in_number)>=10:
        phone2 =re.sub("[\W_]","",in_number)[-10:]
        
    else:
        phone2 = web_numbers[int(in_number)-1];
        if temp==phone2:
                printerweb();
                return
            
        
            
    res=postsend()
    if not res ==12 and not res==10:printerweb()
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
    
        aa=input(f"{c()}1. Login\n{c()}2. AutoLogin\n{c()}3. Set Default\n{c()}4. Print\n{c()}5. Choose number\n{c()}=>");
        if aa=="b":
            break;
        elif aa=="e":
            exit();
        elif aa=="4":printerweb();
        elif int(aa)==1:
            weblogin();
        elif int(aa)==2:weblogin(1);
        elif int(aa)==3:setdefault();
        elif int(aa)==5:printnumbers();
        elif len(aa)==10:
            phone2=aa;
            
            res=postsend()
            if not res ==12 and not res==10:printerweb()
            if res==10:weblogin()
        input(f"{c()}Press enter to show menu: ")
        
            




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

        if choose=="b" or choose==8:return;
        if choose=="e":exit()
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
        








#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#for repeating all the things here
def web():
    print(f"{c()}\n***********************************")
    readwrite("update")
    logintest();
    while(True):
        print("\n***********************************\n")
        for i in range(len(fun_list)):
            print(f'{c()}{i+1}. {fun_list[i][0]}');
        
        text=take("Enter the choice: ");
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

#Happy ending here everythings

######################################

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
    choose=take(f"\n{c()}1. Ncell Ecare\n{c()}2. Ncell App{c()}\n3. Ncell Web\n{c()}4. Update\n{c()}=>");

    if choose=="b" or choose==5:break;
    elif choose=="4f":update(repo,"ncellpy",dust=1)
    elif int(choose)==1:web();
    elif int(choose)==2:app();
    elif int(choose)==4:update(repo,"ncellpy",dust=0);
    
    elif int(choose)==3:webaxiata();
