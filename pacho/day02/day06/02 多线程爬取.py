import threading
from house import *
import time

time.clock()

# 开启线程
url = "https://gz.lianjia.com/ershoufang/pg1/"
totalPage = getPage(url)

print(totalPage)

tList = []
for i in range(1, totalPage + 1):
    url = "https://gz.lianjia.com/ershoufang/pg%d/" % (i)
    t = threading.Thread(target=getHouseInfo, args=(url,))
    tList.append(t)
    t.start()

for t in tList:
    t.join()

print(time.clock())