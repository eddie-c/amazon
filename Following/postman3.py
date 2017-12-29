import requests
import json
from bs4 import BeautifulSoup
import time

def getfba_by_update(asin,item_id,requestid):
    url = "https://www.amazon.com/gp/cart/ajax-update.html/ref=ox_sc_update_quantity_1%7C1%7C999"
    # payload = "actionItemID=C31HAVQP205TNO&activeItems=C31HAVQP205TNO|1|0|9|3.05|||0||&addressId=&addressZip=&asin=B003KN7PU2&closeAddonUpsell=1&encodedOffering=%2BMwdK243Pp3oHjtzeyP6rdX8pnsybQAfRMa%2FX803XTXSTS7T%2BThAv741wG3TqvzM2kBUhnHpgojcF03P1%2FiSGuiN%2F5D6331v80WV2YLu2HU%3D&flcExpanded=0&hasMoreItems=0&pageAction=update-quantity&quantity.C31HAVQP205TNO=11&requestID=K8N8W33AV98PJ0TBZ4RR&submit.update-quantity.C31HAVQP205TNO=1&timeStamp=1514513902&token=gK1aKeOzd3vavPBJ0WPhgjWe8a95/Nrk0vV6foYAAAAJAAAAAFpFpe5yYXcAAAAA"
#     payload = {
#         """
#         actionItemID:C3764de27-a5cc-4511-88d6-e18a5f4fdabe
# activeItems:C3764de27-a5cc-4511-88d6-e18a5f4fdabe|1|0|4|64.99|||0||
# activeItems:Cdc761b6d-271d-4fdd-8613-2cd580061b50|1|0|1|39.99|||0||
# addressId:
# addressZip:
# asin:B01EJJDD10
# closeAddonUpsell:1
# encodedOffering:0Jg2vDRaG%2FFyiHgyM3AaaW%2BVvzDO0yJq11%2Fq3RZsszYz870SgsbNx8%2F5di79nkAM5yYVf1QY1JQujn8xzEWbZS2U3uEhVCaLxj03p9ruiG6WXECDGLbV9wMrtcOE90a%2FPlx85euThLk%2Bo1BfeIpz7w%3D%3D
# flcExpanded:0
# hasMoreItems:0
# pageAction:update-quantity
# quantity.C3764de27-a5cc-4511-88d6-e18a5f4fdabe:999
# requestID:6820N5FF5BNA5SYMECT6
# submit.update-quantity.C3764de27-a5cc-4511-88d6-e18a5f4fdabe:1
# timeStamp:1514529446
# token:gJ3rK7ddlSKGILpM6hfDeWpWjaBaNNGiMtrb41cAAAAJAAAAAFpF4qZyYXcAAAAA
#         """
#     }
    payload = {
        "actionItemID":item_id,
        "activeItems":item_id+"|1|0|17|64.99|||0||",
        "addressId":"",
        "addressZip":"",
        "asin":asin,
        "closeAddonUpsell":"1",
        "encodedOffering":"0Jg2vDRaG%2FFyiHgyM3AaaW%2BVvzDO0yJq11%2Fq3RZsszYz870SgsbNx8%2F5di79nkAM5yYVf1QY1JQujn8xzEWbZS2U3uEhVCaLxj03p9ruiG6WXECDGLbV9wMrtcOE90a%2FPlx85euThLk%2Bo1BfeIpz7w%3D%3D",
        "flcExpanded":"0",
        "hasMoreItems":"0",
        "pageAction":"update-quantity",
        "quantity."+item_id:"999",
        "requestID":requestid,
        "submit.update-quantity."+item_id:"1",
        "timeStamp":int(time.time()),
        "timeStamp":"1514529999",
        "token":"gJ3rK7ddlSKGILpM6hfDeWpWjaBaNNGiMtrb41cAAAAJAAAAAFpF4qZyYXcAAAAA",
    }
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
    print(response.text)
    # json.dumps(response.text)
    jsonobj = json.loads(response.content, encoding="utf-8")
    print jsonobj['features']['imb']['featurehtml']
    print jsonobj['features']['nav-cart']



def add_to_cart(asin):
    url = "https://www.amazon.com/gp/item-dispatch/ref=pd_cart_cp_1_atc_1"

    querystring = {"ie": "UTF8", "pd_rd_r": "N05KH7AT0QQM0DP1RF3B", "pd_rd_w": "GvuOm", "pd_rd_wg": "23xYs",
                   "refRID": "N05KH7AT0QQM0DP1RF3B"}

    payload = {
        "asin.B01EJJDD10":"B01EJJDD10",
        "discoveredAsins.1":"B01EJJDD10",
        "offeringID.B01EJJDD10":"0Jg2vDRaG%2FFyiHgyM3AaaW%2BVvzDO0yJq11%2Fq3RZsszYz870SgsbNx8%2F5di79nkAM5yYVf1QY1JQujn8xzEWbZS2U3uEhVCaLxj03p9ruiG6WXECDGLbV9wMrtcOE90a%2FPlx85euThLk%2Bo1BfeIpz7w%3D%3D",
        "quantity.B01EJJDD10":"1",
        "session-id":"142-3848605-8806937",
        "submit.addToCart":"Add to Cart"
    }
    headers = {
        'origin': "https://www.amazon.com",
        'upgrade-insecure-requests': "1",
        'content-type': "application/x-www-form-urlencoded",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'referer': "https://www.amazon.com/gp/cart/view.html/ref=lh_cart",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.8",
        'cookie': "skin=noskin; x-wl-uid=14q8KRz8oS2Y0C58RUJqGijItRR8rBqZH1n0ytlg1+RV6MasLnaawSwgPmwW3YWnHxPdIwtta4Lg=; session-token=01hb1Y1NR6+6RymcfvjrXUtrzRBYkMYKxcZUobBg2UCzQao8rEHWQVKdyYrv2FlJ9eKaaIJlsTHiAOtSvxlHrers1InTvarz/yCc7QERoroFPm56IHQF2YY29SQpUTrd/yQeNAdhbRXpP2OUytX+Y/NDNVGHVTrPc2SJ0NGycTLHUTQM8nUACJt6JSQthiy4; csm-hit=YRXX3Y8BYGD2TNS2BMTH+sa-809Z9H741SHYECZC3BFV-D3DVB22N5VF1GBQ41VS5|1514521768930; ubid-main=130-4959715-9713731; session-id-time=2082787201l; session-id=142-3848605-8806937",
        'cache-control': "no-cache",
        'postman-token': "0e9645c5-9ebe-3560-1445-547b4ac59667"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    html = BeautifulSoup(response.text,"lxml")
    itemid = html.find("input",{"name":"hucArgsNewItems"})['value'].split(",")[0]
    print itemid
    requestid = json.loads(html.find(id="rhf-context").find("script").text.strip())['rhfHandlerParams']['relatedRequestId']
    print requestid
    return [itemid,requestid]
    # print(response.text)


def delete_cart_item():
    url = "https://www.amazon.com/gp/cart/ajax-update.html/ref=ox_sc_cart_delete_1"

    payload = {
        "hasMoreItems":"0",
        "timeStamp":"1514521978",
        "token":"gPD07nISq8FFfJagZ1z9Nx+zF7WlwUhV3MrEzg8AAAAJAAAAAFpFxXpyYXcAAAAA",
        "requestID":"0G8YD042HQBTDRRNJWF9",
        "activeItems":"Cc27efb7a-ffcd-40c8-9087-058fd107581a|1|0|2|64.99|||0||",
        "addressId":"",
        "addressZip":"",
        "closeAddonUpsell":"1",
        "flcExpanded":"0",
        "submit.delete.Cc27efb7a-ffcd-40c8-9087-058fd107581a":"1",
        "pageAction":"delete-active",
        "actionItemID":"Cc27efb7a-ffcd-40c8-9087-058fd107581a",
        "asin":"B01EJJDD10",
        "encodedOffering":"0Jg2vDRaG%2FFyiHgyM3AaaW%2BVvzDO0yJq11%2Fq3RZsszYz870SgsbNx8%2F5di79nkAM5yYVf1QY1JQujn8xzEWbZS2U3uEhVCaLxj03p9ruiG6WXECDGLbV9wMrtcOE90a%2FPlx85euThLk%2Bo1BfeIpz7w%3D%3D",

    }
    headers = {
        'origin': "https://www.amazon.com",
        'x-aui-view': "Desktop",
        'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'accept': "application/json, text/javascript, */*; q=0.01",
        # 'x-devtools-emulate-network-conditions-client-id': "05052e3d-86a0-4636-880b-be05c10dd982",
        'x-requested-with': "XMLHttpRequest",
        'referer': "https://www.amazon.com/gp/cart/view.html/ref=lh_cart",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.8",
        'cookie': "skin=noskin; x-wl-uid=14q8KRz8oS2Y0C58RUJqGijItRR8rBqZH1n0ytlg1+RV6MasLnaawSwgPmwW3YWnHxPdIwtta4Lg=; session-token=01hb1Y1NR6+6RymcfvjrXUtrzRBYkMYKxcZUobBg2UCzQao8rEHWQVKdyYrv2FlJ9eKaaIJlsTHiAOtSvxlHrers1InTvarz/yCc7QERoroFPm56IHQF2YY29SQpUTrd/yQeNAdhbRXpP2OUytX+Y/NDNVGHVTrPc2SJ0NGycTLHUTQM8nUACJt6JSQthiy4; ubid-main=130-4959715-9713731; session-id-time=2082787201l; session-id=142-3848605-8806937; csm-hit=YRXX3Y8BYGD2TNS2BMTH+s-0G8YD042HQBTDRRNJWF9|1514522185463",
        'cache-control': "no-cache",
        # 'postman-token': "097a610c-54b4-3965-ab24-4ba44be1dc36"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
asin = "B01EJJDD10"
[itemid,requestid] = add_to_cart(asin)
print itemid,requestid
getfba_by_update(asin,itemid,requestid)
# delete_cart_item(itemid)
