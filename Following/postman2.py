import requests
import json
import time
import urllib
def getfba_by_update_2():
    itemid = "C4d213967-110f-44f8-88cb-a225d974ac71"
    asin = "B01H4ZBRWS"
    count = "10"
    requestid = "C9XAMS1M6BQZK4Y5JQ7A"
    timestamp = str(int(time.time()))
    url = "https://www.amazon.com/gp/cart/ajax-update.html/ref=ox_sc_update_quantity_1%7C2%7C"+count
    # payload = "actionItemID=C4d213967-110f-44f8-88cb-a225d974ac71&activeItems=C4d213967-110f-44f8-88cb-a225d974ac71%7C1%7C0%7C20%7C64.99%7C%7C%7C0%7C%7C&activeItems=Cdc761b6d-271d-4fdd-8613-2cd580061b50%7C1%7C0%7C1%7C39.99%7C%7C%7C0%7C%7C&addressId=&addressZip=&asin=B01EJJDD10&closeAddonUpsell=1&encodedOffering=0Jg2vDRaG%252FFyiHgyM3AaaW%252BVvzDO0yJq11%252Fq3RZsszYz870SgsbNx8%252F5di79nkAM5yYVf1QY1JQujn8xzEWbZS2U3uEhVCaLxj03p9ruiG6WXECDGLbV9wMrtcOE90a%252FPlx85euThLk%252Bo1BfeIpz7w%253D%253D&flcExpanded=0&hasMoreItems=0&pageAction=update-quantity&quantity.C4d213967-110f-44f8-88cb-a225d974ac71=15&requestID=C9XAMS1M6BQZK4Y5JQ7A&submit.update-quantity.C4d213967-110f-44f8-88cb-a225d974ac71=1&timeStamp=1514529999&token=gM0QUIFnl%2B%2BWRRi4qoB9fthlAso5k29jRXmsGQUAAAAJAAAAAFpF5M9yYXcAAAAA"
    # payload = "actionItemID=%s&activeItems=%s&addressId=&addressZip=&asin=%s&closeAddonUpsell=1&encodedOffering=0Jg2vDRaG%252FFyiHgyM3AaaW%252BVvzDO0yJq11%252Fq3RZsszYz870SgsbNx8%252F5di79nkAM5yYVf1QY1JQujn8xzEWbZS2U3uEhVCaLxj03p9ruiG6WXECDGLbV9wMrtcOE90a%252FPlx85euThLk%252Bo1BfeIpz7w%253D%253D&flcExpanded=0&hasMoreItems=0&pageAction=update-quantity&quantity.%s=%s&requestID=%s&submit.update-quantity.C4d213967-110f-44f8-88cb-a225d974ac71=1&timeStamp=%s&token=gM0QUIFnl%2B%2BWRRi4qoB9fthlAso5k29jRXmsGQUAAAAJAAAAAFpF5M9yYXcAAAAA" %
    # (itemid,itemid,asin,requestid,,timestamp)

    timestamp = str(int(time.time()))
    payload = """actionItemID={0}
                    &activeItems={1}
                    |1|0|16|30|||0||&addressId=&addressZip=&asin={2}
                    &closeAddonUpsell=1&encodedOffering=0Jg2vDRaG%252FFyiHgyM3AaaW%252BVvzDO0yJq11%252Fq3RZsszYz870SgsbNx8%252F5di79nkAM5yYVf1QY1JQujn8xzEWbZS2U3uEhVCaLxj03p9ruiG6WXECDGLbV9wMrtcOE90a%252FPlx85euThLk%252Bo1BfeIpz7w%253D%253D&flcExpanded=0&hasMoreItems=0&pageAction=update-quantity&quantity.{3}
                    ={4}
                    &requestID={5}
                    &submit.update-quantity.{6}
                    =1&timeStamp={7}
                    &token=gM0QUIFnl%2B%2BWRRi4qoB9fthlAso5k29jRXmsGQUAAAAJAAAAAFpF5M9yYXcAAAAA""".format(
                    itemid,
                    itemid,
                    asin,
                    itemid,
                    count,
                    requestid,
                    itemid,
        "1514529999").replace(" ","").replace("\n","")

    print payload
    headers = {
        'origin': "https://www.amazon.com",
        'x-aui-view': "Desktop",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'accept': "application/json, text/javascript, */*; q=0.01",
        'x-devtools-emulate-network-conditions-client-id': "05052e3d-86a0-4636-880b-be05c10dd982",
        'x-requested-with': "XMLHttpRequest",
        'referer': "https://www.amazon.com/gp/cart/view.html/ref=nav_cart",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.8",
        'cookie': "skin=noskin; x-wl-uid=14q8KRz8oS2Y0C58RUJqGijItRR8rBqZH1n0ytlg1+RV6MasLnaawSwgPmwW3YWnHxPdIwtta4Lg=; session-token=01hb1Y1NR6+6RymcfvjrXUtrzRBYkMYKxcZUobBg2UCzQao8rEHWQVKdyYrv2FlJ9eKaaIJlsTHiAOtSvxlHrers1InTvarz/yCc7QERoroFPm56IHQF2YY29SQpUTrd/yQeNAdhbRXpP2OUytX+Y/NDNVGHVTrPc2SJ0NGycTLHUTQM8nUACJt6JSQthiy4; csm-hit=YRXX3Y8BYGD2TNS2BMTH+s-Y73H1PWETVV03KVKBHX5|1514525576618; ubid-main=130-4959715-9713731; session-id-time=2082787201l; session-id=142-3848605-8806937; skin=noskin; x-wl-uid=14q8KRz8oS2Y0C58RUJqGijItRR8rBqZH1n0ytlg1+RV6MasLnaawSwgPmwW3YWnHxPdIwtta4Lg=; session-token=01hb1Y1NR6+6RymcfvjrXUtrzRBYkMYKxcZUobBg2UCzQao8rEHWQVKdyYrv2FlJ9eKaaIJlsTHiAOtSvxlHrers1InTvarz/yCc7QERoroFPm56IHQF2YY29SQpUTrd/yQeNAdhbRXpP2OUytX+Y/NDNVGHVTrPc2SJ0NGycTLHUTQM8nUACJt6JSQthiy4; csm-hit=YRXX3Y8BYGD2TNS2BMTH+s-6820N5FF5BNA5SYMECT6|1514529456871; ubid-main=130-4959715-9713731; session-id-time=2082787201l; session-id=142-3848605-8806937",
        'cache-control': "no-cache",
        'postman-token': "b64e3376-1fa0-8b92-4bc7-3d17f6787ed6"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    # print(response.text)
    # json.dumps(response.text)
    jsonobj = json.loads(response.content, encoding="utf-8")
    print jsonobj['features']['imb']['featurehtml']
    print jsonobj['features']['nav-cart']

getfba_by_update_2()