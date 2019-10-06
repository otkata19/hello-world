# ライブラリのインポート
import pandas as pd
import matplotlib.pyplot as plt
import codecs
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#csvファイルを読み取って表にする
df = pd.read_csv("../datasets/okajoki_data_copy.csv",  encoding="utf-16", header = None)
print(df)

df2 = pd.read_csv("../datasets/okajoki_data2.csv",  encoding="utf-16", header = None)
df2 = df2.T
df2.to_csv("../datasets/okajoki_data2.csv")
print(df2)
