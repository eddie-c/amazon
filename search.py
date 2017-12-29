from global_tools import GlobalTools
import requests
from bs4 import BeautifulSoup
import brotli
import logging
import traceback

def get_link_by_asin(asin,baseurl):
    # print "in get_link_by_asin"
    headers = GlobalTools.getHeaders()
    # baseurl = "http://www.amazon.co.uk"
    url = baseurl+"/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="+str(asin)
    # url = baseurl
    # print url

    # url:search - alias = aps
    # field - keywords:B01KGUMWJU
    params = {
        # "url":"search-alias=aps",
        # "field-keywords":asin
    }
    # proxies = {
    #     "http":"123.148.74.107:80",
    #     "https": "218.18.10.11:9797"
    # }
    print "get url:"+url

    res = requests.get(url,headers=headers)

    print "res:headers:"
    print res.headers
    if res.headers['Content-Encoding'] == "br":
        html = BeautifulSoup(brotli.decompress(res.content),"lxml")
    else:
        html = BeautifulSoup(res.content,"lxml")
    # html = BeautifulSoup(res.content, "lxml")

    tmp = open("tmp2.html","w+")
    if res.headers['Content-Encoding'] == "br":
        tmp.write(brotli.decompress(res.content))
    else:
        tmp.write(res.content)
    tmp.close()

    # print "url:"+url
    # print html.find(id="centerMinus")
    # link = html.find(id="s-results-list-atf")
    link = (html.find(id="s-results-list-atf")).find('a',attrs={'class':'s-access-detail-page'})
    link = link.get('href')
    link = link.split("&qid")[0]
    print "link:"+link
    return link

if __name__=="__main__":
    get_link_by_asin('B01MYPXWYV',"http://www.amazon.co.uk")