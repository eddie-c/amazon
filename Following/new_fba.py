import requests
import time
from global_tools import GlobalTools
import json
import httplib
import urllib


def newfba(asin):
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        # "Content-Length":"547",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        # "Content-Type": "text/html;charset=UTF-8",
        "Host":"www.amazon.co.uk",
        "Origin":"https://www.amazon.co.uk",
        "Content-Encoding": "br",
        "Pragma":"no-cache",
        "Referer": "https://www.amazon.co.uk/gp/cart/view.html/ref=lh_cart_vc_btn",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "X-AUI-View": "Desktop",
        "X-Requested-With":"XMLHttpRequest",
        "Cookie":"""s_nr=1507528377078-New; s_vnum=1939528377079%26vn%3D1; s_dslv=1507528377080; x-wl-uid=1Vm2WQeeHRHErocdZmw5/GK41LYoPF67ySPkncJEPAiRRhWfNF0OyPa9yuT4S7+FNdyHQwhizugO0QMrffNe4I2JzXtJIy14CzCSmvUSme8lqhoZjjh77OF8sXJ/jQGXBcjMLuoUEESU=; at-acbuk=Atza|IwEBIOoVGprM0g2Qazrt-ifX53XNbsi7XFYs1OZNmIDgeZD6a5i2s7p4JuLWL6fC30oebF1OGUvU7z7HI266F0nMzVdpN8mWBQ1uOoa0XcmqZYdODKvv57Rq3jARRIaOoqkDAS6Ke6QFIjp1s1V6ZnPftLOOaz9uKLjRlvbMvtD57XnNZq2blSLo8IqJh0BhgpIH1K7cfEd7zgHGInlid0GyjKhMTaN5oRoZEzbvHAl9aHx15bRG8rKSbqpHQMeylRnYRnOirQGFgyPs2zQUp6YtUbivSlb8LGmOXL8aQaqZSE2lwyI3Sy9cGtDbBucHLB-OK4t89Rf5NIMRMSM-uMddzWr504Cg7_bOJ6RZFABsEDvdDEIItPRgnhrDksbMefih0AQSF8jnS9xXg3UbX9tqRbjA; amznacsleftnav-328511b4-0414-31f1-91c6-bca31c30900c=1; x-acbuk="DpcKYrm9@Uw75TNjTsXwmX79eaa3NMP2dk5ZlsVntw6MXujQjHcGEerpfDRFK8hR";session-token=9SQ2EeLcEOiWNXk9Km/DNS6S1V0UZwProvVruiPJrCVgmxhyesgqA/fp58r9T9x2sKqlQqrsEEER26oL2mWsLSDfPDsZIgbKwHiWox5/i0IB0R8heds6DI1HK15chFLvoLUg/J8JaqgwtAoINSoQpvXPRngz83hB73b9x54TmuIuxH8LyuVsQlHkt5CeOaWAKHpif0qNYASaMLmf/Q0EDRW8RO0yBFk+SPYTIZwRv8wy4200Mchhe4UhrsdJOX4aubGsciZgiUtFN7fjp4F4NQ=="; lc-acbuk=en_GB; ubid-acbuk=261-6573040-2508135; session-id-time=2082758401l; session-id=259-7896668-2728509; csm-hit=DQ3DSN2G6C2P8DBSE4K4+s-4CDTDE03S82FARC6XGS1|1514455697049"""
    }

    url = "https://www.amazon.co.uk/gp/cart/ajax-update.html/ref=ox_sc_update_quantity_1%7C9%7C11"

    data = {
        "hasMoreItems":0,
        "timeStamp":1514454024,
        "token":"gFHNsVRD27zMiOpe+yYpwFsAOZohN8u+a5VmqKkAAAAJAAAAAFpEvAhyYXcAAAAA",
        "activeItems":"C31HAVQP205TNO|1|0|5|3.05|||0||",
        "addressId":"",
        "addressZip":"",
        "closeAddonUpsell":1,
        "flcExpanded":0,
        "quantity.C31HAVQP205TNO":"11",
        "pageAction":"update-quantity",
        "submit.update-quantity.C31HAVQP205TNO":"1",
        "actionItemID":"C31HAVQP205TNO",
        "requestID":"EFHWWNTW6V3PRPMTQVWY",
        "asin":"B003KN7PU2",
        "encodedOffering":"%2BMwdK243Pp3oHjtzeyP6rdX8pnsybQAfRMa%2FX803XTXSTS7T%2BThAv741wG3TqvzM2kBUhnHpgojcF03P1%2FiSGuiN%2F5D6331v80WV2YLu2HU%3D"
    }

    # headers = urllib.quote(json.dumps(headers))
    comm_params = urllib.quote(json.dumps(data))
    request = requests.session()
    request.get("https://www.amazon.co.uk",headers=GlobalTools.getHeaders())
    # res = request.post(url,headers=headers,data=comm_params)
    res = requests.post(url,headers=headers,data=comm_params)
    print res.content
    jsonobj = json.loads(res.content,encoding="utf-8")
    print jsonobj['features']['imb']
    print jsonobj['features']['nav-cart']


if __name__=="__main__":
    # asin = "B00NHRX0GO"
    asin = "B003KN7PU2"
    newfba(asin)