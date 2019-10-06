import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

# csvファイルを作成して開く
csvFile = open("../datasets/okajoki_data.csv", 'wt', newline='', encoding='utf-8')
csvRow = []

for num in range(1, 1001):
    csvFile = open("../datasets/okajoki_data.csv", 'a', encoding='utf-8')
    html = urlopen("http://okajoki.com/db/search.php?page=" + str(num))
    time.sleep(15)
    bsObj = BeautifulSoup(html, "html.parser")
    for cell in bsObj.findAll("td", {"class": "search_sakuhin"}):
        csvRow.append(cell.get_text())

#csvRowのリストデータをcsvファイルに書き込み
try:
    writer = csv.writer(csvFile)
    writer.writerow(csvRow)
#csvファイルを閉じる
finally:
    csvFile.close()
