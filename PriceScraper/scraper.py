import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://smartstore.naver.com/grizzlykorea/products/429224385?NaPm=ct%3Dk00o16o0%7Cci%3D0zq00000rAHr%5FrcybvjG%7Ctr%3Dpla%7Chk%3D0bccd72aeb8d739f6b8c862dbbbe76d3e856b418"

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'}

page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

productname = soup.find(class_= 'prd_name').get_text()[5:]
price = soup.find(class_ = 'info_cost is_benefit').get_text()[15:21]
discount = soup.find(class_ = 'discount thm').get_text()

convertedprice = float(price.replace(',', ''))

#function to send mail
def sendmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('jaep970805@gmail.com', 'oiylswpadsxyoohny')
    subject = 'Price fell down!'
    body = f'Check the link {URL}'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        'jaep970805@gmail.com',
        'jaep970805@gmail.com',
        msg
    )
    print("Email has been sent")
    server.quit()

while(True):
    if(convertedprice < 60000):
        sendmail()
    #check every week
    time.sleep(3600*24*7)

print(productname)
print(price)
print(discount)
print(convertedprice)
