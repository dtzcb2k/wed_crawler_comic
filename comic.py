import requests
import bs4
#多次爬取
def getData(infor):
    request = requests.get(infor[0], timeout = 30)
    #清空infor的空間
    infor=[""]
    data = bs4.BeautifulSoup(request.content, "lxml")
    #a(變數名稱) = data.find_all("a"抓取標籤, class_ = "bcover"屬於哪一個類別)
    titles = data.find_all("p", class_ = "ell")

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
            infor.insert(i,"https://www.manhuagui.com/"+title.a["href"]+" "+title.a.string+"\n")
            i = i+1
    prePage = data.find("a", class_ = "prev", text = "下一页")
    newUrl = "https://www.manhuagui.com/"+prePage["href"]
    infor[0] = newUrl
    return infor
#將資料存成list
infor = ["https://www.manhuagui.com/list/view.html"]
# 只爬一次
# print(getData(infor))
file = open("Pet_Get_comic.txt", "w", encoding="UTF-8")
#可以設置要爬幾次
for x in range(1,4,1):
    #如果要將資料分開儲存
    #file = open("Pet_Get"+str(x)+".txt", "w", encoding="utf-8")
    #加上分隔線以利於區分第幾頁
    file.write("--------------- 第"+str(x)+"頁---------------\n")
    #顯使該頁介面，因為在儲存的時候就將下一頁的網址設置在[0]的位置
    file.write(infor[0]+" 第"+str(x)+"頁"+"\n")
    infor=getData(infor)
    #將infor中的資料讀出
    for j in infor[1:]:
        file.write(j)
    #結束時關掉
    #file.close()
#結束時關掉，以減少占用空間        
file.close()
print("End")