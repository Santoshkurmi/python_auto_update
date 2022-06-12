#version 1.1
#this is the latest version of sat 12 june 6:14 pm
import os
repo="https://github.com/Santoshkurmi/python_auto_update"
def check_update(repo,tempdir,filename):
    version1="";version2="";
    if os.path.exists(tempdir):
        os.system(f"rm {tempdir} -rf");

    if not os.system(f"git clone {repo} {tempdir} && clear"):
        file = open(f"{tempdir}/{filename}.py");
        version1=float(file.readline().replace("#version",""));
        file.close()
    
    if os.path.exists(f"{filename}.py"):
        version2=float(open(f"{filename}.py").readline().replace("#version",""));
    return [version2,version1];

def do_update():
    current,latest = check_update(repo,".temp","auto");
    if current>=1 and latest>=1:
        if current<latest:
            print("Update is available,updating");
            if os.system(f"cp {tempdir}/{filename}.py ."):
                print("Successfully updated the program");
                
            
        else:
            print("Everything is upto date");
    else:
        print("Something went wrong in the server")

        
do_update();
