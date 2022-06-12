#version 1.3
#latest update of 12 jun 6:20 pm
import os
import time


repo="https://github.com/Santoshkurmi/python_auto_update"
def update(repo,filename,tempdir=".temp"):
    version1="";version2="";
    if os.path.exists(tempdir):
        os.system(f"rm {tempdir} -rf");

    if not os.system(f"git clone {repo} {tempdir} && clear"):
        file = open(f"{tempdir}/{filename}.py");
        latest=float(file.readline().replace("#version",""));
        file.close()
    
    if os.path.exists(f"{filename}.py"):
        current=float(open(f"{filename}.py").readline().replace("#version",""));

    if current>=1 and latest>=1:
        if current<latest:
            time1=time.time();
            print("\n_____________________\nUpdate is available,updating\n");
            if not os.path.exists(".hehe"):
                os.system(f"mkdir .hehe");
            if not os.system(f"cp {filename}.py .hehe/.{filename}_{time1}"):
                if not os.system(f"cp {tempdir}/{filename}.py ."):
                    print("Successfully updated the program\n_____________________\n");
                    print(f"\n{c()}Please restart the program")
                    exit();
            if os.path.exists(tempdir):
                os.system(f"rm {tempdir} -rf");

                
            
        else:
            print("Everything is upto date");
    else:
        print("Something went wrong in the server")

    

#end of upate function

def printer():
    print("Hello what's up");
number=input("1.Check update\n2.Print")
if number=="1":update(repo,"auto");
elif number=="2":printer();

