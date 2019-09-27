import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

#csvファイルを作成
csvFile = open("data.csv", 'wt', newline='', encoding='utf-8')
#
for num in range(20, 22120, 20):
    csvFile = open("data.csv", 'a', newline='', encoding='utf-8')
    html = urlopen("http://ohh.sisos.co.jp/cgi-bin/openhh/jsearch.cgi?group=hirarajp&dbi=20140103235455_20140104000746&s_entry=" + str(num) + "&se0=0&sf0=0&sk0=")
    time.sleep(15)
    bsObj = BeautifulSoup(html, "html.parser")
    # テーブルを指定
    table = bsObj.findAll("table", {"class": "srl"})[0]
    rows = table.findAll("tr")
    #1行目、2行目を消す
    del rows[:2]
    #csvファイルに書き込み
    try:
        writer = csv.writer(csvFile)
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td']):
                csvRow.append(cell.get_text())

            writer.writerow(csvRow)
    finally:
        csvFile.close()
