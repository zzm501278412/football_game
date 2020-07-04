import requests
import threading
import time
from lxml import etree
import random
import config
def update_result():
    url='https://live.500.com/zqdc.php'
    header={
        'user-agent':random.choice(config.userAgent),
        "cookie":config.cookie,
        'referer':'https://live.500.com/'
    }
    re=requests.get(url=url,headers=header)

    re.encoding='gb2312'
    data=etree.HTML(re.text)
    matchNo=data.xpath('//body//div[6]//div[1]/table//tbody//td[1]//input//@value')
    result=data.xpath('//body//div[6]//div[1]/table//tbody//td[9]//text()')
    a=[]
    for i in result:
        if i==' - ':
            a.append("")
        else:
            i=i.replace(" - ",":")
            a.append(i)
    c=[]
    for i in range(len(result)):
        getData={

        "matchNo":matchNo[i],
        "result": a[i],
    }
        print(getData)
        c.append(getData)
    requestsData=requests.post(url="http://127.0.0.1:80/api/update_result.do",json=c)
    print(requestsData.json())
if __name__ == '__main__':
    pass