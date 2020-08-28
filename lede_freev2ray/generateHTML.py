'''
根据爬取的vmess生成订阅页面
'''

from freev2ray import FreeV2ray
import base64
import time
f = open("/www/v2ray/index.html", "r+")
oldline = f.read()
flag = False
code = bytes("", encoding="utf-8")
while not flag:
    vmess = FreeV2ray().getVmessFromWeb()
    print("vmess:" + vmess)
    code = base64.b64encode(vmess.encode("utf-8"))
    if oldline.strip() != str(code.decode("utf-8")).strip():
        print("oldline:" + oldline.strip())
        print("newline:" + str(code.decode("utf-8")).strip())
        flag = True
    else:
        time.sleep(10)
f.seek(0)
f.truncate()
f.write(code.decode("utf-8"))
f.close()
