import requests
import re
import config
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
from time import localtime, strftime, sleep
import send_email

class lookupProduct:
    def __init__(self, name, store, url, findClass, classType, typeContent, regex, availability, storeColor, headers):
        self.name = name
        self.store = store
        self.url = url
        self.findClass = findClass
        self.classType = classType
        self.typeContent = typeContent
        self.regex = regex
        self.availability = availability
        self.storeColor = storeColor
        self.headers = headers
    
    def soldOut_email(self):
        productStatus_update = ""
        cur_time = strftime("%H:%M:%S", localtime())
        print(cur_time, Fore.WHITE + "::", self.storeColor + self.store, Style.RESET_ALL, Fore.CYAN + self.name, Fore.WHITE + "::", Fore.RED + "Sold-Out")
        print(Fore.WHITE + "-------------------------------------------------------------")
        print(Style.RESET_ALL)
        productStatus_update += cur_time + product.store + " " + product.name + "  Sold-Out\n"
        sleep(2)


    def get_availability(self):
        page = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        result = str(soup.find(self.findClass, {self.classType:self.typeContent}))
        buttonState = re.compile(self.regex)
        availabilityMatch = buttonState.search(result).group()
        if self.availability == 0 or self.availability == availabilityMatch:
            soldOut_email()
        else:
            available_email()
            

    
    elif availability != product.availability:
            print(cur_time, Fore.WHITE + "::", product.storeColor + product.store, Style.RESET_ALL,
                Fore.CYAN + product.name, Fore.WHITE + "::", Fore.GREEN + "Available")
            print(Fore.WHITE + "-------------------------------------------------------------")
            print(Style.RESET_ALL)
            productStatus_update += cur_time + product.store + " " + product.name + " \n"
            if product.store == config.BB_prod["store"]:
                send_email.send_mailBB()
            elif product.store == config.GS_prod["store"]:
                send_email.send_mailGS()
            print(Fore.GREEN + "AVAILABLE --- Email Sent!")
            sleep(5)
    return productStatus_update

def product_update():
    productStatus_Total = ""
    productStatus_update = product_checker()
    productStatus_Total += productStatus_update
    print(emailCounter)
    return productStatus_Total

emailCounter = 1
emailupdate_string = ""

while True:
    email_update = product_update()
    emailupdate_string += email_update
    emailCounter += 1
    if emailCounter == 2:
        send_email.send_mailUpdate(emailupdate_string)
        print(Fore.WHITE + "Product Status Update \n")
        emailCounter = 0
        
    p1 = lookupProduct(config.BB_prod["name"], config.BB_prod["store"], config.BB_prod["url"], config.BB_prod["findClass"], config.BB_prod["classType"], config.BB_prod["typeContent"], config.BB_prod["regex"], config.BB_prod["availability"], Fore.BLUE)
    p2 = lookupProduct(config.GS_prod["name"], config.GS_prod["store"], config.GS_prod["url"], config.GS_prod["findClass"], config.GS_prod["classType"], config.GS_prod["typeContent"], config.GS_prod["regex"], config.GS_prod["availability"], Fore.MAGENTA)
    products = (p1, p2)
        