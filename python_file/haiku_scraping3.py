import csv
import pandas as pd
import requests as req
from bs4 import BeautifulSoup

#URLの指定
res = req.get("http://ohh.sisos.co.jp/cgi-bin/openhh/jsearch.cgi?group=hirarajp&dbi=20140103235455_20140104000746&se=0&sf=0&sk=")
soup = BeautifulSoup(res.text, 'html.parser')

#テーブルを指定
table = soup.find_all("table", {"class":"srl"})[0]
rows = table.find("tr")

data = []
for row in rows:
    data.append([
      rows.find("td").string
    ])

df = pd.DataFrame(data, columns = ['1'])
df.to_csv('test.csv')
