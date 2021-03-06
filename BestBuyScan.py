import requests
from SendAlert import SendAlert

class BestBuyScanner:
    def __init__(self):
        self.sa = SendAlert()
        self.oneTimeRun = 0
        self.myDict={}

    def getJSONPageCount(self,key,card):
        url=f'https://api.bestbuy.com/v1/products(search=rtx&search={card}&search=graphics&search=card)?format=json&show=sku&apiKey={key}'
        r=requests.get(url)
        self.pageCount= r.json()["totalPages"]
        return self.pageCount

    def scanBBStock(self, key, card, email, password,notifyContact, port):
        
        x=0
        count =0
        w=[]
        if(self.pageCount>=1):
            for i in range(self.pageCount):
                x=i+1
                url=f'https://api.bestbuy.com/v1/products(search=rtx&search={card}&search=graphics&search=card)?format=json&show=sku,name,salePrice,orderable,url&apiKey={key}&page={x}'
                w.append(requests.get(url))
        for c in range(len(w)):   
            for j in range(len(w[c].json())):
                try:
                    print(f'''Product: {w[c].json()["products"][j]["name"]}\nPrice: {w[c].json()["products"][j]["salePrice"]}\nAvailability: {w[c].json()["products"][j]["orderable"]}\nURL:{w[c].json()["products"][j]["url"]}\n=====================================================================================================================''')
                    if w[c].json()["products"][j]["sku"] not in self.myDict:
                        self.myDict[w[c].json()["products"][j]["sku"]] = w[c].json()["products"][j]["orderable"]
                        print("key added")
                        count+=1
                    else:
                        print("key already exists") 
                    if (w[c].json()["products"][j]["orderable"] == "SoldOut"):
                        if 
                        card = w[c].json()["products"][j]["name"]
                        url= w[c].json()["products"][j]["url"]
                        self.sa.sendAlert(email, password,notifyContact,port,card,url)
                except:
                    break 
        print(count)