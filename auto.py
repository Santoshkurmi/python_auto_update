#version 1.0
import os

repo="https://github.com/Santoshkurmi/python_auto_update"
if os.path.exists(".temp"):
    os.system("rm .temp -rf");

if not os.system(f"git clone {repo} .temp && clear"):
    file = open(".temp/auto.py");
    version=file.readline().replace("#version","");
    print(version);
    
  
