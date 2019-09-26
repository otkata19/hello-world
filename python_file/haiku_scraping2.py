from urllib import request
from bs4 import BeautifulSoup
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# アクセスするURL
url = "http://www.haiku-data.jp/kigo_work_list.php?kigo_cd=1048"

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = request.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")
tr = soup.find_all('tr')

for r in tr:
    print(r.text)
