#打開檔案
#open的權限，"w" 以覆寫模式打開檔案，"r" : 以唯讀模式打開檔案，"a" : 以續寫模式打開檔案
#變數名 = open("檔名", "模式" , encoding="UTF-8")
#open的功能是打開檔案，但如果沒有這個檔案則會直接創建該檔案

file = open("file.text", "w", encoding = "UTF-8")
file.write("茲茲茲茲")

file = open("file.text", "r", encoding = "UTF-8")
print(file.read())

#當檔案用完後記得要關閉以釋放運算資源，close()
file.close()