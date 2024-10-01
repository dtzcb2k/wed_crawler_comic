import requests
#處理資料夾的套件
import os
import bs4
#簡單抓取一張圖片
# def saveImage(postUrl):
#     #存放照片的位置
#     path=r"C:/Microsoft VS Code/VS Live server\web crawler/use requests beautifulsoup4/Pet_Get_picture"
#     #判斷是否有沒有該路徑，如果沒有就建一個
#     if (os.path.exists(path) == False):
#         os.makedirs(path)
#     #抓取圖片
#     getImage=requests.get(postUrl)
#     #將圖片轉成二進位
#     image=getImage.content
#     #建立檔案
#     imageSave=open(path+"/imp.png","wb")
#     imageSave.write(image)
#     imageSave.close()
    # #抓取圖片
    # getImage=requests.get(postUrl)
    # #將圖片轉成二進位
    # image=getImage.content
    # #建立檔案
    # imageSave=open(path+"/imp.png","wb")
    # imageSave.write(image)
    # imageSave.close()
#圖片網址
# postUrl = "https://th.bing.com/th/id/OIP.Az1J-P0Ul9Ad5YFpf0w36QHaJ2?pid=ImgDet&rs=1"
# saveImage(postUrl)
# print("End")

#用爬蟲抓圖片
def saveImage(postUrl):
    #對網頁發出請求
    request = requests.get(postUrl)
    #檢析網頁原始碼
    data = bs4.BeautifulSoup(request.text, "lxml")
    #要抓的標籤
    imageData = data.find_all("img")
    #存放照片的位置
    path=r"C:/Microsoft VS Code/VS Live server\web crawler/use requests beautifulsoup4/Pet_Get_picture"
    #判斷是否有沒有該路徑，如果沒有就建一個
    if (os.path.exists(path) == False):
        os.makedirs(path)
    #儲存圖片網址的地方
    imgList = []
    #紀錄抓到多少資料，這裡也可以直接設定要多少組資料
    lenth = len(imageData)
    #將找到的圖片放進list中
    for x in range(lenth):
        imgList.insert(x, imageData[x].attrs["src"])
    for i in range(lenth):
        #選擇要印出的圖片資料
        getImage = requests.get(imgList[i])
        #將圖片轉成二進位置
        image = getImage.content
        imageSave = open(path+"/img"+str(i)+".png","wb")
        imageSave.write(image)
        imageSave.close()
        print("img"+str(i)+".png"+"下載成功")

postUrl = "https://www.bing.com/images/search?q=%E5%8D%A1%E5%A4%9A%E5%85%8B%C2%B7%E6%B3%BD%E5%A7%86%E9%9C%B2%E6%99%AE%E6%96%AF&qs=UT&form=QBIRMH&sp=2&pq=%E5%8D%A1%E5%A4%9A%E5%85%8B&sk=LT1&sc=8-3&cvid=6C061A89AE6E4ACCA08377BA5891579C&first=1&tsc=ImageHoverTitle"
saveImage(postUrl)
print("End")