import requests
import time
import smtplib, ssl
from configparser import ConfigParser
from datetime import datetime, timedelta
count =0
w=[]

#read apikey from config.ini
parser = ConfigParser()
parser.read('config.ini')
key = parser.get('COMMON', 'APIKEY')
email = parser.get('COMMON', 'EMAILADDRESS')
password = parser.get('COMMON', 'EMAILPW')
contactToNotify = parser.get('COMMON', 'NOTIFYCONTACT')
port = 465

url=f'https://api.bestbuy.com/v1/products(search=rtx&search=3070&search=graphics&search=card)?format=json&show=sku,name,salePrice,orderable,url&apiKey={key}'

r=requests.get(url)
pageCount= r.json()["totalPages"]

while True:
    if(pageCount>=1):
        for i in range(r.json()["totalPages"]):
            #time.sleep(1)
            x=i+1
            url=f'https://api.bestbuy.com/v1/products(search=rtx&search=3070&search=graphics&search=card)?format=json&show=sku,name,salePrice,orderable,url&apiKey={key}&page={x}'
            w.append(requests.get(url))

        for c in range(len(w)):   
            for j in range(len(w[c].json())):
                try:
                    print(f'''Product: {w[c].json()["products"][j]["name"]}\nPrice: {w[c].json()["products"][j]["salePrice"]}\nAvailability: {w[c].json()["products"][j]["orderable"]}\nURL:{w[c].json()["products"][j]["url"]}\n=============================================================================================================''')
                    if (w[c].json()["products"][j]["orderable"] == "Available"):
                        #Replace Code Here
                        message = f"""\
{w[c].json()["products"][j]["name"]}
URL: {w[c].json()["products"][j]["url"]}"""
#awkward indentation is due to emails not properly sending unless message variable is formated in this way
                        #stop replace here
                        context = ssl.create_default_context()
                        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                            server.login(email, password)
                            server.sendmail(email, contactToNotify, message)
                        count+=1

                except:
                    
                    break 
    

    print (count)
    time.sleep(5)