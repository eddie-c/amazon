import time
itemid = "C4d213967-110f-44f8-88cb-a225d974ac71"
asin = "B01EJJDD10"
count = "999"
requestid = "C9XAMS1M6BQZK4Y5JQ7A"
timestamp = str(int(time.time()))
payload = """actionItemID={0}
                &activeItems={1}
                &addressId=&addressZip=&asin={2}
                &closeAddonUpsell=1&encodedOffering=0Jg2vDRaG%252FFyiHgyM3AaaW%252BVvzDO0yJq11%252Fq3RZsszYz870SgsbNx8%252F5di79nkAM5yYVf1QY1JQujn8xzEWbZS2U3uEhVCaLxj03p9ruiG6WXECDGLbV9wMrtcOE90a%252FPlx85euThLk%252Bo1BfeIpz7w%253D%253D&flcExpanded=0&hasMoreItems=0&pageAction=update-quantity&quantity{3}
                ={4}
                &requestID={5}
                &submit.update-quantity{6}
                =1&timeStamp={7}
                &token=gM0QUIFnl%2B%2BWRRi4qoB9fthlAso5k29jRXmsGQUAAAAJAAAAAFpF5M9yYXcAAAAA""".format(
                itemid,
                itemid,
                asin,
                itemid,
                count,
                requestid,
                itemid,
                timestamp)
print payload.replace(" ","").replace("\n","")