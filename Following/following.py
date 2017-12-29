from global_tools import GlobalTools
import requests
from bs4   import  BeautifulSoup
import brotli
def get_following_by_asin(asin,baseurl):
    headers = GlobalTools.getHeaders()

    url = baseurl+"/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="+str(asin)

    print "get url:"+url

    res = requests.get(url,headers=headers)

    # print "res:headers:"
    # print res.headers
    if res.headers['Content-Encoding'] == "br":
        html = BeautifulSoup(brotli.decompress(res.content),"lxml")
    else:
        html = BeautifulSoup(res.content,"lxml")

    tmp = open("tmp2.html","w+")
    if res.headers['Content-Encoding'] == "br":
        tmp.write(brotli.decompress(res.content))
    else:
        tmp.write(res.content)
    tmp.close()

    link = (html.find(id="s-results-list-atf")).find('a',attrs={'class':'s-access-detail-page'})
    links = (html.find(id="s-results-list-atf")).find_all('a')
    target = ""
    for link in links:
        if 'offer-listing' in link['href']:
            # print link.text.strip().split('(')
            if int(link.text.strip().split('(')[1].split()[0]) > 1:
                return [True,link['href']]
            else:
                return [False]
    else:
        return [False]

    # link = link.get('href')
    # link = link.split("&qid")[0]
    # print "link:"+link
    # return link
def getFlowingList(url):
    res = requests.get(url,headers=GlobalTools.getHeaders())
    if res.headers['Content-Encoding'] == "br":
        html = BeautifulSoup(brotli.decompress(res.content),"lxml")
    else:
        html = BeautifulSoup(res.content,"lxml")
    followerlist = html.find(id,"olpOfferList").find_all(class_="olpOffer")
    resultlist = []
    for follow in followerlist:
        followerNameElem = follow.find(class_="olpSellerName")
        if len(followerNameElem.find_all("a"))>0:
            followerName = followerNameElem.text
            url = GlobalTools.getBaseurlFromCountrycode("uk")+(followerNameElem.find("a"))['href']
        else:
            if len(followerNameElem.find_all("img"))>0:
                followerName = followerNameElem.find("img")['alt']
                url = "https://amazon.com"
            else:
                followerName = ""
                url = ""

        print (followerName,url)

if __name__=="__main__":
    res = get_following_by_asin("B004SH3SDM","https://www.amazon.co.uk")

    if res[0] is True:
        print res[1]
        getFlowingList(res[1])