#version 1.1
#latest update of 12 jun 6:20 pm
import os
import time


repo="https://github.com/Santoshkurmi/python_auto_update"
def check_update(repo,tempdir,filename):
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
            time=time.time();
            print("Update is available,updating");
            if os.system(f"cp {filename}.py .{filename}_{time}"):
                if os.system(f"cp {tempdir}/{filename}.py ."):
                    print("Successfully updated the program");
                
            
        else:
            print("Everything is upto date");
    else:
        print("Something went wrong in the server")

        
check_update(repo,".temp","auto");
