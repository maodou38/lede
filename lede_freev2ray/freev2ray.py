import requests
import bs4
import re
import time

'''
从网站上爬取域名 端口 UUID alterID信息
'''
requests.packages.urllib3.disable_warnings

class FreeV2ray(object):
    def __init__(self):
        self.url = "https://view.freev2ray.org/"

    def getParamFromWeb(self):
        response=self.getHtmlFromPage()
        content = bs4.BeautifulSoup(response.content.decode("utf-8"), "html.parser")
        address = content.find('span', id='ip').text
        port = content.find('span', id='port').text
        uuid = content.find('span', id='uuid').text
        alterID = re.findall(r"AlterID:\s*(.+?)", response.text)[0]
        return address, port, uuid, alterID

    def getVmessFromWeb(self):
        response = self.getHtmlFromPage()
        content = bs4.BeautifulSoup(response.content.decode("utf-8"), "html.parser")
        vmess = content.find('button', class_='copybtn').get("data-clipboard-text")
        return vmess

    def getHtmlFromPage(self):
        while True:
            #忽略验证证书
            response = requests.get(self.url, verify=False)
            if response.status_code != 200:
                time.sleep(60)
            else:
                return response

