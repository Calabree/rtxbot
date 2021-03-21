from SendAlert import SendAlert
from configparser import ConfigParser
from BestBuyScan import BestBuyScanner
import os

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
    #TODO: ask user which rtx card they are looking 
    os.system('cls' if os.name == 'nt' else 'clear')
    intro()
    print("""
    Welome to Calabree's RTX Stock Bot! Please select a card from the menu below:
    1. RTX 3060/RTX 3060 TI
    2. RTX 3070
    3. RTX 3080
    4. RTX 3090
    """)
    
    card = Switch(input('please select a number from above '))
    parser['COMMON']['CARDNAME']=f'{card}'
    print(card)
    with open('config.ini','w') as configfile:
        parser.write(configfile)
    bbs.getJSONPageCount(key,card)
    bbs.scanBBStock(key,card,email, password, contactToNotify, 465)

def Switch(card):
    switch={
        '1': "3060",
        '2': "3070",
        '3': "3080",
        '4': "3090"
    }
    return switch.get(card, "Not A Valid Entry")

def intro():
    print("""
 _       __     __                             ______         ______      __      __                  _          ____  _______  __    ____  ____  ______
| |     / /__  / /________  ____ ___  ___     /_  __/___     / ____/___ _/ /___ _/ /_  ________  ___ ( )_____   / __ \/_  __/ |/ /   / __ )/ __ \/_  __/
| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \     / / / __ \   / /   / __ `/ / __ `/ __ \/ ___/ _ \/ _ \|// ___/  / /_/ / / /  |   /   / __  / / / / / /   
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/    / / / /_/ /  / /___/ /_/ / / /_/ / /_/ / /  /  __/  __/ (__  )  / _, _/ / /  /   |   / /_/ / /_/ / / /    
|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/    /_/  \____/   \____/\__,_/_/\__,_/_.___/_/   \___/\___/ /____/  /_/ |_| /_/  /_/|_|  /_____/\____/ /_/     
    ____                 __   __  __            ____  _________    ____  __  _________                __                                                
   / __ \___  ____ _____/ /  / /_/ /_  ___     / __ \/ ____/   |  / __ \/  |/  / ____/ ____ ___  ____/ /                                                
  / /_/ / _ \/ __ `/ __  /  / __/ __ \/ _ \   / /_/ / __/ / /| | / / / / /|_/ / __/   / __ `__ \/ __  /                                                 
 / _, _/  __/ /_/ / /_/ /  / /_/ / / /  __/  / _, _/ /___/ ___ |/ /_/ / /  / / /____ / / / / / / /_/ /                                                  
/_/ |_|\___/\__,_/\__,_/   \__/_/ /_/\___/  /_/ |_/_____/_/  |_/_____/_/  /_/_____(_)_/ /_/ /_/\__,_/                                                   
    ____       ____                                    __  _             _                                                                              
   / __ )___  / __/___  ________     _________  ____  / /_(_)___  __  __(_)___  ____ _                                                                  
  / __  / _ \/ /_/ __ \/ ___/ _ \   / ___/ __ \/ __ \/ __/ / __ \/ / / / / __ \/ __ `/                                                                  
 / /_/ /  __/ __/ /_/ / /  /  __/  / /__/ /_/ / / / / /_/ / / / / /_/ / / / / / /_/ /                                                                   
/_____/\___/_/  \____/_/   \___/   \___/\____/_/ /_/\__/_/_/ /_/\__,_/_/_/ /_/\__, /                                                                    
                                                                             /____/                                                                     

""")
    input("Press enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ =="__main__":
    main()
