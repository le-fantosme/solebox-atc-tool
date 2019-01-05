import requests
from bs4 import BeautifulSoup as bs
import webbrowser
import datetime
import time


#REMEMBER TO EDIT ALL LINES THAT ARE MARKED WITH COMMENTS BOII
print("A 5 minutes trash by pxtrck")
s=requests.session()
header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
solename=""	#WRITE THERE YOUR NAME; must be the one you used to register on solebox
productlink="https://www.solebox.com/Footwear/Running/Moon-Racer-variant.html"	#the link of your product
aid="31764" 	#the aid value, read README.md to check how to find it out
def get_prod():
    a=s.get(productlink, headers=header)
    if a.status_code ==200:
        print("Got product!")
        print(datetime.datetime.now())
    else:
        print("Error getting product. ")
        time.sleep(1)	#just change the retry delays how you want it
        get_prod()

    soup=bs(a.text, 'lxml')
    cnid=soup.find('input',{'name':'cnid'})['value']
    anid=soup.find('input',{'name':'anid'})['value']
    parentid=soup.find('input',{'name':'parentid'})['value']
    panid=""

    payloadatc={"lang": "0",
    "cnid": "cnid",
    "listtype": "list",
    "actcontrol": "details",
    "cl": "details",
    "aid": aid,
    "anid": anid,
    "parentid": parentid,
    "panid": panid,
    "fnc": "tobasket",
    "am": "1"}

    atc=s.post("https://www.solebox.com/index.php?", headers=header, data=payloadatc, allow_redirects=False)
    if atc.status_code==302:
        print("ATC successfull")
        print(datetime.datetime.now())
    else:
        print("ATC failed")
        print(datetime.datetime.now())
        time.sleep(0.5)
        get_prod()
get_prod()


def login_checkout():
    b=s.get("https://www.solebox.com/mein-konto/", headers=header)
    soup=bs(b.text, 'lxml')
    stoken=soup.find('input',{'name':'stoken'})['value']
    ldt={"stoken": stoken,
    "lang": "0",
    "listtype": "",
    "actcontrol": "account",
    "fnc": "login_noredirect",
    "cl": "account",
    "lgn_usr": "",	#YOUR SOLEBOX EMAIL, enter it there 
    "lgn_pwd": ""}	#YOUR SOLEBOX PASSWORD 
    login=s.post("https://www.solebox.com/index.php?", headers=header, data=ldt)
    if solename in login.text:
        print("Logged in")
        print(datetime.datetime.now())
    else:
        print("Cold not log in")
        print(datetime.datetime.now())
        time.sleep(1)
        login_checkout()

    conclude=s.get("http://solebox.com/index.php?actcontrol=payment&cl=payment&fnc=validatepayment&paymentid=globalpaypal&lang=0&stoken=&userform=", headers=header)
    print("Waiting on PayPal")
    time.sleep(1)
    print(conclude.url)
    print(datetime.datetime.now())
    x=conclude.url

    webbrowser.open(x)
    print("Opening browser, pay with PayPal. ")
    print(datetime.datetime.now())
login_checkout()
