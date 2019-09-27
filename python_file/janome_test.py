import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

# csvファイルを作成して開く
csvFile = open("../datasets/ghk_data.csv", 'wt', newline='', encoding='utf-8')

for num in range(1, 5):
    csvFile = open("../datasets/ghk_data.csv", 'a', newline='', encoding='utf-8')
    html = urlopen("http://haiku-data.jp/work_detail.php?cd=" + str(num))
    time.sleep(10)
    bsObj = BeautifulSoup(html, "html.parser")
    # テーブルを指定
    title = bsObj.findAll("div", {"class": "title"})[0]
    rows = title.findAll("b")
    #rowに入ったテキストデータをcsvファイルに書き込み
    try:
        writer = csv.writer(csvFile)
        for row in rows:
            csvRow = []
            #for cell in row.find(['b']):
            csvRow.append(row.get_text())
            writer.writerow(csvRow)
    #csvファイルを閉じる
    finally:
        csvFile.close()
