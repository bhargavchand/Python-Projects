import bs4
import requests
import re
from bs4 import BeautifulSoup
import smtplib

MY_HEADER = {
    "Accept-Language": 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,te;q=0.6',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/91.0.4472.124 Safari/537.36 '
}
MY_COMPRESSIONS_URL = 'https://www.amazon.ca/gp/product/B0819PX7JH?pf_rd_r=681J0M1KMH0A5M0EK5WX&pf_rd_p=05326fd5-c43e' \
                      '-4948-99b1-a65b129fdd73&pd_rd_r=e873548f-615d-4832-9a0f-fc00ece8f2ac&pd_rd_w=Qba1r&pd_rd_wg' \
                      '=InzSo&ref_=pd_gw_unk'

response = requests.get(url=MY_COMPRESSIONS_URL,headers=MY_HEADER);
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
price = soup.find(id="priceblock_ourprice").get_text()
title = soup.find(id="productTitle").get_text().strip()
price = re.sub('\D','',price.split()[0])
BUY_PRICE = 20

if price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )