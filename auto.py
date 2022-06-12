#version 1.2
#latest update of 12 jun 6:20 pm
import os
import time


repo="https://github.com/Santoshkurmi/python_auto_update"
def update(repo,tempdir,filename):
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
            print("Update is available,updating");
            if not os.system(f"cp {filename}.py .{filename}_{time1}"):
                if not os.system(f"cp {tempdir}/{filename}.py ."):
                    print("Successfully updated the program");
            if os.path.exists(tempdir):
                os.system(f"rm {tempdir} -rf");

                
            
        else:
            print("Everything is upto date");
    else:
        print("Something went wrong in the server")

    

#end of upate function

def printer():
    print("Hello what's up");
in=input("1.Check update\n2.Print")
if input=="1":update(repo,".temp","auto");
elif input=="2":printer();

