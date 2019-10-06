import csv
import codecs
import numpy as np
import pandas as pd
from janome.tokenizer import Tokenizer
from sklearn.feature_extraction.text import CountVectorizer
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#csvファイルを読み取って表にする
with codecs.open("../datasets/issa_data.csv", "r", "Shift-JIS", "ignore") as file:
    df = pd.read_table(file, delimiter=",")
    #print(df.iloc[:, 1])

data = []
each_data = []
t = Tokenizer()
for row in range(10):
    val = df.iloc[row, 1]
    tokens = t.tokenize(val)
    for token in tokens:
        partOfSpeech = token.part_of_speech.split(',')[0]
        # 今回抽出するのは名詞だけとします。（もちろん他の品詞を追加、変更、除外可能です。）
        if partOfSpeech == u'名詞':
            each_data.append(token.surface)
    data.append(each_data)
    each_data = []

print(data)


"""
    try:
        csvFile = open("../datasets/issa_wakachi_data.csv", 'wt', newline='', encoding='utf-8')
        writer = csv.writer(csvFile)
        writer.writerow(data)
    finally:
        csvFile.close()
        """
