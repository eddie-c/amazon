#coding:utf-8
import random
import tkMessageBox as messagebox
from bs4 import BeautifulSoup
import brotli
import re

class GlobalTools(object):

    baseurl = ""

    @classmethod
    def setbaseurl(cls,baseurl):
        cls.baseurl = baseurl

    @classmethod
    def getbaseurl(cls):
        return cls.baseurl

    @classmethod
    def getUserAgent(cls):
        user_agents = [
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        ]
        return random.choice(user_agents)

    @classmethod
    def getHeaders(cls):
        headers = {
            "Connection":"keep-alive",
            "Connection":"Transfer-Encoding",
            "Pragma":"no-cache",
            "Content-Type":"text/html;charset=UTF-8",
            # "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Cache-Control":"no-cache",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent": cls.getUserAgent(),
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Content-Encoding":"br",
            "Cookie":"""s_nr=1507528377078-New; s_vnum=1939528377079%26vn%3D1; s_dslv=1507528377080; x-wl-uid=1Vm2WQeeHRHErocdZmw5/GK41LYoPF67ySPkncJEPAiRRhWfNF0OyPa9yuT4S7+FNdyHQwhizugO0QMrffNe4I2JzXtJIy14CzCSmvUSme8lqhoZjjh77OF8sXJ/jQGXBcjMLuoUEESU=; at-acbuk=Atza|IwEBIOoVGprM0g2Qazrt-ifX53XNbsi7XFYs1OZNmIDgeZD6a5i2s7p4JuLWL6fC30oebF1OGUvU7z7HI266F0nMzVdpN8mWBQ1uOoa0XcmqZYdODKvv57Rq3jARRIaOoqkDAS6Ke6QFIjp1s1V6ZnPftLOOaz9uKLjRlvbMvtD57XnNZq2blSLo8IqJh0BhgpIH1K7cfEd7zgHGInlid0GyjKhMTaN5oRoZEzbvHAl9aHx15bRG8rKSbqpHQMeylRnYRnOirQGFgyPs2zQUp6YtUbivSlb8LGmOXL8aQaqZSE2lwyI3Sy9cGtDbBucHLB-OK4t89Rf5NIMRMSM-uMddzWr504Cg7_bOJ6RZFABsEDvdDEIItPRgnhrDksbMefih0AQSF8jnS9xXg3UbX9tqRbjA; amznacsleftnav-328511b4-0414-31f1-91c6-bca31c30900c=1; x-acbuk="DpcKYrm9@Uw75TNjTsXwmX79eaa3NMP2dk5ZlsVntw6MXujQjHcGEerpfDRFK8hR"; session-token="c4Zm/gVOVNPaG0sqPMSXyc1gSvo5FLQ1zSJiGIGtYyRTkLELs8YvdMxMDnJI6qSn4Js64xl0XcaoXI6lr8CYr7MgtlOwX8l5w1tHL3Oxj7XlR9TV+Lgi3RTkNyBBzYTkU3UN2dytZVNRmhz8r857X75WMVa/tDplddiQlzh1sal6qYJ+KrRk1JAb4ikjJshFVimJOIcVWnW/5uKa0PZ/xIHnRBfrNSFoYzokE6EWTTqlZ3ghsSSeb77CzyVQPWPhELEP+MukvVSmnFbNF7VTqw=="; lc-acbuk=en_GB; ubid-acbuk=261-6573040-2508135; session-id-time=2082758401l; session-id=259-7896668-2728509; csm-hit=STKFR5ZW99V4P01J7HXB+s-5690GGS4GQ2JJ9WFEP8D|1514354303483"""
        }
        return headers

    @classmethod
    def setCookie(cls,cookies):
        cls.cookies = cookies

    @classmethod
    def getCookie(cls):
        return cls.cookies

    @classmethod
    def getMarketplaceID(cls):
        return "A1F83G8C2ARO7P"

    @classmethod
    def getExcelFile(cls,countrycode):
        # return "./uk.xls"
        # return "./"+countrycode+".xls"
        return "d:/"+countrycode+".xls"


    @classmethod
    def getimgsavepath(cls, asin, extrainfo):
        return "./imgs/"+asin+"_"+extrainfo+".png"

    @classmethod
    def getSearchShopProductsUrl(cls):
        return "https://www.amazon.co.uk/sp/ajax/products"

    # def getSavePath(self):
    #     return "./uk.xls"

    @classmethod
    def get_table_header(self):
        return [u"商品链接",u"价格",u"店铺名称",u"商标",u"上架时间",u"QA:",u"STARS",u"好评",u"差评",u"好评点赞数",u"库存",u"一级分类",u"二级分类",u"排名"]

    @classmethod
    def get_search_products_pagesize(cls):
        return 12

    @classmethod
    def showMessage(cls,title,message):
        messagebox.askyesno(title, message)

    @classmethod
    def showerror(cls,title,message):
        messagebox.showerror(title,message)

    @classmethod
    def getResponseContent(cls,res):
        html = ""
        if res.headers['Content-Encoding'] == "br":
            html = BeautifulSoup(brotli.decompress(res.content), "lxml")
        else:
            html = BeautifulSoup(res.content, "lxml")
        return html

    @classmethod
    def removeBlankChars(cls,txt):
        out = re.sub(r"\s{2,}", " ", txt)
        return out

    @classmethod
    def getBaseurlFromCountrycode(cls,countrycode):
        countrycodemap = {
            "us":"https://www.amazon.com",
            "uk":"https://www.amazon.co.uk",
            "de":"https://www.amazon.de",
            "fr":"https://www.amazon.fr",
            "it":"https://www.amazon.it",
            "jp":"https://www.amazon.co.jp"
        }

        return countrycodemap[countrycode]

if __name__=="__main__":
    txt = "\n\n this is o ...hhaha \n\n    "
    print GlobalTools.removeBlankChars(txt)
