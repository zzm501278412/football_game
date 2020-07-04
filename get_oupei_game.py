import requests
import threading
import time
from lxml import etree
import random
import config
from get_game_id import *

def get_oupei_30_data(data):
    try:
        time.sleep(2)
        getDateUrl = 'https://odds.500.com/fenxi/ouzhi-%s.shtml'%data['gameId']
        header = {
            "user-agent": random.choice(config.userAgent),
            "referer": "https://odds.500.com/",
            "cookie": config.cookie
        }
        re = requests.get(getDateUrl, headers=header)
        re.encoding = 'gb2312'
        result = etree.HTML(re.text)

        companyName = result.xpath("//tr[contains(@class,'tr1')]//td[contains(@class,'tb_plgs')]/@title") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[contains(@class,'tb_plgs')]/@title")
        # 公司id
        companyId = result.xpath("//tr[contains(@class,'tr1')]/@id") + result.xpath("//tr[contains(@class,'tr2')]/@id")
        # 变化时间
        europeFlushTime = result.xpath("//tr[contains(@class,'tr1')]//@data-time") + result.xpath(
            "//tr[contains(@class,'tr2')]//@data-time")
        # 胜赔率
        win = result.xpath("//tr[contains(@class,'tr1')]//td[3]//tr[2]//td[1]//text()") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[3]//tr[2]//td[1]//text()")
        # 胜赔率涨跌标识
        winZd = result.xpath("//tr[contains(@class,'tr1')]//td[3]//td[1]//@class") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[3]//td[1]//@class")
        # 平赔率
        draw = result.xpath("//tr[contains(@class,'tr1')]//td[3]//tr[2]//td[2]//text()") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[3]//tr[2]//td[2]//text()")
        # 平赔率涨跌标识
        drawZd = result.xpath("//tr[contains(@class,'tr1')]//td[3]//td[2]//@class") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[3]//td[2]//@class")
        # 负赔率
        loss = result.xpath("//tr[contains(@class,'tr1')]//td[3]//tr[2]//td[3]//text()") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[3]//tr[2]//td[3]//text()")

        # 负赔率涨跌标识
        lossZd = result.xpath("//tr[contains(@class,'tr1')]//td[3]//td[3]//@class") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[3]//td[3]//@class")

        # 胜凯利
        winKeiliIndex = result.xpath("//tr[contains(@class,'tr1')]//td[6]//tr[2]//td[1]//text()") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[6]//tr[2]//td[1]//text()"
        )
        # 平凯利
        drawKeiliIndex = result.xpath("//tr[contains(@class,'tr1')]//td[6]//tr[2]//td[2]//text()") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[6]//tr[2]//td[2]//text()"
        )
        # 负凯利
        lossKeiliIndex = result.xpath("//tr[contains(@class,'tr1')]//td[6]//tr[2]//td[3]//text()") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[6]//tr[2]//td[3]//text()"
        )
        # 胜概率
        winProb = result.xpath("//tr[contains(@class,'tr1')]//td[4]//tr[2]//td[1]//text()") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[4]//tr[2]//td[1]//text()")
        # 平概率
        drawProb = result.xpath("//tr[contains(@class,'tr1')]//td[4]//tr[2]//td[2]//text()") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[4]//tr[2]//td[2]//text()")
        # 负概率
        lossProb = result.xpath("//tr[contains(@class,'tr1')]//td[4]//tr[2]//td[3]//text()") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[4]//tr[2]//td[3]//text()")
        a = []
        for i in winProb:
            i = i[0:5]
            a.append(i)
        b = []
        for i in drawProb:
            i = i[0:5]
            b.append(i)
        c = []
        for i in lossProb:
            i = i[0:5]
            c.append(i)
        f=[]
        e=[]
        h=[]
        for i in winZd:
            if i=='bg-a':
                f.append(1)
            elif i=='bg-b':
                f.append(-1)
            elif i=='':
                f.append(0)
        for i in drawZd:
            if i=='bg-a':
                e.append(1)
            elif i=='bg-b':
                e.append(-1)
            elif i=='':
                e.append(0)
        for i in lossZd:
            if i=='bg-a':
                h.append(1)
            elif i=='bg-b':
                h.append(-1)
            elif i=='':
                h.append(0)
        d=[]
        print("****************%s30家公司数据获成功%s****************欧赔数据"%(data["gameName"],data["gameId"]))
        for i in range(len(companyName)):
            returnData = {
                "matchName":data["gameName"],
                "matchNo": data['gameId'],
                "zhuName": data['zhuName'],
                "keName": data["keName"],
                "companyId": companyId[i],
                "companyName": companyName[i],
                "statart_time": data["gameTime"],
                "win": win[i],
                "winZd": f[i],
                "draw": draw[i],
                "drawZd": e[i],
                "loss": loss[i],
                "lossZd": h[i],
                "winKeiliIndex": winKeiliIndex[i],
                "drawKeiliIndex": drawKeiliIndex[i],
                "lossKeiliIndex": lossKeiliIndex[i],
                "winProb": a[i],
                "drawProb": b[i],
                "lossProb": c[i],
                "europeFlushTime": europeFlushTime[i],
            }
            d.append(returnData)
        print(d)
        return d
    except:
        print("****************%s30家公司无数据%s****************欧赔数据"%(data["gameName"],data["gameId"]))
def get_oupei_60_data(data):
    try:
        time.sleep(2)
        getDateUrl = 'https://odds.500.com/fenxi1/ouzhi.php'
        header = {
            "user-agent": random.choice(config.userAgent),
            "referer": "ttps://odds.500.com/fenxi/ouzhi-%s.shtml"%data['gameId'],
            "cookie": config.cookie
        }
        urlData={
            "id": data['gameId'],
            "ctype": "1",
            'start': 30,
            "style": 0,
            "guojia": 0
        }

        re = requests.get(getDateUrl, headers=header,params=urlData)
        re.encoding = 'utf-8'
        result = etree.HTML(re.text)

        companyName = result.xpath("//tr[contains(@class,'tr1')]//td[contains(@class,'tb_plgs')]/@title") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[contains(@class,'tb_plgs')]/@title")
        # 公司id
        companyId = result.xpath("//tr[contains(@class,'tr1')]/@id") + result.xpath("//tr[contains(@class,'tr2')]/@id")
        # 变化时间
        europeFlushTime = result.xpath("//tr[contains(@class,'tr1')]//@data-time") + result.xpath(
            "//tr[contains(@class,'tr2')]//@data-time")
        # 胜赔率
        win = result.xpath("//tr[contains(@class,'tr1')]//td[3]//tr[2]//td[1]//text()") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[3]//tr[2]//td[1]//text()")
        # 胜赔率涨跌标识
        winZd = result.xpath("//tr[contains(@class,'tr1')]//td[3]//td[1]//@class") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[3]//td[1]//@class")
        # 平赔率
        draw = result.xpath("//tr[contains(@class,'tr1')]//td[3]//tr[2]//td[2]//text()") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[3]//tr[2]//td[2]//text()")
        # 平赔率涨跌标识
        drawZd = result.xpath("//tr[contains(@class,'tr1')]//td[3]//td[2]//@class") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[3]//td[2]//@class")
        # 负赔率
        loss = result.xpath("//tr[contains(@class,'tr1')]//td[3]//tr[2]//td[3]//text()") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[3]//tr[2]//td[3]//text()")

        # 负赔率涨跌标识
        lossZd = result.xpath("//tr[contains(@class,'tr1')]//td[3]//td[3]//@class") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[3]//td[3]//@class")

        # 胜凯利
        winKeiliIndex = result.xpath("//tr[contains(@class,'tr1')]//td[6]//tr[2]//td[1]//text()") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[6]//tr[2]//td[1]//text()"
        )
        # 平凯利
        drawKeiliIndex = result.xpath("//tr[contains(@class,'tr1')]//td[6]//tr[2]//td[2]//text()") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[6]//tr[2]//td[2]//text()"
        )
        # 负凯利
        lossKeiliIndex = result.xpath("//tr[contains(@class,'tr1')]//td[6]//tr[2]//td[3]//text()") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[6]//tr[2]//td[3]//text()"
        )
        # 胜概率
        winProb = result.xpath("//tr[contains(@class,'tr1')]//td[4]//tr[2]//td[1]//text()") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[4]//tr[2]//td[1]//text()")
        # 平概率
        drawProb = result.xpath("//tr[contains(@class,'tr1')]//td[4]//tr[2]//td[2]//text()") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[4]//tr[2]//td[2]//text()")
        # 负概率
        lossProb = result.xpath("//tr[contains(@class,'tr1')]//td[4]//tr[2]//td[3]//text()") + result.xpath(
            "//tr[contains(@class,'tr2')]//td[4]//tr[2]//td[3]//text()")


        a = []
        for i in winProb:
            i = i[0:5]
            a.append(i)
        b = []
        for i in drawProb:
            i = i[0:5]
            b.append(i)
        c = []
        for i in lossProb:
            i = i[0:5]
            c.append(i)
        f=[]
        e=[]
        h=[]
        for i in winZd:
            if i=='bg-a':
                f.append(1)
            elif i=='bg-b':
                f.append(-1)
            elif i=='':
                f.append(0)
        for i in drawZd:
            if i=='bg-a':
                e.append(1)
            elif i=='bg-b':
                e.append(-1)
            elif i=='':
                e.append(0)
        for i in lossZd:
            if i=='bg-a':
                h.append(1)
            elif i=='bg-b':
                h.append(-1)
            elif i=='':
                h.append(0)
        d=[]
        print("****************%s60家公司获取数据成功%s****************欧赔数据"%(data["gameName"],data["gameId"]))
        for i in range(len(companyName)):
            returnData = {
                "matchName":data["gameName"],
                "matchNo": data['gameId'],
                "zhuName": data['zhuName'],
                "keName": data["keName"],
                "companyId": companyId[i],
                "companyName": companyName[i],
                "statart_time": data["gameTime"],
                "win": win[i],
                "winZd": f[i],
                "draw": draw[i],
                "drawZd": e[i],
                "loss": loss[i],
                "lossZd": h[i],
                "winKeiliIndex": winKeiliIndex[i],
                "drawKeiliIndex": drawKeiliIndex[i],
                "lossKeiliIndex": lossKeiliIndex[i],
                "winProb": a[i],
                "drawProb": b[i],
                "lossProb": c[i],
                "europeFlushTime": europeFlushTime[i],
            }
            d.append(returnData)
        print(d)
        return d
    except:
        print("****************%s60家公司获取数据失败%s***************欧赔数据"%(data["gameName"],data["gameId"]))
if __name__ == '__main__':
    # for i in get_all_game():
    #     print(get_oupei_60_data(i))
    #     print(get_oupei_30_data(i))
    #     break
    # while True:
    #     time.sleep(60)
    #     tasks = []
    #     for i in get_all_game():
    #         task = threading.Thread(target=get_oupei_30_data, args=(i,))
    #         task1 = threading.Thread(target=get_oupei_60_data, args=(i,))
    #         task2 = threading.Thread(target=get_yanzhou_30_game_result, args=(i,))
    #         task3 = threading.Thread(target=get_yanzhou_60_game_result, args=(i,))
    #         tasks.append(task)
    #         tasks.append(task1)
    #         tasks.append(task2)
    #         tasks.append(task3)
    #         task.start()
    #         task1.start()
    #         task2.start()
    #         task3.start()
    #         # 等待所有线程完成
    #     for _ in tasks:
    #         _.join()
    #
    pass
