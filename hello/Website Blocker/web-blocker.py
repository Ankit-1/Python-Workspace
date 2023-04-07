import time
from datetime import datetime as dt

hosts_temp=r"C:\Users\TheBOT\Python Workspace\hello\Website Blocker\Hosts\hosts"
hosts_path=r"C:\Windows\System32\drivers\etc"
redirect="127.0.0.1"
website_list=['https://jimsindia.org/','104.27.131.80','https://jimsindia.org','jimsindia.org','www.google.com']

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() <dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("Working Hours!")
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_temp,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours!!")
    time.sleep(3)