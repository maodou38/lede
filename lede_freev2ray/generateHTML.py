'''
根据爬取的vmess生成订阅页面
'''

from freev2ray import FreeV2ray
import base64
import time
from datetime import datetime
import os
f = open("/www/v2ray/index.html", "r+")
oldline = f.read()

code = bytes("", encoding="utf-8")

vmess = FreeV2ray().getVmessFromWeb()
code = base64.b64encode(vmess.encode("utf-8"))
if oldline.strip() != str(code.decode("utf-8")).strip():
    f.seek(0)
    f.truncate()
    f.write(code.decode("utf-8"))
    dayOfWeek = datetime.now().isoweekday()
    if(dayOfWeek == 7):
      os.system("/usr/share/shadowsocksr/ssrplusupdate.sh >>/dev/null 2>&1")
    else:
      os.system("/usr/bin/lua /usr/share/shadowsocksr/subscribe.lua >>/dev/null 2>&1")
f.close()