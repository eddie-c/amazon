import requests
from bs4 import BeautifulSoup
import json
from global_tools import GlobalTools

class Products(object):
    def __init__(self,seller):
        self.marketplaceid = GlobalTools.getMarketplaceID()
        self.headers = GlobalTools.getHeaders()
        self.url = GlobalTools.getSearchShopProductsUrl()
        self.seller = seller

    def get_page_size(self):
        # return 12
        return 20

    def get_one_page(self,page_num):
        # print "page_num:"+str(page_num)
        # s = r'{"marketplace":"A1F83G8C2ARO7P","seller":"A2UY2PPMCE8RY7","url":"/sp/ajax/products","pageSize":40,"searchKeyword":"","extraRestrictions":{},"pageNumber":'+str(page_num)+"}"
        # print s
        # data = {
        #     'productSearchRequestData': {
        #         "marketplace": "A1F83G8C2ARO7P",
        #         "seller": "A2UY2PPMCE8RY7",
        #         "url": "/sp/ajax/products",
        #         "pageSize": 12,
        #         "searchKeyword": "",
        #         "extraRestrictions":{},
        #         "pageNumber":page_num
        #     },
        #     'marketplaceID': self.marketplaceid,
        #     'seller': self.seller
        # }
        page_size = self.get_page_size()
        s = r'{"marketplace":"A1F83G8C2ARO7P","seller":"A2UY2PPMCE8RY7","url":"/sp/ajax/products","pageSize":%s,"searchKeyword":"","extraRestrictions":{},"pageNumber":%s}'%(str(page_size),str(page_num))

        data = {
            'productSearchRequestData': s,
            'marketplaceID': self.marketplaceid,
            'seller': self.seller
        }

        headers = {
            "Host": "www.amazon.co.uk",
            "Connection": "keep-alive",
            "Content-Length": "315",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Origin": "https://www.amazon.co.uk",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://www.amazon.co.uk/sp?_encoding=UTF8&asin=&isAmazonFulfilled=1&isCBA=&marketplaceID=A1F83G8C2ARO7P&orderID=&seller=A2UY2PPMCE8RY7&tab=&vasStoreID=",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "Cookie": """s_nr=1507528377078-New; s_vnum=1939528377079%26vn%3D1; s_dslv=1507528377080; x-wl-uid=1Vm2WQeeHRHErocdZmw5/GK41LYoPF67ySPkncJEPAiRRhWfNF0OyPa9yuT4S7+FNdyHQwhizugO0QMrffNe4I2JzXtJIy14CzCSmvUSme8lqhoZjjh77OF8sXJ/jQGXBcjMLuoUEESU=; at-acbuk=Atza|IwEBIOoVGprM0g2Qazrt-ifX53XNbsi7XFYs1OZNmIDgeZD6a5i2s7p4JuLWL6fC30oebF1OGUvU7z7HI266F0nMzVdpN8mWBQ1uOoa0XcmqZYdODKvv57Rq3jARRIaOoqkDAS6Ke6QFIjp1s1V6ZnPftLOOaz9uKLjRlvbMvtD57XnNZq2blSLo8IqJh0BhgpIH1K7cfEd7zgHGInlid0GyjKhMTaN5oRoZEzbvHAl9aHx15bRG8rKSbqpHQMeylRnYRnOirQGFgyPs2zQUp6YtUbivSlb8LGmOXL8aQaqZSE2lwyI3Sy9cGtDbBucHLB-OK4t89Rf5NIMRMSM-uMddzWr504Cg7_bOJ6RZFABsEDvdDEIItPRgnhrDksbMefih0AQSF8jnS9xXg3UbX9tqRbjA; amznacsleftnav-328511b4-0414-31f1-91c6-bca31c30900c=1; lc-acbuk=en_GB; session-id=259-7896668-2728509; session-id-time=2082787201l; ubid-acbuk=261-6573040-2508135; x-acbuk="DpcKYrm9@Uw75TNjTsXwmX79eaa3NMP2dk5ZlsVntw6MXujQjHcGEerpfDRFK8hR"; session-token="c4Zm/gVOVNPaG0sqPMSXyc1gSvo5FLQ1zSJiGIGtYyRTkLELs8YvdMxMDnJI6qSn4Js64xl0XcaoXI6lr8CYr7MgtlOwX8l5w1tHL3Oxj7XlR9TV+Lgi3RTkNyBBzYTkU3UN2dytZVNRmhz8r857X75WMVa/tDplddiQlzh1sal6qYJ+KrRk1JAb4ikjJshFVimJOIcVWnW/5uKa0PZ/xIHnRBfrNSFoYzokE6EWTTqlZ3ghsSSeb77CzyVQPWPhELEP+MukvVSmnFbNF7VTqw=="; csm-hit=STKFR5ZW99V4P01J7HXB+b-5690GGS4GQ2JJ9WFEP8D|1514354880407"""
        }
        print data

        res = requests.post(self.url, headers=headers, data=data)
        # open("tmp.html","w+").write(res.text)
        # print res.text
        jsonstr = json.loads(res.text)
        print jsonstr
        products = jsonstr['products']
        print len(products)
        for product in products:
            self.parse_product(product)

    def get_products_by_shop(self):
        page_count = self.get_page_count()
        for i in range(1, page_count+1):
            self.get_one_page(i)

    def get_product_count(self):
        # url = GlobalTools.getbaseurl()+"/s?merchant="+self.seller+"&fallThrough=1"
        url = "https://www.amazon.co.uk"+ "/s?merchant="+self.seller+"&fallThrough=1"
        res = requests.get(url, headers=self.headers)
        html = BeautifulSoup(res.text,"lxml")
        raw_count = html.find(id="s-result-count")
        print raw_count.text
        count = int(raw_count.text.split("of")[1].split('results')[0].strip())
        return count

    def get_page_count(self):
        # total = self.get_product_count()
        # page_size = self.get_page_size()
        # if total % page_size == 0:
        #     return total/page_size
        # else:
        #     return total/page_size+1
        return 1


    def parse_product(self,jsonstr):
        # print jsonstr['title']['expandedText']
        # print jsonstr['price']
        # print jsonstr['formattedRating']
        # print jsonstr['ratingFullStars']
        # print jsonstr['ratingCount']
        # print jsonstr['imageData']['imageURL']
        print "asin:"+jsonstr['reviewURL'].split("product-reviews/")[1].split("?ref")[0]

if __name__=="__main__":
    pro = Products("A2UY2PPMCE8RY7")
    pro.get_products_by_shop()