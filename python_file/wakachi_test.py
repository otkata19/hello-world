from janome.tokenizer import Tokenizer
import pandas as pd
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#csvファイルの読み込み
df = pd.read_csv("../datasets/issa_data.csv", encoding="shift-jis")
#csvファイルの[80, 1]のテキストを取得
text = df.iloc[80, 1]
#形態素解析
t = Tokenizer()
tokens = t.tokenize(text)
#形態素解析した結果を表示
for token in tokens:
    print(token)
