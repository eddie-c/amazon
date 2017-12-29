import requests
from bs4 import BeautifulSoup
from global_tools import GlobalTools
import json

import urlparse

class Shop(object):
    def __init__(self,link,id=None):
        self.shopid = None
        self.link = link
        self.id = id

    def get_shop_id(self):
        result = urlparse.urlparse(self.link)
        params = urlparse.parse_qs(result.query)
        self.id = params['seller']
        print self.id

    def get_shop_info(self):
        headers = GlobalTools.getHeaders()
        res = requests.get(self.link,headers=headers)
        html = BeautifulSoup(res.text,'lxml')
        print html.find(id="sellerName").text
        feedback = html.find(id="feedback-summary-table")
        feedbacktab = feedback.find_all("tr")
        timescoop = feedbacktab[0].find_all("th")
        for item in timescoop:
            print item.text
        positive = feedbacktab[1].find_all("td")
        neutral = feedbacktab[2].find_all("td")
        negtive = feedbacktab[3].find_all("td")
        count = feedbacktab[4].find_all("td")
        for  feedback in feedbacktab:
            line = feedback.find_all("td")
            for item in line:
                print item.text.strip("\n").strip()+",",
            print

        products = html.find(id="product-data").find_all(attrs={'class':"product-details"})
        for product in products:
            titlelink = product.find('a',attrs={'class':"product-title"})
            title = titlelink.get('title')
            href = titlelink.get('href')
            price = product.find('div',attrs={'class':'product-price'})
            ranting = product.find('div',class_="product-rating")
            print title+" "+href+" "+price+" "+ranting+" "


    def get_shop_feed_back(self):
        pass

if __name__=="__main__":
    shop = Shop("https://www.amazon.co.uk/gp/help/seller/at-a-glance.html/ref=dp_merchant_link?ie=UTF8&seller=A2UY2PPMCE8RY7&isAmazonFulfilled=1")
    shop.get_shop_id()
    shop.get_shop_info()
