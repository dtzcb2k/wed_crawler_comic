import requests
import bs4
#預防萬一的轉碼
def ourl(url):
    r=requests.get(url)
    r.encoding=r.apparent_encoding
    d=bs4.BeautifulSoup(r.content,"lxml")
    return d
# url = "https://www.ptt.cc/bbs/LoL/index.html"
# 獲取網頁資訊，設置如果沒有回應後會取消
#一般情況
# request = requests.get(url, timeout = 30)
# data = ourl(url)
# print(data.title)
# #有的時候會遇到要再按一次確認鍵或已滿18等按鈕，需要做的就是傳給瀏覽器cookie已通過
# headers = {"cookie" : "over18=1"}
#注意!!!over18=1間不能有空格
# #接著利用requests.get()將headers傳過去
# request = requests.get(url,headers = headers)


#將資料印出來
# print(request.text)

#解析資料，data儲存被解析出來的資料，而資料格式是html.parser
# data = bs4.BeautifulSoup(request.content, "lxml")

#若想去掉<>則在後面加上.text
# print(data.title.text)

#尋找標題，但只會顯示第一個
# titles = data("div", class_ = "title")
#尋找全部則要再加上_all，接著用迴圈一個個印出來
# titles = data.find_all("div", class_ = "title")
#若想去掉<>則在後面加上a.text，因為是在<div>中的<a>
# print(titles.a.text)
#要小心如果文章被刪除就會顯示錯誤，所以要加上if去去掉沒標題的文章
# for title in titles:
#     if title.a != None:
#         print(title.a.string)

#尋找資料會需要往下找或翻頁，"a"指的是<a>，而text則是要輸入我們要找的東西
# prePage = data.find("a", class_ = "btn wide", text = "‹ 上頁")
#前往下一頁或上一頁的網址
#注意!!!只有獲取href是不行的，要觀察該網站的形式去取得完整的網址
# newUrl = "https://www.ptt.cc/"+prePage["href"]
# print(newUrl)
#接著只要將其設置為函數就可以不斷重複，進行多次爬取

#多次爬取
def getData(infor):
    request = requests.get(infor[0], timeout = 30)
    data = bs4.BeautifulSoup(request.content, "lxml")
    titles = data.find_all("div", class_ = "title")
    i=1
    for title in titles:
        #也可以在這裡加上if "關鍵字" not in title.a.content 去篩選我們要的東西
        if title.a != None:
            #如果要加上網，就在前方加上"網址"+title.a["href"]
            # print(title.a.string)
            #將爬到的資料存進infor中(位置，資料)
            # print(type(title.a["href"]))
            # print(type(title.a.string))
            # print(type(title.a.text))
            infor.insert(i,"https://www.ptt.cc/"+title.a["href"]+" "+title.a.string+"\n")
            i = i+1
    prePage = data.find("a", class_ = "btn wide", text = "‹ 上頁")
    newUrl = "https://www.ptt.cc/"+prePage["href"]
    infor[0] = newUrl
    return infor
#將資料存成list
infor = ["https://www.ptt.cc/bbs/LoL/index.html"]
# 只爬一次
# print(getData(url))
file = open("Pet_Get.txt", "w", encoding="UTF-8")
#可以設置要爬幾次
for i in range(1,4,1):
    infor=getData(infor)
    #加上分隔線以利於區分第幾頁
    file.write("--------------- 第"+str(i)+"頁---------------")
    #將infor中的資料讀出
    for j in infor:
        file.write(j)
file.close()
print("End")