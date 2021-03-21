from SendAlert import SendAlert
from configparser import ConfigParser
from BestBuyScan import BestBuyScanner

sa = SendAlert()
bbs= BestBuyScanner()
parser = ConfigParser()
#PARSES THROUGH config.ini FOR CONFIG VALUES
parser.read('config.ini')
key = parser.get('COMMON', 'APIKEY')
email = parser.get('COMMON', 'EMAILADDRESS')
password = parser.get('COMMON', 'EMAILPW')
contactToNotify = parser.get('COMMON', 'NOTIFYCONTACT')


def main():
    bbs.getJSONPageCount(key)
    bbs.scanBBStock(key,email, password, contactToNotify, 465)
    #sa.sendAlert(email, password, contactToNotify, 465)


if __name__ =="__main__":
    main()

