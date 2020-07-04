import requests
import threading
import time
from lxml import etree
import random
import config

def get_all_game():
    gameIdUrl='https://live.500.com/2h1.php'
    header={
        'referer':'https://live.500.com/',
        'user-agent':random.choice(config.userAgent),
        "cookie":config.cookie
    }
    re=requests.get(gameIdUrl,headers=header)
    re.encoding='gb2312'
    result=etree.HTML(re.text)
    gameName=result.xpath("//table[contains(@class,'bf_tablelist01' )]//tbody//tr/@gy")
    gameTime=result.xpath("//table[contains(@class,'bf_tablelist01' )]//tbody//td[4]/text()")
    t=[]
    for i in gameTime:
        i=" ".join(i.split())
        t.append(i)
    gameTime=t
    gameId=result.xpath("//table[contains(@class,'bf_tablelist01' )]//tbody//tr/@fid")
    keName=result.xpath("//table[contains(@class,'bf_tablelist01' )]//tbody//tr/td[6]/a/text()")
    zhuName=result.xpath("//table[contains(@class,'bf_tablelist01' )]//tbody//tr/td[8]/a/text()")
    a=[]
    for i in range(len(gameId)):
        data={
            'gameName':gameName[i],
            'gameId':gameId[i],
            'gameTime':gameTime[i],
            'keName':keName[i],
            "zhuName":zhuName[i],

        }
        a.append(data)
    return a

def get_yanzhou_30_game_result(data):
    try:
        time.sleep(2)
        gameDataUrl="https://odds.500.com/fenxi/yazhi-%s.shtml"%data['gameId']
        header = {
            'referer': 'https://live.500.com/2h1.php',
            'user-agent': random.choice(config.userAgent),
            "cookie": config.cookie
        }

        re=requests.get(gameDataUrl,headers=header)
        re.encoding='gb2312'
        result=etree.HTML(re.text)
        # 公司名称
        companyName = result.xpath(
            "//table[contains(@class,'pub_table')]//tr[contains(@class,'tr1')]//a//span[1]//text()") + result.xpath(
            "//table[contains(@class,'pub_table')]//tr[contains(@class,'tr2')]//a//span[1]//text()")
        # 公司id
        companyId = result.xpath("//table[contains(@class,'pub_table')]//tr[contains(@class,'tr1')]/@id") + result.xpath(
            "//table[contains(@class,'pub_table')]//tr[contains(@class,'tr2')]/@id")
        # 变化时间
        gameTime = result.xpath(
            "//table[contains(@class,'pub_table')]//tr[contains(@class,'tr1')]//td[4]//time//text()") + result.xpath(
            "//table[contains(@class,'pub_table')]//tr[contains(@class,'tr2')]//td[4]//time//text()")
        # 上水系数
        upWater = result.xpath(
            "//table[contains(@class,'pub_table')]//tr[contains(@class,'tr1')]//td[3]//td[1]//text()") + result.xpath(
            "//table[contains(@class,'pub_table')]//tr[contains(@class,'tr2')]//td[3]//td[1]//text()")
        # 上水升降标识
        upZhangdie = result.xpath(
            "//table[contains(@class,'pub_table')]//tr[contains(@class,'tr1')]//td[3]//td[1]//@class") + result.xpath(
            "//table[contains(@class,'pub_table')]//tr[contains(@class,'tr2')]//td[3]//td[1]//@class")
        # 下水升降标识
        lowZhangdie = result.xpath(
            "//table[contains(@class,'pub_table')]//tr[contains(@class,'tr1')]//td[3]//td[3]//@class") + result.xpath(
            "//table[contains(@class,'pub_table')]//tr[contains(@class,'tr2')]//td[3]//td[3]//@class")
        # 下水系数
        lowWater = result.xpath(
            "//table[contains(@class,'pub_table')]//tr[contains(@class,'tr1')]//td[3]//td[3]//text()") + result.xpath(
            "//table[contains(@class,'pub_table')]//tr[contains(@class,'tr2')]//td[3]//td[3]//text()")
        # 盘面
        asiaDisk = result.xpath(
            "//table[contains(@class,'pub_table')]//tr[contains(@class,'tr1')]//td[3]//td[2]/text()") + result.xpath(
            "//table[contains(@class,'pub_table')]//tr[contains(@class,'tr2')]//td[3]//td[2]/text()")

        a=[]
        for i in lowWater:
            i=i[0:5]
            a.append(i)
        b=[]
        for i in upWater:
            i=i[0:5]
            b.append(i)
        f=[]
        for i in range(len(upZhangdie)):
            if upZhangdie[i]=="ying":
                f.append(1)
            elif upZhangdie[i]=='':
                f.append(0)
            elif upZhangdie[i]=="ping":
                f.append(-1)

        d=[]
        for i in range(len(lowZhangdie)):
            if lowZhangdie[i] == "ying":
                d.append(1)
            elif lowZhangdie[i] == '':
                d.append(0)
            elif lowZhangdie[i] == "ping":
                d.append(-1)
        # print(d)
        h=[]
        print("****************%s30家公司数据获成功%s****************亚盘数据"%(data["gameName"],data["gameId"]))
        for i in range(len(gameTime)):
            result =  {
                    "matchName":data["gameName"],
                    "matchNo": data["gameId"],
                    "zhuName": data["zhuName"],
                    "keName": data["keName"],
                    "companyId": companyId[i],
                    "companyName": companyName[i],
                    "statart_time": data["gameTime"],
                    "asiaDisk": asiaDisk[i],
                    "asiaFlushTime": gameTime[i],
                    "upWater": a[i],
                    "upZhangdie": d[i],
                    "lowWater": b[i],
                    "lowZhangdie":f[i]
                }
            h.append(result)


        return h
    except Exception as e:
        print(e)
        print("****************%s30家公司无数据%s****************亚盘数据"%(data["gameName"],data["gameId"]))
def get_yanzhou_60_game_result(data):
    try:
        time.sleep(2)
        gameDataUrl="https://odds.500.com/fenxi1/yazhi.php"
        header = {
            'referer': 'https://odds.500.com/fenxi/yazhi-%s.shtml'%data['gameId'],
            'user-agent': random.choice(config.userAgent),
            "cookie": config.cookie
        }
        gameData={
            "id":data['gameId'],
            "ctype":"1",
            'start':30,
            "style":0,
            "guojia":0
        }
        re=requests.get(gameDataUrl,headers=header,params=gameData)
        re.encoding='utf-8'
        result=etree.HTML(re.text)
        #公司名称
        companyName=result.xpath("//tr[contains(@class,'tr1')]//a//span[1]//text()")+result.xpath("//tr[contains(@class,'tr2')]//a//span[1]//text()")
        #公司id
        companyId=result.xpath("//tr[contains(@class,'tr1')]/@id")+result.xpath("//tr[contains(@class,'tr2')]/@id")
        #变化时间
        gameTime=result.xpath("//tr[contains(@class,'tr1')]//td[4]//time//text()")+result.xpath("//tr[contains(@class,'tr2')]//td[4]//time//text()")
        #上水系数
        upWater=result.xpath("//tr[contains(@class,'tr1')]//td[3]//td[1]//text()")+result.xpath("//tr[contains(@class,'tr2')]//td[3]//td[1]//text()")
        #上水升降标识
        upZhangdie=result.xpath("//tr[contains(@class,'tr1')]//td[3]//td[1]//@class")+result.xpath("//tr[contains(@class,'tr2')]//td[3]//td[1]//@class")
        #下水升降标识
        lowZhangdie=result.xpath("/tr[contains(@class,'tr1')]//td[3]//td[3]//@class")+result.xpath("//tr[contains(@class,'tr2')]//td[3]//td[3]//@class")
        #下水系数
        lowWater=result.xpath("//tr[contains(@class,'tr1')]//td[3]//td[3]//text()")+result.xpath("//tr[contains(@class,'tr2')]//td[3]//td[3]//text()")
        #盘面
        asiaDisk=result.xpath("//tr[contains(@class,'tr1')]//td[3]//td[2]/text()")+result.xpath("//tr[contains(@class,'tr2')]//td[3]//td[2]/text()")


        a=[]
        for i in lowWater:
            i=i[0:5]
            a.append(i)
        b=[]
        for i in upWater:
            i=i[0:5]
            b.append(i)
        f=[]
        for i in range(len(upZhangdie)):
            if upZhangdie[i]=="ying":
                f.append(1)
            elif upZhangdie[i]=='':
                f.append(0)
            elif upZhangdie[i]=="ping":
                f.append(-1)

        d=[]
        for i in range(len(lowZhangdie)):
            if lowZhangdie[i] == "ying":
                d.append(1)
            elif lowZhangdie[i] == '':
                d.append(0)
            elif lowZhangdie[i] == "ping":
                d.append(-1)
        # print(d)
        h=[]
        print("****************%s60家公司获取数据成功%s****************亚盘数据" % (data["gameName"],data["gameId"]))
        for i in range(len(gameTime)):
            result =  {
                    "matchName":data["gameName"],
                    "matchNo": data["gameId"],
                    "zhuName": data["zhuName"],
                    "keName": data["keName"],
                    "companyId": companyId[i],
                    "companyName": companyName[i],
                    "statart_time": data["gameTime"],
                    "asiaDisk": asiaDisk[i],
                    "asiaFlushTime": gameTime[i],
                    "upWater": a[i],
                    "upZhangdie": d[i],
                    "lowWater": b[i],
                    "lowZhangdie":f[i]
                }
            h.append(result)

        print(h)
        return h
    except Exception as e:
        print(e)
        print("****************%s60家公司获取数据失败%s****************亚盘数据" % (data["gameName"],data["gameId"]))
if __name__ == '__main__':
    for i in get_all_game():
        print(get_yanzhou_30_game_result(i))
        break
    # while True:
    #     time.sleep(60)
    #     tasks = []
    #     for i in get_all_game():
    #         task = threading.Thread(target=get_yanzhou_30_game_result, args=(i,))
    #         task1 = threading.Thread(target=get_yanzhou_60_game_result, args=(i,))
    #         tasks.append(task)
    #         tasks.append(task1)
    #         task.start()
    #         task1.start()
    #         # 等待所有线程完成
    #     for _ in tasks:
    #         _.join()
    pass