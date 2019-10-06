import csv
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import time

# csvファイルを作成して開く
csvFile = open("../datasets/okajoki_data_4_6.csv", 'wt', newline='', encoding='utf-8')
csvRow = []

for num in range(3, 6):
    csvFile = open("../datasets/okajoki_data_4_6.csv", 'a', encoding='utf-8')
    html = requests.get("http://okajoki.com/db/search.php?page=" + str(num))
    time.sleep(15)
    print(html.encoding)
    bsObj = BeautifulSoup(html.content, "html.parser", from_encoding='utf-8')
    for cell in bsObj.findAll("td", {"class": "search_sakuhin"}):
        csvRow.append(cell.get_text())

#csvRowのリストデータをcsvファイルに書き込み
try:
    writer = csv.writer(csvFile)
    writer.writerow(csvRow)
#csvファイルを閉じる
finally:
    csvFile.close()
