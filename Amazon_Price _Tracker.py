#We have to import require modules
#First we have to install requests, bs4 using pip
#IN terminal we install modules like >>>pip install requests bs4

import requests
from bs4 import BeautifulSoup
import smtplib
# URL of the Product you want to Track
URL="https://www.amazon.in/JBL-Most-Powerful-Portable-Speaker-20000MAH/dp/B075XR7W41/ref=sr_1_1?crid=2CDQFW5T74KRN&keywords=jbl+boombox&qid=1566984399&s=gateway&sprefix=jbl+boom%2Caps%2C300&sr=8-1"
#we can get your user agent by searching "MY USER AGENT" in Google (COPY AND PASTE)
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}

def check_price():
    page=requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    print(soup.prettify())

    title=soup.find(id="productTitle").get_text()

    price=soup.find(id="priceblock_ourprice").get_text()

    cp=(''.join(filter(str.isdigit,price)))
    changed_price=int(cp[0:-2])
    print(changed_price)
    print(title.strip())

    if (changed_price<25000):
        send_mail()

    print(changed_price)
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls( )
    server.ehlo()
    # we have to give our required mail details like Email-ID, Password
    server.login('***email***','***password***')

    subject="Price Decreased"
    body='Check AMAZON LINK https://www.amazon.in/JBL-Most-Powerful-Portable-Speaker-20000MAH/dp/B075XR7W41/ref=sr_1_1?crid=2CDQFW5T74KRN&keywords=jbl+boombox&qid=1566984399&s=gateway&sprefix=jbl+boom%2Caps%2C300&sr=8-1'
    msg=f"Subject:{subject}\n\n{body}"
    # Here we have to give your Mailid and Mail id to whome you have to send Mail
    server.sendmail(
        '***your mail id***','***mailID to whome you have to send***',msg
    )
    print("EMAIL has Sent")
    server.quit()

check_price()